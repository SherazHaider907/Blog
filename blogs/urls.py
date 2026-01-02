from django.urls import path

from . import views

urlpatterns = [
    path('<int:catagory_id>/', views.posts_by_catagory, name='posts_by_catagory'),
]
