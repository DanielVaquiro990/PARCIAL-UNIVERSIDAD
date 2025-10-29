from sqlalchemy import Table, Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

matriculas_table = Table(
    "matriculas",  # Nombre de la tabla en la base de datos
    Base.metadata, # Se asocia a la estructura de SQLAlchemy
    Column("curso_id", Integer, ForeignKey("cursos.id")),        # Relación con Curso
    Column("estudiante_id", Integer, ForeignKey("estudiantes.id"))  # Relación con Estudiante
)

class Cursos(Base):

    __tablename__ = "Cursos"

    codigo = Column(Integer, primary_key=True, index=True)   # Codigo curso (clave primaria)
    nombre = Column(String, index=True) # Nombre curso
    credito = Column(Integer) # Creditos del curso
    horario = Column(Boolean) #Horario del curso


    # Relación N:M → curso tiene muchos estudiantes
    estudiantes = relationship(
        "Estudiante",  # Clase destino
        secondary=matriculas_table,  # Tabla intermedia
        back_populates="cursos"  # Relación inversa
    )


class Estudiantes(Base):
    __tablename__ = "Estudiantes"

    cedula = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    email = Column(String, index=True)
    semestre = Column(Integer)

    # Relación N:M → estudiante tiene muchos cursos
    cursos = relationship(
        "Curso",
        secondary=matriculas_table,
        back_populates="estudiantes"
    )