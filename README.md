# 🌧️ Atividade Parcial - Integração de Sistema - API de Monitoramento e Alerta de Alagamentos em Fortaleza

## 📌 Objetivo
Este projeto tem como objetivo desenvolver uma **API de integração** entre sistemas de sensores pluviométricos e o sistema da Defesa Civil de Fortaleza.

A API coleta dados de chuva em tempo real, processa regras de risco e emite alertas de alagamento para comunidades vulneráveis (ex.: Praia do Futuro, Mucuripe, Pirambu), contribuindo com o ODS 11 – Cidades e comunidades sustentáveis.

## 👥 Equipe

Herison Daniel Wanderley  – 2315221 - Responsável pela documentação de requisitos, execução da primeira fase de implementação, realização dos primeiros testes e elaboração do relatório final.

Millene de Souza Júnior   – 2326165  - Responsável pela segunda fase de implementação, garantindo a integração das funcionalidades desenvolvidas.

Talles de Lima Pereira    – 2326201  - Responsável pela terceira fase de implementação, focando na codificação e ajustes finais das funcionalidades.

João Eduardo Lúcio Araújo – 291356   - Responsável pela segunda fase de testes, verificando a qualidade e o funcionamento das implementações.


## 🏗️ Arquitetura da Solução

A solução integra dois sistemas distintos:

Sensores de chuva → fornecem dados pluviométricos

Defesa Civil/App Moradores → recebem alertas emitidos pela API

**Diagrama de Arquitetura**

`[Sensores de Chuva]` --> `[API Integração]` --> `[Banco de Dados Alertas]`
                                      \
                                       --> `[Aplicativo Defesa Civil / Moradores]`

## 📡 Endpoints da API
1. POST /sensores/dados

Recebe dados de chuva de um sensor e avalia risco de alagamento.

Exemplo de Request

{
  "sensor_id": "SENSOR_MUCURIPE_01",
  "chuva_mm": 62,
  "data_hora": "2025-09-08T14:35:00Z"
}


Resposta

{
  "status": "ok",
  "alerta": "risco_alagamento",
  "mensagem": "Volume de chuva acima do limite. Notificação enviada."
}

2. GET /alertas/{sensor_id}

Retorna os alertas registrados para um sensor/bairro.

Exemplo de Resposta

{
  "sensor_id": "SENSOR_MUCURIPE_01",
  "alertas": [
    {
      "nivel": "risco_alagamento",
      "mensagem": "Chuva intensa registrada",
      "data_hora": "2025-09-08T14:35:00Z"
    }
  ]
}

##⚙️ Regras de Negócio

chuva_mm > 50 → risco de alagamento

30 <= chuva_mm <= 50 → alerta de atenção

chuva_mm < 30 → situação normal

## ▶️ Como Executar o Projeto
Pré-requisitos

Python 3.9+

Pip

Instalação
pip install fastapi uvicorn pytest

Rodando a API
uvicorn src.main:app --reload

Acessando a documentação

Swagger UI → http://127.0.0.1:8000/docs

ReDoc → http://127.0.0.1:8000/redoc

## ✅ Testes

Rodar com:

pytest

## 📂 Estrutura do Repositório
projeto-alagamentos/
│── src/
│   └── main.py          # Código principal da API
│── tests/
│   └── test_api.py      # Testes unitários
│── docs/
│   └── arquitetura.png  # (diagrama a ser adicionado)
│── postman_collection.json
│── README.md
│── requirements.txt

## 🧪 Postman/Insomnia

Arquivo postman_collection.json incluído no repositório

Permite simular requisições aos endpoints

## 📄 requirements.txt
fastapi==0.111.0
uvicorn[standard]==0.30.1
pydantic==2.7.1
pytest==8.2.2
httpx==0.27.0

## 📌 Explicação das dependências

fastapi → framework principal da API

uvicorn[standard] → servidor ASGI rápido para rodar a API

pydantic → validação de dados (já usado nos modelos)

pytest → framework de testes unitários

httpx → cliente HTTP usado internamente nos testes com TestClient

## ▶️ Como instalar

Após criar o ambiente virtual, rodar:

pip install -r requirements.txt

🏆 Checklist

 API integra 2 sistemas distintos (sensores + Defesa Civil/App moradores)

 2 endpoints funcionais implementados

 Uso do protocolo REST/HTTP

 Tratamento de erros e exceções

 Testes unitários incluídos

 Estrutura do repositório conforme orientações

 Relacionamento com ODS 11 explicado

 Coleção Postman/Insomnia exportada

## 📖 Referências

FastAPI Documentation

Swagger/OpenAPI

Postman Docs

ODS 11 – ONU
