from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect 
from django.template.response import TemplateResponse
from event.models import Event,Agenda
from auth.models import User
from .forms import EventForm,AgendaForm
from admin.extpaginator import extpaginator
from django.core.urlresolvers import reverse,resolve
from PIL import Image

# Create your views here.

def index(request):
	p = request.GET.get('p')
	k = request.GET.get('k')
	if p == None:
		p = 1
	if k == None:
		k = ''

	if k != '':
		events = Event.objects.filter(name__contains=k)
	else:
		events = Event.objects.all()
	paginator = extpaginator(events, 10)
	pagestr = paginator.pagestr(p,{'k':k})
	try:
		pevents = paginator.page(p)
	except PageNotAnInteger:
		pevents = paginator.page(1)
	except EmptyPage:
		pevents = paginator.page(paginator.num_pages)
	return TemplateResponse(request, 'event/index.html',{'events':pevents, 'pagestr':pagestr})

def add(request):
	if request.method == "POST":
		form = EventForm(request.POST,request.FILES)
		if form.is_valid():
			newEvent = form.save(commit=False)
			newEvent.user = User.objects.get(id=request.session['user_id'])
			try:
				newEvent.save()
				return HttpResponse('Add Event Successfully!')
			except :
				return HttpResponse('Error')
	else:
		form = EventForm()
	return TemplateResponse(request, 'event/add.html',{'form':form})

def edit(request,id):
	if request.method == "POST":
		a = Event.objects.get(id=request.POST['id'])
		form = EventForm(request.POST,request.FILES,instance=a)		
		if form.is_valid():
			try:
				form.save()
			except :
				return HttpResponse('Error')
		return HttpResponseRedirect(reverse('event-index'))
	else:
		event = Event.objects.get(id=id)
		form = EventForm(instance=event)
		return TemplateResponse(request, 'event/edit.html',{'form':form,'id':id})

def show(request,id):
	event = Event.objects.get(id=id)
	return TemplateResponse(request, 'event/show.html',{'event':event})
	# return HttpResponse('show')

def agendas(request,id):
	agendas = Agenda.objects.filter(event__id=id)
	return TemplateResponse(request,'event/agendas.html',{'agendas':agendas,'event_id':id})

def addAgenda(request,event_id):
	if request.method == "POST":
		form = AgendaForm(request.POST)
		if form.is_valid():
			newAgenda = form.save(commit=False)
			newAgenda.event = Event.objects.get(id=event_id)
			try:
				newAgenda.save()
				return HttpResponse('Add Event Agenda Successfully!')
			except :
				return HttpResponse('Error')
	else:
		form = AgendaForm()
	return TemplateResponse(request, 'event/addAgenda.html',{'form':form})

def editAgenda(request,id):
	if request.method == "POST":
		agenda = Agenda.objects.get(id=request.POST['id'])
		form = AgendaForm(request.POST,instance=agenda)		
		if form.is_valid():
			try:
				form.save()
			except :
				return HttpResponse('Error')
		return HttpResponseRedirect(reverse('event-agendas',args=[agenda.event.id]))
	else:
		agenda = Agenda.objects.get(id=id)
		form = AgendaForm(instance=agenda)
		return TemplateResponse(request, 'event/editAgenda.html',{'form':form,'id':id})

def deleteAgenda(request,id):
	agenda = Agenda.objects.get(id=id)
	event_id = agenda.event.id
	agenda.delete()
	return HttpResponseRedirect(reverse('event-agendas',args=[event_id]))