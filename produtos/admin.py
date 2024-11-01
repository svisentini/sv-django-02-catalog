from django.contrib import admin
from .models import Categoria, Acabamento, Produto

admin.site.register(Categoria)
admin.site.register(Acabamento)
admin.site.register(Produto)