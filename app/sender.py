from sqlalchemy.orm import Session
from fastapi.logger import logger
from app.models import Usuario, UsuarioEntrada


def insert_usuario(data: UsuarioEntrada, db: Session):
    try:

        data = dict(data.usuario)
        novo_usuario = Usuario(
            nome=data.get("nome"),
            email=data.get("email"),
            cpf=data.get("cpf"),
            datanascimento=data.get("datanascimento"),
            cep=data.get("cep"),
            endereco=data.get("endereco"),
            numero=data.get("numero"),
            complemento=data.get("complemento")
        )

        db.add(novo_usuario)
        db.commit()
        db.refresh(novo_usuario)

        return True
    
    except Exception as error:
        logger.warning(str(error))
        db.rollback()

        return False