from app import db
from datetime import datetime


class Contato(db.Model):
    id = db.Colunm(db.Integer, primary_key= True)
    data_envio = db.Comlunm(db.Datatime, default = datetime.utc())
    nome = db.Colunm(db.String, nullable= True)
    email = db.Colunm(db.String, nullable= True)
    assunto = db.Colunm(db.String, nullable= True)
    mensagem = db.Colunm(db.String, nullable= True)