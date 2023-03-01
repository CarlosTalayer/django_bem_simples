"""Configuração de URL do meuprojeto

A lista `urlpatterns` roteia URLs para visualizações. Para mais informações consulte:
     https://docs.djangoproject.com/en/2.2/topics/http/urls/
Exemplos:
Visualizações de funções
     1. Adicione uma importação: das exibições de importação my_app
     2. Adicione um URL a urlpatterns: path('', views.home, name='home')
Visualizações baseadas em classe
     1. Adicione uma importação: from other_app.views import Home
     2. Adicione um URL a urlpatterns: path('', Home.as_view(), name='home')
Incluindo outro URLconf
     1. Importe a função include(): from django.urls import include, path
     2. Adicione um URL a urlpatterns: path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myproject.core.views import index


urlpatterns = [
    path('admin/', index, name='index'),
    path('admin/', admin.site.urls),
]
