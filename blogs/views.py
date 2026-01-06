from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Blog,Catagory,Comment
from django.db.models import Q
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

def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='published')
    if request.method == "POST":
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)
    # commits
    comments = Comment.objects.filter(blog=single_blog)
    comment_count = comments.count()

    context = {
        "single_blog": single_blog,
        "comments":comments,
        "comment_count":comment_count,
    }
    return render(request, "blog.html", context)

def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='published')
    context = {
        "blogs": blogs,
        "keyword": keyword,
    }
    return render(request, "search.html",context)