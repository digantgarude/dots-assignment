from django.urls import path, include
from . import views

urlpatterns = [
    path("player", views.create_player),
    path("player/<int:player_id>", views.player_details),
    path("leaderboards", views.leaderboards),
]