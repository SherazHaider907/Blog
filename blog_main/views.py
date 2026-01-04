from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm
from blogs.models import Blog, Catagory
from assignment.models import About
from django.contrib import auth
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

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
            print(form.errors)
    else:
        form = RegistrationForm()
    context = {
        "form": form,
        }
    return render(request, "register.html", context)

# create login view
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
    form = AuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, "login.html", context)

# create logout view
def logout(request):
    auth.logout(request)
    return redirect('home')