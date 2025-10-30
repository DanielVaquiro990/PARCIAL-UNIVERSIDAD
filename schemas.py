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

#Crea curso
class CrearCurso(CursoBase):
    pass

#Actualiza la informacion de los cursos
class ActualizarCurso(CursoBase):
    codigo: Optional[int] = None
    nombre: Optional[str] = None
    creditos: Optional[int] = None
    horario: Optional[str] = None

#ESTUDIANTES

#Atributos base de los estudiantes
class EstudianteBase(BaseModel):
    cedula: int
    nombre: str
    email: str
    semestre: int

#crea un estudiantes
class CrearEstudiante(EstudianteBase):
    pass

#Muestra estudiante y cursos matriculados
class InfoEstudiante(EstudianteBase):
    id: int
    cursos: List[Curso] = [] #Realacion N:M

#Actualiza la informacion de los estudiantes
class ActualizarEstudiante(EstudianteBase):
    cedula: Optional[int] = None
    nombre: Optional[str] = None
    email: Optional[str] = None
    semestre: Optional[str] = None



