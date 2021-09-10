from django.urls import path
from . import views

app_name = "livros"

urlpatterns = [
    path("", views.ListaLivro.as_view(), name="listar"),
    path("cadastrarLivro/", views.CriarLivro.as_view(), name="criar"),
    path("editarLivro/<int:pk>/", views.EditarLivro.as_view(), name="editar"),
    path("deletarLivro/<int:pk>/", views.DeleteLivro.as_view(), name="deletar")

]
