from .models import Catagory 
def get_catagories(request):
    catagories = Catagory.objects.all()
    return dict(catagories=catagories)