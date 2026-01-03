from django.contrib import admin
from django.conf.urls.static import static 
from django.urls import include, path
from . import views
from django.conf import settings
from blogs import views as BlogViews
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path('category/',include('blogs.urls')),
    path('blogs/<slug:slug>/',BlogViews.blogs, name='blogs'),
    # search endpoint
    path('blogs/search/', BlogViews.search, name='search'),
    # register
    path('register/', views.register, name='register'),
    # login functionality
    path ('login/',views.login, name='login'),
    # logout functionality
    path('logout/', views.logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
