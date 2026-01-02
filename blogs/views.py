from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Blog,Catagory
# Create your views here.
def posts_by_catagory(request, catagory_id):
    # Fetch the posts that belongs to the category with id category_id  
    posts = Blog.objects.filter(catagory=catagory_id, status='published')
    # Use try/except to handle the case where the category does not exist
    # try:
    #     catagory = Catagory.objects.get(pk=catagory_id)
    # except:
    #     return redirect('home')
    
    # use get_object_or_404 if needed when you want to show the 404 error in the page if the category is not found
    # catagories = Catagory.objects.all()
    catagory = get_object_or_404(Catagory, pk=catagory_id)
    context = {
        "posts": posts,
        "catagory": catagory,  # selected category
        # "catagories": catagories,  # list for navigation
    }
    return render(request, "posts_by_catagory.html", context)