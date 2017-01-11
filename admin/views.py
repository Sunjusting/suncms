from django.http import HttpResponse,HttpResponseRedirect 
from django.template.response import TemplateResponse
from django.db import models
from auth.models import User, Agency,RbacRule,RbacRole,RbacRoleAccess
from .forms import AgencyForm,UserForm,EuserForm,RuleForm,RoleForm
from django.core.urlresolvers import reverse,resolve
from function.functions import get_tree
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .extpaginator import extpaginator
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from auth.rbac import rbac

# Create your views here.
def index(request):
	pageTitle = u'Dashboard'
	return TemplateResponse(request, 'admin/index.html',{'pageTitle':pageTitle})

def agencies(request):
	agencies = Agency.objects.all()
	q = []
	for n in agencies:
		q.append({'id':n.id,'pid':n.pid,'name':n.name,'phone':n.phone,'email':n.email,'status':n.status})

	return TemplateResponse(request, 'admin/agencies.html',{'agencies':get_tree(q)})

def addAgency(request,id):
	if request.method == "POST":
		form = AgencyForm(request.POST)
		if form.is_valid():
			try:
				form.save()
			except :
				return HttpResponse('Error')
		return HttpResponseRedirect(reverse('admin-agencies'))
	else:
		# return HttpResponse(id)
		if(id == 0):
			form = AgencyForm()
		else:
			form = AgencyForm({'pid':id})
	return TemplateResponse(request, 'admin/addAgency.html',{'form':form})

def editAgency(request,id):
	if request.method == "POST":
		a = Agency.objects.get(id=request.POST['id'])
		form = AgencyForm(request.POST,instance=a)		
		if form.is_valid():
			try:
				form.save()
			except :
				return HttpResponse('Error')
		return HttpResponseRedirect(reverse('admin-agencies'))
	else:
		agency = Agency.objects.get(id=id)
		form = AgencyForm(instance=agency)
		return TemplateResponse(request, 'admin/editAgency.html',{'form':form,'id':id})

def users(request):
	p = request.GET.get('p')
	k = request.GET.get('k')
	if p == None:
		p = 1
	if k == None:
		k = ''

	if k != '':
		users = User.objects.filter(Q(username__contains=k)|Q(nickname__contains=k))
	else:
		users = User.objects.all()
	paginator = extpaginator(users, 10)
	pagestr = paginator.pagestr(p,{'k':k})
	try:
		pusers = paginator.page(p)
	except PageNotAnInteger:
		pusers = paginator.page(1)
	except EmptyPage:
		pusers = paginator.page(paginator.num_pages)
	return TemplateResponse(request, 'admin/users.html',{'users':pusers, 'pagestr':pagestr})

