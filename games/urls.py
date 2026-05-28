from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('games/', views.games, name='games'),
    path('games/<int:game_id>/', views.game_detail, name='game_detail'),
]