from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect 
from django.template.response import TemplateResponse
from event.models import Event,Agenda
from django.core.urlresolvers import reverse,resolve
# Create your views here.

def index(request):
	events = Event.objects.all()
	return TemplateResponse(request,'front/index.html',{'event':events})

def show(request,id):
	event = Event.objects.get(id=id)
	return TemplateResponse(request,'front/show.html',{'event':event})
