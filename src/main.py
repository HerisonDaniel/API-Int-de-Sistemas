from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import List, Dict

app = FastAPI(
    title="API Monitoramento de Alagamentos",
    description="Integração entre sensores pluviométricos e sistema de alertas da Defesa Civil",
    version="1.0.0"
)

# ---------------------------
# MODELOS DE DADOS
# ---------------------------
class SensorData(BaseModel):
    sensor_id: str
    chuva_mm: float
    data_hora: datetime

class Alerta(BaseModel):
    nivel: str
    mensagem: str
    data_hora: datetime

# ---------------------------
# BANCO DE DADOS SIMULADO (em memória)
# ---------------------------
alertas_db: Dict[str, List[Alerta]] = {}

# ---------------------------
# ENDPOINTS
# ---------------------------

@app.post("/sensores/dados")
def receber_dados(sensor: SensorData):
    """
    Recebe dados de um sensor e gera alerta se necessário.
    """
    # Validações simples
    if sensor.chuva_mm < 0:
        raise HTTPException(status_code=400, detail="Valor de chuva_mm inválido (negativo).")

    # Regras de negócio
    if sensor.chuva_mm > 50:
        nivel = "risco_alagamento"
        mensagem = "Volume de chuva acima do limite. Notificação enviada."
    elif 30 <= sensor.chuva_mm <= 50:
        nivel = "atencao"
        mensagem = "Chuva moderada registrada. Atenção recomendada."
    else:
        nivel = "normal"
        mensagem = "Sem risco de alagamento."

    alerta = Alerta(nivel=nivel, mensagem=mensagem, data_hora=sensor.data_hora)

    # Salvar alerta por sensor_id
    if sensor.sensor_id not in alertas_db:
        alertas_db[sensor.sensor_id] = []
    alertas_db[sensor.sensor_id].append(alerta)

    return {"status": "ok", "alerta": nivel, "mensagem": mensagem}


@app.get("/alertas/{sensor_id}")
def listar_alertas(sensor_id: str):
    """
    Lista os alertas registrados para um sensor/bairro específico.
    """
    if sensor_id not in alertas_db:
        raise HTTPException(status_code=404, detail="Sensor não encontrado ou sem alertas")

    return {"sensor_id": sensor_id, "alertas": alertas_db[sensor_id]}


@app.get("/status/sensores")
def status_sensores():
    """Retorna resumo simples do estado dos sensores (dados em memória)."""
    resumo = []
    for sid, alerts in alertas_db.items():
        ultimo = alerts[-1] if alerts else None
        resumo.append({
            "sensor_id": sid,
            "ultimo_alerta": ultimo.dict() if ultimo else None,
            "total_alertas": len(alerts)
        })
    return {"sensores": resumo}
