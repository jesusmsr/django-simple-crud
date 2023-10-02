from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('api/get-all-posts/', views.get_all_posts),
    path('api/create-post/', views.create_post),
    path('api/delete-post/<int:post_id>', views.delete_post),
    path('api/get-post/<int:post_id>', views.get_post_by_id),
    path('api/update-post/<int:post_id>', views.update_post),
]