from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('compress/', views.compress_view, name='compress'),
    path('decompress/', views.decompress_view, name='decompress'),
]
