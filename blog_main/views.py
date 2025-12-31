from django.shortcuts import render


# create home view
def home(request):
    return render(request, "home.html")