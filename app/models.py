from datetime import date
from pydantic import BaseModel
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class DadosUsuario(BaseModel):
    nome: str
    email: str
    cpf: str
    datanascimento: date
    cep: str
    endereco: str
    numero: str
    complemento: str

class UsuarioEntrada(BaseModel):
    usuario: DadosUsuario

class Base(DeclarativeBase):
    pass

class Usuario(Base):
    __tablename__ = "usuario"
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    email: Mapped[str]
    cpf: Mapped[str]
    datanascimento: Mapped[date]
    cep: Mapped[str]
    endereco: Mapped[str]
    numero: Mapped[str]
    complemento: Mapped[str]
    __table_args__ = {'schema': 'usuario'}