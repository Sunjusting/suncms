from django import forms
from django.forms import ModelForm
from auth.models import Agency,User,RbacRule,RbacRole
from function.functions import create_tree,get_tree
from django.contrib.auth.hashers import make_password

class AgencyForm(ModelForm):

	class Meta:
		model = Agency
		fields = ['id','pid','name','phone','email','address','website','remark']
	
	pid = forms.ChoiceField(label=u'上级机构',widget=forms.Select(attrs={'class':'form-control'}))

	def __init__(self,*args,**kwargs):
		super(self.__class__, self).__init__(*args,**kwargs)
		choices = create_tree(Agency.objects.values('id','pid','name'))
		choices.insert(0,('0',u'顶级机构'))
		self.fields['pid'].choices = choices

class UserForm(ModelForm):

	class Meta:
		model = User
		fields = ['id','agency_id','username','password','nickname','sex','phone','address']

	
	choices = [(1,u'男'),(0,u'女')]
	sex = forms.ChoiceField(label=u'性别',choices=choices,widget=forms.RadioSelect(attrs={'class':'form-control'}))
	agency_id = forms.ChoiceField(label=u'所属机构',widget=forms.Select(attrs={'class':'form-control'}))

	def __init__(self,*args,**kwargs):
		super(self.__class__, self).__init__(*args,**kwargs)
		choices = create_tree(Agency.objects.values('id','pid','name'))
		self.fields['agency_id'].choices = choices

	def clean_password(self):
		data = make_password(self.cleaned_data['password']+self.cleaned_data['username'],None,'pbkdf2_sha256')
		return data

class EuserForm(ModelForm):
	class Meta:
		model = User
		fields = ['id','agency_id','username','nickname','sex','phone','address']
	
	choices = [(1,u'男'),(0,u'女')]
	sex = forms.ChoiceField(label=u'性别',choices=choices,widget=forms.RadioSelect(attrs={'class':'form-control'}))
	agency_id = forms.ChoiceField(label=u'所属机构',widget=forms.Select(attrs={'class':'form-control'}))

	def __init__(self,*args,**kwargs):
		super(self.__class__, self).__init__(*args,**kwargs)
		choices = create_tree(Agency.objects.values('id','pid','name'))
		self.fields['agency_id'].choices = choices

class RuleForm(ModelForm):
	class Meta:
		model = RbacRule
		fields = ['id','pid','name','title','condition','is_menu']

	pid = forms.ChoiceField(label=u'上级权限',widget=forms.Select(attrs={'class':'form-control'}))

	def __init__(self,*args,**kwargs):
		super(self.__class__, self).__init__(*args,**kwargs)
		choices = create_tree(RbacRule.objects.values('id','pid','name'))
		choices.insert(0,('0',u'顶级权限'))
		self.fields['pid'].choices = choices

class RoleForm(ModelForm):
	class Meta:
		model = RbacRole
		fields = ['id','name','remark']


