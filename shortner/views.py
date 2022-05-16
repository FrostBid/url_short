from base64 import urlsafe_b64decode
from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html') #uses index.html as the home page

def create(request):
    if request.method == 'POST':
        link = request.POST['link'] #get what the user's link and store it as URL.
        uid = str(uuid.uuid4())[:5] #limits the UUID into 5 chara.
        new_url = Url(link=link, uuid=uid)
        new_url.save()
        return HttpResponse(uid)

def go(request,pk):
    url_details = Url.objects.get(uuid=pk) #get the id as pk
    return redirect(url_details.link) #as a link is assigned to it then redirects the user to the link