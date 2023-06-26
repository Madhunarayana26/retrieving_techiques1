from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.


def display_topic(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    return render( request,'display_topic.html',d)

def display_webpage(request):
    webpages=WebPage.objects.all()
    d={'webpages':webpages}
    return render(request,'display_webpage.html',d)
def display_accessrecords(request):
    access=AccessRecords.objects.all()
    d={'access':access}
    return render(request,'display_accessrecords.html',d)