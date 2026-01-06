from django import forms

from blogs.models import Blog, Catagory

class CatagoryForm(forms.ModelForm):
    class Meta:
        model = Catagory
        fields = '__all__'

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'catagory', 'featured_image', 'short_description', 'blog_body', 'status', 'is_featured']