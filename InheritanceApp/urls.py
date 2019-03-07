from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('comments/', views.comments, name='comments'),
    path('details/', views.details, name='details'),
    path('poster/', views.poster, name='poster'),
]