def addUser(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			try:
				form.save()
			except :
				return HttpResponse('Error')
		return HttpResponseRedirect(reverse('admin-users'))
	else:
		form = UserForm()
	return TemplateResponse(request, 'admin/addUser.html',{'form':form})

def editUser(request,id):
	if request.method == "POST":
		a = User.objects.get(id=request.POST['id'])
		form = EuserForm(request.POST,instance=a)		
		if form.is_valid():
			try:
				form.save()
			except :
				return HttpResponse('Error')
		return HttpResponseRedirect(reverse('admin-users'))
	else:
		agency = User.objects.get(id=id)
		form = EuserForm(instance=agency)
		return TemplateResponse(request, 'admin/editUser.html',{'form':form,'id':id})

def setRole(request,id):
	if request.method == "POST":
		user_id = request.POST['id']
		RbacRoleAccess.objects.filter(user_id=user_id).delete()
		tlist = request.POST.getlist('roles')
		x = []
		for t in tlist:
			x.append(RbacRoleAccess(user_id=user_id,role_id=t))
		RbacRoleAccess.objects.bulk_create(x)		
		return HttpResponseRedirect(reverse('admin-set-role',args=[user_id]))
	else:
		rss = []
		roles = RbacRole.objects.all()
		rs = RbacRoleAccess.objects.filter(user_id=id)

		for r in rs:
			rss.append(r.role_id)

		for role in roles:
			if role.id in rss:
				role.checked = True
			else :
				role.checked = False
		return TemplateResponse(request,'admin/setRole.html',{'roles':roles,'id':id})

def rules(request):
	rules = RbacRule.objects.all()
	q = []
	for n in rules:
		q.append({'id':n.id,'pid':n.pid,'name':n.name,'title':n.title,'condition':n.condition,'status':n.status,'is_menu':n.is_menu})
	return TemplateResponse(request, 'admin/rules.html',{'rules':get_tree(q)})

def addRule(request,id):
	if request.method == "POST":
		form = RuleForm(request.POST)
		if form.is_valid():
			try:
				form.save()
			except :
				return HttpResponse('Error')
		return HttpResponseRedirect(reverse('admin-rules'))
	else:
		if(id == 0):
			form = RuleForm()
		else:
			form = RuleForm({'pid':id})
		return TemplateResponse(request, 'admin/addRule.html',{'form':form})

def editRule(request,id):
	if request.method == "POST":
		rule = RbacRule.objects.get(id=request.POST['id'])
		form = RuleForm(request.POST,instance=rule)		
		if form.is_valid():
			try:
				form.save()
			except :
				return HttpResponse('Error')
		return HttpResponseRedirect(reverse('admin-rules'))
	else:
		rule = RbacRule.objects.get(id=id)
		form = RuleForm(instance=rule)
		return TemplateResponse(request, 'admin/editRule.html',{'form':form,'id':id})

def roles(request):
	roles = RbacRole.objects.all();
	return TemplateResponse(request,'admin/roles.html',{'roles':roles})

def addRole(request):
	if request.method == "POST":
		form = RoleForm(request.POST)
		if form.is_valid():
			try:
				form.save()
			except :
				return HttpResponse('Error')
		return HttpResponseRedirect(reverse('admin-roles'))
	else:
		form = RoleForm()		
		return TemplateResponse(request, 'admin/addRole.html',{'form':form})

def editRole(request,id):
	if request.method == "POST":
		role = RbacRole.objects.get(id=request.POST['id'])
		form = RoleForm(request.POST,instance=role)		
		if form.is_valid():
			try:
				form.save()
			except :
				return HttpResponse('Error')
		return HttpResponseRedirect(reverse('admin-roles'))
	else:
		role = RbacRole.objects.get(id=id)
		form = RoleForm(instance=role)
		return TemplateResponse(request, 'admin/editRole.html',{'form':form,'id':id})
	
def access(request,id):

	if request.method == 'POST':
		role_id = request.POST['id']
		role = RbacRole.objects.get(id=request.POST['id'])

		access = request.POST.getlist('access')
		rules = ','.join(access)
		role.rules = rules
		role.save()
		return HttpResponseRedirect(reverse('admin-access',args=[role_id]))
	else:
		rules = RbacRule.objects.all()
		rs = RbacRole.objects.get(id=id)
				
		q = []
		for n in rules:
			if str(n.id) in rs.rules:
				q.append({'id':n.id,'pid':n.pid,'name':n.name,'title':n.title,'condition':n.condition,'status':n.status,'is_menu':n.is_menu,'checked':'1'})
			else:
				q.append({'id':n.id,'pid':n.pid,'name':n.name,'title':n.title,'condition':n.condition,'status':n.status,'is_menu':n.is_menu,'checked':'0'})
		return TemplateResponse(request, 'admin/access.html',{'rules':get_tree(q),'id':id,'roleName':rs.name})
		# return HttpResponse(get_tree(q))


def test(request):
	current_url = resolve(request.path_info).url_name
	return HttpResponse(current_url)

def test2(request):
	roles = RbacRoleAccess.objects.filter(user_id=6)
	rlist = []
	for r in roles:
		rlist.extend(r.role.rules+',')

	new_ids = []
	for r in rlist:
		if r not in new_ids:
			new_ids.append(r)

	return HttpResponse(new_ids)

def test3(request,id):
	rb = rbac()
	rules = rb.getRbacList(id)
	return HttpResponse(rules)

def testCheck(request,name):
	r = rbac()
	user_id = request.session['user_id']
	# x = r.check(name,user_id)
	rss = r.getRbacList(request,user_id)
	return HttpResponse(request.session['rbac'])
	# if r.check(name,user_id):
	# 	return HttpResponse('Yes, You have the access to ->'+name)
	# else:
	# 	return HttpResponse('No, You dont have the access to ->'+name)
