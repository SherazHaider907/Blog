from django.shortcuts import render
from blogs.models import Blog, Catagory
from assignment.models import About
# create home view
def home(request):
    # catagories = Catagory.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True,status='published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured = False, status='published')

    # fetch about us

    try:
        about = About.objects.get()
    except:
        about = None

    context = {
        # "catagories": catagories,
        "featured_post": featured_posts,
        "posts": posts,
        "about": about,
    }
    return render(request, "home.html", context)