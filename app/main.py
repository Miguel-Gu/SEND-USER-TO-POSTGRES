from fastapi import FastAPI, status, Depends
from fastapi.responses import JSONResponse
from fastapi.logger import logger
from sqlalchemy.orm import Session
from app.sender import insert_usuario
from app.database import get_db
from app.models import UsuarioEntrada


app = FastAPI()

@app.get("/")
def root():
    return {"message": "ok"}

@app.post("/novousuario")
def post_usuario(payload: UsuarioEntrada, db: Session = Depends(get_db)):
    try:
        insert_usuario(payload, db)
    
    except Exception as error:
        logger.warning("Error when sending data to postgres")
        logger.warning(f"error - {error}")
    
    return JSONResponse(status_code=status.HTTP_200_OK, content="Data send with sucess")