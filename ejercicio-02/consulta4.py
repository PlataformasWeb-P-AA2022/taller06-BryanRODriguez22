from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

# se importa la clase(s) del
# archivo genera_tablas
from genera_base import Pais

engine = create_engine('sqlite:///datospaisese.db')

Session = sessionmaker(bind=engine)
session = Session()

# Presentar los países ordenados por la capital, siempre que el país pertenezca a Europa

info_pais = session.query(Pais.nombre_pais,Pais.capital).filter(Pais.continente=='EU').order_by(Pais.capital).all()
print(info_pais)