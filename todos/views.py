from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy # Para usar o name das urls
from django.shortcuts import get_object_or_404, redirect
from .models import Todo

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View


# Create your views here.
def home(request):
    # return HttpResponse("<h1>Ola Treinaweb !</h1>")
    return render(request, "todos/home.html")


# >> Função foi substituida pela classe TodoListView 

#def todo_list(request):
#    todos = Todo.objects.all()
#    return render(request, "todos/todo_list.html", {
#        "todos": todos
#    })


class TodoListView(ListView):
    model = Todo

class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("url_todo_list")

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("url_todo_list")

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("url_todo_list")

class TodoCompleteView(View):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.concluirTarefa()
        return redirect("url_todo_list")

