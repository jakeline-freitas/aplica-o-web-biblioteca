from django.urls import path
from .views import CriarLivro, EditarLivro, ListaLivro, DeleteLivro

app_name = "livros"

urlpatterns = [
    path("", ListaLivro.as_view(), name="listar"),
    path("cadastrarLivro/", CriarLivro.as_view(), name="criar"),
    path("editarLivro/<int:pk>/", EditarLivro.as_view(), name="editar"),
    path("deletarLivro/<int:pk>/", DeleteLivro.as_view(), name="deletar")

]
