from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from .models import Livro


####### Create #########
class CriarLivro(CreateView):
    models = Livro
    fields = '__all__'
    template_name = 'livros/livro_create.html'
    success_url = reverse_lazy('livros:listar')

    def get_queryset(self):
        return Livro.objects.all()



####### Read #########
class ListaLivro(ListView):
    models = Livro
    template_name = 'livros/livro_list.html'
    

    def get_queryset(self):
        queryset = Livro.objects.all()
        return queryset


####### Update #########
class EditarLivro(UpdateView):
    models = Livro
    fields = '__all__'
    template_name = 'livros/livro_create.html'
    success_url = reverse_lazy('livros:listar')

    def get_queryset(self):
        return Livro.objects.all()


####### Delete #########
class DeleteLivro(DeleteView):
    models = Livro
    template_name ='livros/livro_delete.html'
    success_url = reverse_lazy('livros:listar')

    def get_queryset(self):
        queryset = Livro.objects.all()
        return queryset

