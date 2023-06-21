from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
def insert_Webpage(request):
    t=input('enter a topic_name:')
    n=input('Enter a name:')
    u=input('enter a url')
    O=Topic.objects.get_or_create(topic_name=t)[0]
    O.save()
    v=Webpage.objects.get_or_create(topic_name=O,name=n,url=u)[0]
    v.save()
    return HttpResponse('insert data is successful')
