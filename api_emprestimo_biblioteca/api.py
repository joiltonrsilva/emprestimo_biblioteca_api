from ninja import NinjaAPI

from emprestimo.api import router as emprestimo_router
from core.api import router as core_router

api = NinjaAPI()

api.add_router("/core/", core_router)
api.add_router("/api_emprestimo/", emprestimo_router)