from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('api/get-all-posts/', views.get_all_posts),
    path('api/create-post/', views.create_post),
    path('api/delete-post/', views.delete_post),
    path('api/get-post/', views.get_post_by_id),
]