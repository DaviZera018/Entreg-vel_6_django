from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),          # Rota para o painel de administração
    path('', include('hello.urls')),         # Inclui as rotas do app "hello"
]
