from .models import Catagory 
from assignment.models import SocialLink
def get_catagories(request):
    catagories = Catagory.objects.all()
    return dict(catagories=catagories)

def get_social_links(request):
    social_links = SocialLink.objects.all()
    return dict(social_links=social_links)