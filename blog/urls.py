from django.urls import path
from blog import views

#urls da aplicacao
urlpatterns = [
    path('', views.PostView.as_view(), name='home')     #pagina /home
]
