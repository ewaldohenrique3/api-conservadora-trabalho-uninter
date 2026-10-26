# schemas.py
# Modelos Pydantic para entrada/saída da API (validação e serialização)

from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

class VisitaBase(BaseModel):
    """
    Base de dados para criar/atualizar visitas.
    """
    nome_responsavel_tecnico: str = Field(min_length=3, max_length=150)
    nome_cliente_condominio: str = Field(min_length=3, max_length=150)
    cnpj_condominio: str = Field(min_length=14, max_length=20)
    endereco: str = Field(min_length=5, max_length=200)
    data_hora: datetime
    nome_sindico: str = Field(min_length=3, max_length=150)
    contato_sindico: str = Field(min_length=8, max_length=50)
    tipo_servico: str = Field(min_length=3, max_length=100)

class VisitaCreate(VisitaBase):
    """
    Payload para criação de visita.
    """
    pass

class VisitaUpdate(BaseModel):
    """
    Payload para atualização parcial/total de visita.
    Todos os campos são opcionais para permitir atualizações dinâmicas via PUT.
    """
    nome_responsavel_tecnico: str | None = Field(default=None, min_length=3, max_length=150)
    nome_cliente_condominio: str | None = Field(default=None, min_length=3, max_length=150)
    cnpj_condominio: str | None = Field(default=None, min_length=14, max_length=20)
    endereco: str | None = Field(default=None, min_length=5, max_length=200)
    data_hora: datetime | None = None
    nome_sindico: str | None = Field(default=None, min_length=3, max_length=150)
    contato_sindico: str | None = Field(default=None, min_length=8, max_length=50)
    tipo_servico: str | None = Field(default=None, min_length=3, max_length=100)
    status: str | None = Field(default=None, max_length=50)

class VisitaOut(BaseModel):
    """
    Resposta enviada ao cliente.
    """
    model_config = ConfigDict(from_attributes=True)

    id: int
    nome_responsavel_tecnico: str
    nome_cliente_condominio: str
    cnpj_condominio: str
    endereco: str
    data_hora: datetime
    nome_sindico: str
    contato_sindico: str
    tipo_servico: str
    status: str
    created_at: datetime | None