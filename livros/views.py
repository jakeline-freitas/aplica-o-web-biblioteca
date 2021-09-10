from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Livro


####### Create #########
class CriarLivro(CreateView):
    models = Livro


####### Read #########
class ListaLivro(ListView):
    models = Livro

    def get_queryset(self):
        queryset = Livro.objects.all()
        return queryset


####### Update #########
class EditarLivro(UpdateView):
    models = Livro


####### Delete #########
class DeleteLivro(DeleteView):
    models = Livro
