# API de Agendamento de Visitas Técnicas — Conservadora 

API RESTful desenvolvida em Python com **FastAPI** e **SQLAlchemy** para o gerenciamento de agendamentos de visitas técnicas, vistorias prediais e manutenções em condomínios e estabelecimentos comerciais.

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.12
- **Framework Web:** FastAPI
- **Servidor ASGI:** Uvicorn
- **ORM / Persistência:** SQLAlchemy (SQLite)
- **Validação de Dados:** Pydantic
- **Documentação:** Swagger UI / OpenAPI

## 🚀 Como Executar o Projeto

### 1. Clonar o repositório
```bash
git clone https://github.com/ewaldohenrique3/api-conservadora-trabalho-uninter.git
cd api-conservadora-trabalho-uninter
```

### 2. Criar e ativar o ambiente virtual
```bash
python -m venv venv

# Windows (CMD)
.\venv\Scripts\activate.bat

# Windows (PowerShell)
.\venv\Scripts\Activate.ps1
```

### 3. Instalar as dependências
```bash
pip install -r requirements.txt
```

### 4. Iniciar o servidor
```bash
uvicorn main:app --reload
```

A API estará disponível em: `http://127.0.0.1:8000`

## 📖 Documentação dos Endpoints (Swagger)

Com o servidor rodando, acesse a documentação interativa em:
👉 **`http://127.0.0.1:8000/docs`**

### Principais Rotas
- `GET /health` — Verifica o status de funcionamento da API.
- `GET /visitas` — Lista os agendamentos cadastrados (com filtro opcional por `tipo_servico`).
- `GET /visitas/{visita_id}` — Obtém os detalhes de um agendamento específico.
- `POST /visitas` — Cadastra um novo agendamento de visita técnica.
- `PUT /visitas/{visita_id}` — Atualiza os dados de um agendamento existente.
- `DELETE /visitas/{visita_id}` — Remove um agendamento do sistema (requer o cabeçalho `X-API-Key: conservadora123`).
