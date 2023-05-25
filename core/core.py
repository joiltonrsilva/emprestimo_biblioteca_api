from typing import List
from django.contrib.auth.models import User
from ninja import Router, Schema

from api_emprestimo_biblioteca.emprestimo.api import TodoSchema

router = Router()


