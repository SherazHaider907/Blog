from django.shortcuts import get_object_or_404, redirect, render
from .forms import BlogPostForm, CatagoryForm
from blogs.models import Blog, Catagory
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    catagory_count = Catagory.objects.all().count()
    blogs_count = Blog.objects.all().count()
    context = {
        "catagory_count": catagory_count,
        "blogs_count": blogs_count,
    }
    return render(request, "dashboard/dashboard.html", context)

def catagories(request):
    catagories = Catagory.objects.all()
    context = {
        "catagories": catagories,
    }
    return render(request, "dashboard/catagories.html", context)

# Catagory CRUD views
def add_catagory(request):
    if request.method == "POST":
        form = CatagoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catagories')
    form = CatagoryForm()
    context = {
        "form": form,
    }
    return render(request, "dashboard/add_catagory.html", context)

def edit_catagory(request, pk):
    catagory = get_object_or_404(Catagory, pk=pk)
    if request.method == "POST":
        form = CatagoryForm(request.POST, instance=catagory)
        if form.is_valid():
            form.save()
            return redirect('catagories')
    form = CatagoryForm(instance=catagory)
    context = {
        "form": form,
        "catagory": catagory,
    }
    return render(request, "dashboard/edit_catagory.html",context)

def delete_catagory(request, pk):
    catagory = get_object_or_404(Catagory, pk=pk)
    catagory.delete()
    return redirect('catagories')


# Blog post CRUD views

def posts(request):
    posts = Blog.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, "dashboard/posts.html", context)


# def add_post(request):
#     if request.method == "POST":
#         form = BlogPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             title = form.cleaned_data['title']
#             post.slug = slugify(title) + "-" + str(post.id)
#             post.save()
#             return redirect('posts')
#         else:
#             print(form.errors)
#     # Placeholder for adding a new blog post
#     form = BlogPostForm()
#     context = {
#         "form": form,
#     }
#     return render(request, "dashboard/add_post.html", context)

def add_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user

            # TEMP slug to avoid UNIQUE constraint error
            post.slug = "temp"
            post.save()

            # Create final unique slug
            title = form.cleaned_data['title']
            post.slug = slugify(title) + "-" + str(post.id)
            post.save(update_fields=['slug'])

            return redirect('posts')
        else:
            print(form.errors)

    # keep your context pattern
    form = BlogPostForm()
    context = {
        "form": form,
    }
    return render(request, "dashboard/add_post.html", context)


def edit_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            post.slug = slugify(post.title) + "-" + str(post.id)
            post.save(update_fields=['slug'])
            return redirect('posts')
    form = BlogPostForm(instance=post)
    context = {
        "form": form,
        "post": post,
    }
    return render(request, "dashboard/edit_post.html",context)

def delete_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.delete()
    return redirect('posts')