from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('comments/', views.comments, name='comments'),
    path('details/', views.details, name='details'),
    path('poster/', views.poster, name='poster'),
    path('home/', views.home, name='home'),
    path('sell/', views.sell, name='sell'),
    path('list/', views.list, name='list'),
    path('team/', views.team, name='team'),
]