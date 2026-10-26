# models.py
# Modelos de dados do domínio "visitas" usando SQLAlchemy ORM

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base

class Visita(Base):
    """
    Representa o agendamento de uma visita técnica da conservadora:
    - nome_responsavel_tecnico: técnico responsável pela visita
    - nome_cliente_condominio: nome do condomínio ou estabelecimento
    - cnpj_condominio: CNPJ do local
    - endereco: endereço da visita
    - data_hora: data e hora do agendamento
    - nome_sindico: responsável local
    - contato_sindico: telefone/contato do responsável
    - tipo_servico: tipo do serviço a ser realizado
    - status: status atual do agendamento
    - created_at: timestamp de criação no banco
    """
    __tablename__ = "visitas"

    id = Column(Integer, primary_key=True, index=True)
    nome_responsavel_tecnico = Column(String(150), nullable=False)
    nome_cliente_condominio = Column(String(150), nullable=False, index=True)
    cnpj_condominio = Column(String(20), nullable=False)
    endereco = Column(String(200), nullable=False)
    data_hora = Column(DateTime(timezone=True), nullable=False)
    nome_sindico = Column(String(150), nullable=False)
    contato_sindico = Column(String(50), nullable=False)
    tipo_servico = Column(String(100), nullable=False, index=True)
    status = Column(String(50), default="Agendado")
    created_at = Column(DateTime(timezone=True), server_default=func.now())