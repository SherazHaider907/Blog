from django import forms

from blogs.models import Blog, Catagory
from django.contrib.auth.forms import UserChangeForm

from django.contrib.auth.models import User

class CatagoryForm(forms.ModelForm):
    class Meta:
        model = Catagory
        fields = '__all__'

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'catagory', 'featured_image', 'short_description', 'blog_body', 'status', 'is_featured']


class AddUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser','groups','user_permissions']
    
class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser','groups','user_permissions']