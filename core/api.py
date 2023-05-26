from typing import List
from django.shortcuts import get_object_or_404
from ninja import Router, Schema
from ninja.orm import create_schema


from emprestimo.api import EmprestimoSchema
from .models import Usuario

router = Router()

UsuarioSchema = create_schema(Usuario)

class UsuarioSchemaEntrada(Schema):
    id: int
    nome: str
    nascimento: str
    cpf: str
    email: str

    class Meta:
        model: Usuario
        fields= '__all__'

@router.get("/usuarios", response=List[UsuarioSchema])
def list_usuarios(request):
    list_query_usuarios = Usuario.objects.all()
    return list_query_usuarios

@router.get("/usuario/{id}", response=UsuarioSchema)
def get_usuario(request, id: int):
    get_query_usuario = get_object_or_404(Usuario, id=id)
    return get_query_usuario

@router.post("/usuario/{id}", response={201: UsuarioSchema})
def create_usuario(request, playload: UsuarioSchemaEntrada):
    post_query_usuario = Usuario.objects.create(**playload.dict())
    return 201, post_query_usuario

#Put:
@router.put("/usuario/{id}", response=UsuarioSchema)
def edit_usuario(request, id: int, playload: UsuarioSchemaEntrada):
    put_query_usuario = get_object_or_404(Usuario, id=id)
    for atr, valor in playload.dict().items():
        setattr(put_query_usuario, atr, valor)
    put_query_usuario.save()
    return put_query_usuario

#Del:
@router.delete("/usuario/{id}", response={204: None})
def del_usuario(request, id: int):
    del_query_usuario = get_object_or_404(Usuario, id=id)
    del_query_usuario.delete()
    return del_query_usuario
