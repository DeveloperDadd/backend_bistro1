from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('menu/', views.show_menu, name='show_menu')
]