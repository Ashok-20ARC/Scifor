from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("upload/", views.upload_song, name="upload"),
    path("playlist/", views.playlist, name="playlist"),
    path('now_playing/', views.now_playing, name='now_playing'),  
    path("now_playing/<int:song_id>/", views.now_playing, name="now_playing_with_id"),
    path('delete/<int:song_id>/', views.delete_song, name='delete_song'),
]
