from sqlalchemy import Table, Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship
from database import Base

matriculas_table = Table(
    "matriculas",  # Nombre de la tabla en la base de datos
    Base.metadata, # Se asocia a la estructura de SQLAlchemy
    Column("curso_id", Integer, ForeignKey("cursos.id")),        # Relación con Curso
    Column("estudiante_id", Integer, ForeignKey("estudiantes.id"))  # Relación con Estudiante
)

class Curso(Base):

    __tablename__ = "cursos"

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(Integer, index=True, unique=True)   # Codigo curso (clave primaria), codigo del curso unico (unique=True)
    nombre = Column(String, index=True) # Nombre curso
    creditos = Column(Integer) # Creditos del curso
    horario = Column(String) #Horario del curso


    # Relación N:M → curso tiene muchos estudiantes
    estudiantes = relationship(
        "Estudiante",  # Clase destino
        secondary=matriculas_table,  # Tabla intermedia
        back_populates="cursos"  # Relación inversa
    )


class Estudiante(Base):
    __tablename__ = "estudiantes"

    id = Column(Integer, primary_key=True, index=True)
    cedula = Column(Integer, index=True, unique=True) #cedula unica (unique=True)
    nombre = Column(String, index=True)
    email = Column(String, index=True)
    semestre = Column(Integer)

    # Relación N:M → estudiante tiene muchos cursos
    cursos = relationship(
        "Curso",
        secondary=matriculas_table,
        back_populates="estudiantes"
    )
