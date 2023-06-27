from django.shortcuts import render
from django.http import HttpResponse

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

def update_webpages(request):
    CTO=Topic.objects.get(Topic_name='rugby')

    #WebPage.objects.filter(Name='dhoni').update( Url='https://msd.com')#single row
    #WebPage.objects.filter(Topic_name='cricket').update( Url='https://msd.com')#multiple row
    #WebPage.objects.filter(Name='Dhoni msd').update(Url='http://mmm.com')#no rows
    #WebPage.objects.filter(Name='dhoni').update(Topic_name='BCCI CRICKET')#foreign key error
    #WebPage.objects.filter(Name='dhoni').update(Topic_name='rugby')#existing values
    #WebPage.objects.update_or_create(Name='harshad',defaults={'Url':'http://team.in'})#Single row
    #WebPage.objects.update_or_create(Topic_name='cricket',defaults={'Url':'https://TeamIndia.com'})# multiple rows
    #WebPage.objects.update_or_create(Topic_name='BCCI',defaults={'Url':'http://bcci.in'})#No rows matching
    #WebPage.objects.update_or_create(Topic_name='football',defaults={'Name':'don'})
    WebPage.objects.update_or_create(Name='rani',defaults={'Topic_name':CTO})

    #WebPage.objects.update_or_create(Name='weird',defaults={'Url':'https://abc.com','Topic_name':CTO})
    #WebPage.objects.update_or_create(Name='crazy',defaults={'Url':'https://xyz.com','Topic_name':CTO})

    webpages=WebPage.objects.all()
    d={'webpages':webpages}
    return render(request,'display_webpages.html',d)


    