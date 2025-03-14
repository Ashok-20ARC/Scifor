from django.urls import path
from .views import home,movie_detail

urlpatterns=[
    path('',home,name='home'),
    path('movie/<int:movie_id>/',movie_detail,name='movie_detail'),
]