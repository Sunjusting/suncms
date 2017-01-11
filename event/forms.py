from django import forms
from django.forms import ModelForm
from event.models import Event,City,Agenda

class EventForm(ModelForm):

	class Meta:
		model = Event
		fields = ['id','name','ename','hosts','organizer','contact','address','phone','email','website','venue','vaddress','start_at','end_at','intro','image','category','city']
	
	# user = forms.CharField(label='',widget=forms.HiddenInput())
	# image = forms.ImageField()


class AgendaForm(ModelForm):

	class Meta:
		model = Agenda
		fields = ['id','day','start_time','end_time','subject','place','sort','intro']

	
