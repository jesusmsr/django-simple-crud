from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('api/get-all-posts/', views.get_all_posts)
]