# main.py
# Ponto de entrada da API: rotas REST para o recurso "visitas"

from fastapi import FastAPI, Depends, HTTPException, Query, Header, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from database import Base, engine, get_db
from schemas import VisitaCreate, VisitaUpdate, VisitaOut
import crud

# Inicializa tabelas no banco
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Conservadora - Agendamento de Visitas",
    description="API REST para gerenciamento de agendamentos de visitas técnicas com FastAPI + SQLAlchemy.",
    version="1.0.0",
)

# Configuração de CORS para permitir acesso local/frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Validação simples de API Key no header 
API_KEY_SECRET = "conservadora123"

def verificar_api_key(x_api_key: str = Header(..., description="Chave de API para autenticação")):
    if x_api_key != API_KEY_SECRET:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Chave de API inválida ou ausente."
        )


@app.get("/", summary="Página Inicial")
def inicio():
    return {"mensagem": "API da Conservadora rodando com sucesso! Acesse /docs para testar os endpoints e usa-la."}



@app.get("/health", summary="Verifica saúde da API")
def healthcheck():
    """
    Healthcheck simples para ver se a API está de pé.
    """
    return {"status": "ok"}

@app.get(
    "/visitas",
    response_model=List[VisitaOut],
    summary="Listar visitas técnicas",
    tags=["visitas"]
)
def listar_visitas(
    skip: int = Query(0, ge=0, description="Número de registros a pular"),
    limit: int = Query(50, ge=1, le=200, description="Máximo de registros a retornar"),
    tipo_servico: str | None = Query(None, description="Filtro por tipo de serviço (parcial)"),
    db: Session = Depends(get_db)
):
    """
    Retorna lista paginada de visitas. Filtro opcional por tipo de serviço.
    """
    results = crud.list_visitas(db, skip=skip, limit=limit, tipo_servico=tipo_servico)
    return results

@app.get(
    "/visitas/{visita_id}",
    response_model=VisitaOut,
    summary="Obter visita por ID",
    tags=["visitas"]
)
def obter_visita(visita_id: int, db: Session = Depends(get_db)):
    """
    Retorna uma visita pelo ID. 404 se não existir.
    """
    visita = crud.get_visita(db, visita_id)
    if not visita:
        raise HTTPException(status_code=404, detail="Visita não encontrada")
    return visita

@app.post(
    "/visitas",
    response_model=VisitaOut,
    status_code=201,
    summary="Criar novo agendamento de visita",
    tags=["visitas"]
)
def criar_visita(payload: VisitaCreate, db: Session = Depends(get_db)):
    """
    Cria uma nova visita técnica. Retorna o recurso criado.
    """
    visita = crud.create_visita(db, payload)
    return visita

@app.put(
    "/visitas/{visita_id}",
    response_model=VisitaOut,
    summary="Atualizar visita por ID",
    tags=["visitas"]
)
def atualizar_visita(visita_id: int, payload: VisitaUpdate, db: Session = Depends(get_db)):
    """
    Atualiza uma visita existente (campos fornecidos). 404 se não existir.
    """
    visita = crud.get_visita(db, visita_id)
    if not visita:
        raise HTTPException(status_code=404, detail="Visita não encontrada")
    visita = crud.update_visita(db, visita, payload)
    return visita

@app.delete(
    "/visitas/{visita_id}",
    status_code=200,
    summary="Excluir visita por ID (Protegido por API Key)",
    tags=["visitas"],
    dependencies=[Depends(verificar_api_key)]
)
def excluir_visita(visita_id: int, db: Session = Depends(get_db)):
    """
    Exclui uma visita do banco, 404 se não existir.
    """
    visita = crud.get_visita(db, visita_id)
    if not visita:
        raise HTTPException(status_code=404, detail="Visita não encontrada")
    crud.delete_visita(db, visita)

    return {
        "mensagem": f"Visita ID {visita_id} excluída com sucesso!",
        "sucesso": True
    }