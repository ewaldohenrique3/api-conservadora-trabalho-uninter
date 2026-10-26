# crud.py
# Funções de acesso ao banco para o recurso Visita

from sqlalchemy.orm import Session
from models import Visita
from schemas import VisitaCreate, VisitaUpdate

def list_visitas(db: Session, skip: int = 0, limit: int = 50, tipo_servico: str | None = None):
    """
    Lista visitas com paginação simples e filtro por tipo de serviço opcional.
    """
    query = db.query(Visita)
    if tipo_servico:
        query = query.filter(Visita.tipo_servico.ilike(f"%{tipo_servico}%"))
    return query.offset(skip).limit(limit).all()

def get_visita(db: Session, visita_id: int):
    """
    Busca visita por ID.
    """
    return db.query(Visita).filter(Visita.id == visita_id).first()

def create_visita(db: Session, payload: VisitaCreate):
    """
    Cria nova visita a partir do payload validado.
    """
    visita = Visita(**payload.model_dump())
    db.add(visita)
    db.commit()
    db.refresh(visita)
    return visita

def update_visita(db: Session, visita: Visita, payload: VisitaUpdate):
    """
    Atualiza campos fornecidos no payload (atualização parcial/total).
    """
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(visita, field, value)
    db.commit()
    db.refresh(visita)
    return visita

def delete_visita(db: Session, visita: Visita):
    """
    Remove visita do banco.
    """
    db.delete(visita)
    db.commit()