from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ 

from genera_base import Pais
engine = create_engine('sqlite:///datospaisese.db')

Session = sessionmaker(bind=engine)
session = Session()

#Presentar todos los países del continente americano
info_pais = session.query(Pais).filter(Pais.continente.in_(['NA','SA','CA'])).all()
print(info_pais)