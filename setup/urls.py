

from django.contrib import admin
from django.urls import path
from todos.views import home
from todos.views import TodoListView, TodoCreateView, TodoUpdateView, TodoDeleteView, TodoCompleteView

from produtos.views import listar_produtos
from calculadora.views import calculaCustos

urlpatterns = [
    path("admin/", admin.site.urls), 
    path("", TodoListView.as_view(), name="url_todo_list"),
    path("create", TodoCreateView.as_view(), name="url_todo_create"),
    path("update/<int:pk>", TodoUpdateView.as_view(), name="url_todo_update"),
    path("delete/<int:pk>", TodoDeleteView.as_view(), name="url_todo_delete"),
    path("complete/<int:pk>", TodoCompleteView.as_view(), name="url_todo_complete"),

    path('produtos', listar_produtos, name='listar_produtos'),
    path('calculadora', calculaCustos, name='calcula_custos'),

]
