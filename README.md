# API de Monitoramento e Alerta de Alagamentos em Fortaleza

## Objetivo
Esta API integra sensores pluviométricos e um sistema de alertas para a Defesa Civil e moradores,
gerando notificações quando os níveis de chuva atingem valores críticos.

## Estrutura do Repositório
```
projeto-alagamentos/
│── src/
│   └── main.py
│── tests/
│   └── test_api.py
│── docs/
│   └── arquitetura.png
│── postman_collection.json
│── README.md
│── requirements.txt
│── .gitignore
```

## Como rodar localmente
1. Extraia o conteúdo do ZIP em uma pasta local.
2. Crie um ambiente virtual (recomendado) e instale dependências:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # macOS / Linux
   .\.venv\\Scripts\\activate  # Windows PowerShell (ou use o equivalente cmd)
   pip install -r requirements.txt
   ```
3. Inicie a API:
   ```bash
   uvicorn src.main:app --reload
   ```
4. Acesse a documentação automática:
   - Swagger: http://127.0.0.1:8000/docs
   - ReDoc: http://127.0.0.1:8000/redoc

## Testes
Execute:
```bash
pytest
```

## Postman
Importe o arquivo `postman_collection.json` presente na raiz do projeto.

## O que editar antes de enviar
- Atualize o arquivo README.md com os nomes da equipe e matrículas.
- Adicione o diagrama/arquivos extras na pasta `docs/` se necessário.
