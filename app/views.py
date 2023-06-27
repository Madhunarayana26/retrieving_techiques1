from django.shortcuts import render

# Create your views here.
from app.models import *

from django.db.models import Q

def display_topics(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    return render(request,'display_topics.html',d)

def display_webpages(request):
    webpages=WebPage.objects.all()
    #webpages=WebPage.objects.filter(Name__in=['rahul','Dhoni'])
    #webpages=WebPage.objects.filter(Name__regex='R\w+')
    #webpages=WebPage.objects.filter(Q(Name='Virat') | Q(url__startswith='https'))
    #webpages=WebPage.objects.filter(Q(Name='dhoni') & Q(url__startswith='https'))
    
    d={'webpages':webpages}
    return render(request,'display_webpages.html',d)


def display_accessrecords(request):
    LAO=AccessRecords.objects.all()

    #LAO=AccessRecords.objects.filter(Date__gt='1995-01-18')
    #LAO=AccessRecords.objects.filter(Date__lte='1995-01-18')
    #LAO=AccessRecords.objects.filter(Date__year='2021')
    #LAO=AccessRecords.objects.filter(Date__month='07')
    #LAO=AccessRecords.objects.filter(Date__day='3')
    #LAO=AccessRecords.objects.filter(Date__year__gte='2020')
    #LAO=AccessRecords.objects.filter(Date__year__lte='2020')
    #LAO=AccessRecords.objects.filter(Date__day__gt='1')
    #LAO=AccessRecords.objects.filter(Date='1995-12-12')

    
    

    
    
    

    
    
    
    d={'LAO':LAO}
    return render(request,'display_accessrecords.html',d)