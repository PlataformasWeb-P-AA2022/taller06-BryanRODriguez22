from sqlalchemy import create_engine

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///datospaisese.db')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String

class Pais(Base):
    __tablename__ = 'informacion_paiese'
    
    id = Column(Integer, primary_key=True)
    nombre_pais = Column(String)
    capital = Column(String)
    continente = Column(String)
    dial = Column(String)
    geoname_id = Column(String)
    ITU = Column(String)
    Lenguajes = Column(String)
    Dependencia = Column(String)

    def __repr__(self):
        return "Paises: nombre_pais=%s capital=%s continente:%s dial:%s ,\
            geoname_id=%s ITU=%s Lenguajes=%s Dependencia=%s " % (
                          self.nombre_pais,
                          self.capital,
                          self.continente,
                          self.dial,
                          self.geoname_id,
                          self.ITU,
                          self.Lenguajes,
                          self.Dependencia)
Base.metadata.create_all(engine)

