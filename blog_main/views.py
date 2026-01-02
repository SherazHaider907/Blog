from django.shortcuts import render
from blogs.models import Blog, Catagory

# create home view
def home(request):
    # catagories = Catagory.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True,status='published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured = False, status='published')
    context = {
        # "catagories": catagories,
        "featured_post": featured_posts,
        "posts": posts,
    }
    return render(request, "home.html", context)