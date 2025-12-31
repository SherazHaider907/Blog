from django.contrib import admin
from .models import Blog, Catagory

# Register your models here.

# Slug Prepopulate in admin panel
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'catagory','author', 'status', 'is_featured', 'created_at')
    search_fields = ('id','title', 'catagory__catagory_name', 'status')
    list_editable = ('status', 'is_featured')

admin.site.register(Catagory)
admin.site.register(Blog, BlogAdmin)