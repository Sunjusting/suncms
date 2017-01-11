from django import forms
 
class loginForm(forms.Form):
	username = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

class registerForm(forms.Form):
	username = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','id':'inputEmail'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','id':'inputPassword'}))
	confirmPassword = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','id':'confirmPassword'}))
	nickname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	sex = forms.ChoiceField(choices=((u'1',u'男'),( u'0',u'女' ),), widget=forms.RadioSelect(attrs={'class':'form-control'}))
	agency = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
