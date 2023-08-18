from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from fastapi.openapi.utils import get_openapi
from models import Curso
from models import Aluno
from database import engine, Base, get_db
from repositories import CursoRepository
from repositories import AlunoRepository
from schemas import CursoRequest, CursoResponse
from schemas import AlunoRequest, AlunoResponse
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/api/cursos", response_model=CursoResponse, status_code=status.HTTP_201_CREATED)
def create(request: CursoRequest, db: Session = Depends(get_db)):
    curso = CursoRepository.save(db, Curso(**request.dict()))
    return CursoResponse.from_orm(curso)

@app.get("/api/cursos", response_model=list[CursoResponse])
def find_all(db: Session = Depends(get_db)):
    cursos = CursoRepository.find_all(db)
    return [CursoResponse.from_orm(curso) for curso in cursos]

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Ambiente Virtual de Aprendizagem",
        version="1.0.0",
        summary="Alunos EAD",
        description="Sistema de Ambiente Virtual de Aprendizagem para auxiliar alunos 100% EAD",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

@app.get("/api/cursos/{curso_id}", response_model=CursoResponse)
def find_curso(curso_id: int, db: Session = Depends(get_db)):
    curso = CursoRepository.find_by_id(db, curso_id)
    if not curso:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    return CursoResponse.from_orm(curso)

@app.delete("/api/cursos/{curso_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_curso(curso_id: int, db: Session = Depends(get_db)):
    curso = CursoRepository.find_by_id(db, curso_id)
    if not curso:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    CursoRepository.delete(db, curso)

@app.put("/api/cursos/{curso_id}", response_model=CursoResponse)
def update_curso(curso_id: int, request: CursoRequest, db: Session = Depends(get_db)):
    curso = CursoRepository.find_by_id(db, curso_id)
    if not curso:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    
    for attr, value in request.dict().items():
        setattr(curso, attr, value)
    
    db.commit()
    db.refresh(curso)
    return CursoResponse.from_orm(curso)

from fastapi import HTTPException

@app.post("/api/alunos", response_model=AlunoResponse, status_code=status.HTTP_201_CREATED)
def create_aluno(request: AlunoRequest, db: Session = Depends(get_db)):
    aluno = AlunoRepository.save(db, Aluno(**request.dict()))
    return AlunoResponse.from_orm(aluno)

@app.get("/api/alunos/{aluno_id}", response_model=AlunoResponse)
def find_aluno(aluno_id: int, db: Session = Depends(get_db)):
    aluno = AlunoRepository.find_by_id(db, aluno_id)
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return AlunoResponse.from_orm(aluno)

@app.put("/api/alunos/{aluno_id}", response_model=AlunoResponse)
def update_aluno(aluno_id: int, request: AlunoRequest, db: Session = Depends(get_db)):
    aluno = AlunoRepository.find_by_id(db, aluno_id)
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")

    for attr, value in request.dict().items():
        setattr(aluno, attr, value)

    db.commit()
    db.refresh(aluno)
    return AlunoResponse.from_orm(aluno)

@app.delete("/api/alunos/{aluno_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_aluno(aluno_id: int, db: Session = Depends(get_db)):
    aluno = AlunoRepository.find_by_id(db, aluno_id)
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")

    curso_associado = CursoRepository.find_by_id(db, aluno.id_curso)
    if curso_associado and curso_associado.active:
        raise HTTPException(status_code=400, detail="Não foi possível excluir o aluno, pois ele está vinculado a um curso ativo")

    AlunoRepository.delete(db, aluno)


app.openapi = custom_openapi
