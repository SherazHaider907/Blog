from django.urls import path
from . import views

urlpatterns = [
    # Dashboard URLs can be added here
    path('', views.dashboard, name='dashboard'),
    # Catagory CRUD URLs
    path('catagories/', views.catagories, name='catagories'),
    path('catagories/add/', views.add_catagory, name='add_catagory'),
    path('catagories/edit/<int:pk>/', views.edit_catagory, name='edit_catagory'),
    path('catagories/delete/<int:pk>/', views.delete_catagory, name='delete_catagory'),
    # Blog post CRUD URLs
    path('posts/', views.posts, name='posts'),
    path('posts/add/', views.add_post, name='add_post'),
    path('posts/edit/<int:pk>/', views.edit_post, name='edit_post'),
    path('posts/delete/<int:pk>/', views.delete_post, name='delete_post'),
]