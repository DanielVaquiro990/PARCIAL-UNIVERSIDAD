from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from database import Base, engine, SessionLocal
import models, schemas

#Inicia la base de datos y API
Base.metadata.create_all(bind=engine)
app = FastAPI(title="Sistema de gestion de cursos y estudiantes", version="1.0")


# Dependencia para obtener sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



# ENDPOINTS PARA ESTUDIANTES

#CREA UN ESTUDIANTE
@app.post("/estudiantes/", response_model=schemas.EstudianteBase)
def crear_estudiante(estudiante: schemas.CrearEstudiante, db: Session = Depends(get_db)):
    nuevo = models.Estudiante(**estudiante.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

#Lista todos los estudiantes. Filtro por semestre
@app.get("/estudiantes/", response_model=list[schemas.EstudianteBase])
def listar_estudiantes(semestre: int | None = None, db: Session = Depends(get_db)):
    query = db.query(models.Estudiante)
    if semestre:
        query = query.filter(models.Estudiante.semestre == semestre)
    return query.all()


@app.get("/estudiantes/{estudiante_id}", response_model=schemas.EstudianteBase)
def obtener_estudiante(estudiante_id: int, db: Session = Depends(get_db)):
    estudiante = db.query(models.Estudiante).filter(models.Estudiante.id == estudiante_id).first()
    if not estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return estudiante


#ACTUALIZAR DATOS ESTUDIANTE
@app.put("/estudiantes/{estudiante_id}", response_model=schemas.EstudianteBase)
def actualizar_estudiante(estudiante_id: int, datos: schemas.ActualizarEstudiante, db: Session = Depends(get_db)):
    estudiante = db.query(models.Estudiante).filter(models.Estudiante.id == estudiante_id).first()
    if not estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")

    for key, value in datos.model_dump(exclude_unset=True).items():
        setattr(estudiante, key, value)

    db.commit()
    db.refresh(estudiante)
    return estudiante

#ELIMINACION ESTUDIANTE
@app.delete("/estudiantes/{estudiante_id}")
def eliminar_estudiante(estudiante_id: int, db: Session = Depends(get_db)):
    estudiante = db.query(models.Estudiante).filter(models.Estudiante.id == estudiante_id).first()
    if not estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    db.delete(estudiante)
    db.commit()
    return {"mensaje": "Estudiante eliminado correctamente"}


# ----------------------------------------------------------
# ENDPOINTS PARA CURSOS
# ----------------------------------------------------------

#CREA CURSO
@app.post("/cursos/", response_model=schemas.Curso)
def crear_curso(curso: schemas.CrearCurso, db: Session = Depends(get_db)):
    nuevo = models.Curso(**curso.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

#Lista cursos con filtro: creditos o codigo.

@app.get("/cursos/", response_model=list[schemas.Curso])
def listar_cursos(creditos: int | None = None, codigo: str | None = None, db: Session = Depends(get_db)):
    query = db.query(models.Curso)
    if creditos:
        query = query.filter(models.Curso.creditos == creditos)
    if codigo:
        query = query.filter(models.Curso.codigo == codigo)
    return query.all()


@app.get("/cursos/{curso_id}", response_model=schemas.Curso)
def obtener_curso(curso_id: int, db: Session = Depends(get_db)):
    curso = db.query(models.Curso).filter(models.Curso.id == curso_id).first()
    if not curso:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    return curso

#ACTUALIZA EL CURSO
@app.put("/cursos/{curso_id}", response_model=schemas.Curso)
def actualizar_curso(curso_id: int, datos: schemas.ActualizarCurso, db: Session = Depends(get_db)):
    curso = db.query(models.Curso).filter(models.Curso.id == curso_id).first()
    if not curso:
        raise HTTPException(status_code=404, detail="Curso no encontrado")

    for key, value in datos.model_dump(exclude_unset=True).items():
        setattr(curso, key, value)

    db.commit()
    db.refresh(curso)
    return curso

#ELIMINA UN CURSO
@app.delete("/cursos/{curso_id}")
def eliminar_curso(curso_id: int, db: Session = Depends(get_db)):
    curso = db.query(models.Curso).filter(models.Curso.id == curso_id).first()
    if not curso:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    db.delete(curso)
    db.commit()
    return {"mensaje": "Curso eliminado correctamente"}


# ----------------------------------------------------------
# ENDPOINTS PARA MATRÍCULAS


#Matricula un estudiante en un curso.
@app.post("/matriculas/")
def matricular_estudiante(matricula: schemas.CrearMatricula, db: Session = Depends(get_db)):
    estudiante = db.query(models.Estudiante).filter(models.Estudiante.id == matricula.estudiante_id).first()
    curso = db.query(models.Curso).filter(models.Curso.id == matricula.curso_id).first()

    if not estudiante or not curso:
        raise HTTPException(status_code=404, detail="Estudiante o curso no encontrado")

    estudiante.cursos.append(curso)
    db.commit()
    return {"mensaje": f"El estudiante {estudiante.nombre} fue matriculado en {curso.nombre}"}

#Desmatricula un estudiante de un curso.
@app.delete("/matriculas/")
def desmatricular_estudiante(matricula: schemas.MatriculaBase, db: Session = Depends(get_db)):
    estudiante = db.query(models.Estudiante).filter(models.Estudiante.id == matricula.estudiante_id).first()
    curso = db.query(models.Curso).filter(models.Curso.id == matricula.curso_id).first()

    if not estudiante or not curso:
        raise HTTPException(status_code=404, detail="Estudiante o curso no encontrado")

    if curso in estudiante.cursos:
        estudiante.cursos.remove(curso)
        db.commit()
        return {"mensaje": f"El estudiante {estudiante.nombre} fue desmatriculado de {curso.nombre}"}
    else:
        raise HTTPException(status_code=400, detail="El estudiante no estaba matriculado en ese curso")


#Muestra todos los cursos en los que está matriculado un estudiante.
@app.get("/estudiantes/{estudiante_id}/cursos", response_model=List[schemas.CursoBase])
def cursos_de_estudiante(estudiante_id: int, db: Session = Depends(get_db)):
    estudiante = db.query(models.Estudiante).filter(models.Estudiante.id == estudiante_id).first()
    if not estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return estudiante.cursos



#    Muestra todos los estudiantes matriculados en un curso.
@app.get("/cursos/{curso_id}/estudiantes", response_model=List[schemas.EstudianteBase])
def estudiantes_de_curso(curso_id: int, db: Session = Depends(get_db)):
    curso = db.query(models.Curso).filter(models.Curso.id == curso_id).first()
    if not curso:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    return curso.estudiantes