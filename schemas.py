from pydantic import BaseModel
from typing import List, Optional

#CURSOS

#Atributos base de un curso
class CursoBase(BaseModel):
    codigo: int
    nombre: str
    creditos: int
    horario: str

#Obtener curso y estudiantes
class Curso(CursoBase):
    codigo: int
    estudiantes: List["Estudiante"] = [] #Relacion N:M

class CrearCurso(CursoBase):
    pass

#ESTUDIANTES
class EstudianteBase(BaseModel):
    cedula: int
    nombre: str
    email: str
    semestre: int

class CrearEstudiante(EstudianteBase):
    pass

#Muestra estudiante y cursos matriculados
class InfoEstudiante(EstudianteBase):
    id: int
    cursos: List[Curso] = [] #Realacion N:M

class ActualizarEstudiante(EstudianteBase):
    cedula: Optional[int] = None
    nombre: Optional[str] = None
    email: Optional[str] = None
    semestre: Optional[str] = None

