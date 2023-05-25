from typing import List
from django.shortcuts import get_object_or_404
from ninja import Router
from ninja.orm import create_schema

from .models import Livro, Emprestimo

