from typing import List
from django.shortcuts import get_object_or_404
from ninja import Router, Schema
from ninja.orm import create_schema

from .models import Livro, Emprestimo

router = Router()


#Get:
LivroSchema = create_schema(Livro)

@router.get("/livros", response=List[LivroSchema])
def list_livros(request):
    list_query_livros = Livro.objects.all()
    return list_query_livros

@router.get("/livros/{id}", response=LivroSchema)
def get_livro(request, id: int):
    get_query_livro = get_object_or_404(Livro, id=id)
    return get_query_livro

#Post:
class LivroSchemaEntrada(Schema):
    titulo: str
    autor: str
    ano_publicacao: int
    editora: str


@router.post("/livros/{id}", response={201: LivroSchema})
def create_livro(request, playload: LivroSchemaEntrada):
    post_query_livro = Livro.objects.create(**playload.dict())
    return 201, post_query_livro

#Put:
@router.put("/livros/{id}", response=LivroSchema)
def edit_livro(request, id: int, playload: LivroSchemaEntrada):
    put_query_livro = get_object_or_404(Livro, id=id)
    for atr, valor in playload.dict().items():
        setattr(put_query_livro, atr, valor)
    put_query_livro.save()
    return put_query_livro

#Del:
@router.delete("/livros/{id}", response={204: None})
def del_livro(request, id: int):
    del_query_livro = get_object_or_404(Livro, id=id)
    del_query_livro.delete()
    return del_query_livro

#Get:
EmprestimoSchema = create_schema(Emprestimo)

@router.get("/emprestimos", response=List[EmprestimoSchema])
def list_emprestimos(request):
    list_query_emprestimos = Emprestimo.objects.all()
    return list_query_emprestimos

@router.get("/emprestimo/{id}", response=EmprestimoSchema)
def get_emprestimo(request, id: int):
    get_query_emprestimo = get_object_or_404(Emprestimo, id=id)
    return get_query_emprestimo

#Post:
class EmprestimoSchemaEntrada(Schema):
    livro_id: int
    usuario_id: int
    data_emprestimo: str
    data_devolucao: str

@router.post("/emprestimo/{id}", response={201: EmprestimoSchema})
def create_emprestimo(request, playload: EmprestimoSchemaEntrada):
    livro_id = playload.livro_id
    usuario_id = playload.usuario_id
    data_emprestimo = playload.data_emprestimo
    data_devolucao = playload.data_devolucao

    livro = get_object_or_404(Livro, id=livro_id)
    usuario = get_object_or_404(Usuario, id=usuario_id)

    data = dict(
        livro_id = livro,
        usuario_id = usuario,
        data_emprestimo = data_emprestimo,
        data_devolucao = playload.data_devolucao,
    )

    post_query_livro = Livro.objects.create(**data)
    return 201, post_query_livro

#Put:
@router.put("/emprestimo/{id}", response=EmprestimoSchema)
def edit_emprestimo(request, id: int, playload: EmprestimoSchemaEntrada):
    put_query_livro = get_object_or_404(Emprestimo, id=id)
    for atr, valor in playload.dict().items():
        setattr(put_query_livro, atr, valor)
    put_query_emprestimo.save()
    return put_query_emprestimo

#Del:
@router.delete("/emprestimo/{id}", response={204: None})
def del_emprestimo(request, id: int):
    del_query_emprestimo = get_object_or_404(Emprestimo, id=id)
    del_query_emprestimo.delete()
    return del_query_emprestimo