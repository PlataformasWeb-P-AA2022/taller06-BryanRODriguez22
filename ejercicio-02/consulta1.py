from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ 

from genera_base import Pais

Session = sessionmaker(bind=engine)
session = Session()

#Presentar todos los países del continente americano
Pais =  session.query(Pais).filter(or_(Pais.continente =="SA", Pais.continente == "NA")