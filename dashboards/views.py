from django.shortcuts import get_object_or_404, redirect, render
from .forms import CatagoryForm
from blogs.models import Blog, Catagory
from django.contrib.auth.decorators import login_required
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