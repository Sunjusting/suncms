#coding:utf-8
from django.http import HttpResponse,HttpResponseRedirect 
from django.contrib import messages
from django.shortcuts import render
from .forms import registerForm,loginForm
from .models import User
from django.contrib.auth.hashers import make_password,check_password
from django.core.urlresolvers import reverse
from auth.rbac import rbac
import traceback

import time

# Create your views here.
def login(request):
	if request.method == 'POST':
		form = loginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			try:
				user = User.objects.get(username=username,status=1)
			except:
				messages.warning(request, '用户名不存在或者被禁用')
				return render(request, 'auth/login.html',{'form':form})

			if check_password(password+username,user.password):
				user.last_login_time = time.strftime('%Y-%m-%d %H:%M:%S')
				user.save()
				request.session['user_id'] = user.id
				request.session['username'] = user.username
				if 'rbac' in request.session:
					del request.session['rbac']
				rbac().getRbacList(request,user.id)
				return HttpResponseRedirect(reverse('admin-index'))
			else:
				messages.warning(request, ' 请输入正确的用户名和密码')
				return render(request, 'auth/login.html',{'form':form})
			
	else:
		form = loginForm()

	return render(request, 'auth/login.html',{'form':form})

def logout(request):
	try:
		del request.session['user_id']
		del request.session['username']
		del request.session['rbac']
	except:
		pass
	return HttpResponseRedirect(reverse('login'))

def register(request):
	if request.method == 'POST':
		form = registerForm(request.POST)
		if form.is_valid():
			data = {
				'username' : form.cleaned_data['username'],
				'password' : make_password(form.cleaned_data['password']+form.cleaned_data['username'],None,'pbkdf2_sha256'),
				'nickname' : form.cleaned_data['nickname'],
				'sex' : form.cleaned_data['sex'],
				'phone' : form.cleaned_data['phone'],
				'address' : form.cleaned_data['address'],
			}
			try:
				user = User.objects.create(**data)
			except:
				# return HttpResponse('注册失败')		
				traceback.print_exc()

			return HttpResponse(u'注册成功')
	else:
		form = registerForm()

	return render(request, 'auth/register.html',{'form':form})

def checkUser(request):
	if request.method == 'GET':
		username = request.GET['username']
		try:
			User.objects.get(username=username)
		except:
			return HttpResponse("False")
		return HttpResponse(True)
		
def test(request):
	return HttpResponse('hi')
	