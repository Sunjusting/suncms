from django.db import models
from django.contrib.auth.hashers import make_password
from django.utils.encoding import force_text, python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Agency(models.Model):
	pid = models.IntegerField(u'父节点',default=0,)
	name = models.CharField(u'机构名称',max_length=50,unique=True)
	phone = models.CharField(u'电话',max_length=50)
	email = models.EmailField(u'电子邮件')
	address = models.CharField(u'地址',max_length=254)
	website = models.URLField(u'网址')
	remark = models.TextField(u'简介')
	create_time = models.DateTimeField(auto_now_add=True)
	status = models.SmallIntegerField(default=1)

	def __str__(self):
		return self.name


@python_2_unicode_compatible
class User(models.Model):
	agency_id = models.IntegerField(u'所属机构',default=1)
	username  = models.EmailField(u'用户名',unique=True)
	password  = models.CharField(u'密码',max_length=128)
	nickname  = models.CharField(u'姓名',max_length=30)
	sex       = models.CharField(u'性别',max_length=1)
	phone     = models.CharField(u'电话',max_length=20)
	address   = models.CharField(u'地址',max_length=255)
	active_key = models.CharField(max_length=128,null=True)
	active_key_exp = models.DateTimeField(null=True)
	is_active = models.BooleanField(default=False)
	create_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)
	last_login_time = models.DateTimeField(null=True)
	status = models.SmallIntegerField(u'状态',default=1)

	def __str__(self):
		return self.nickname

@python_2_unicode_compatible
class RbacRole(models.Model):
	name = models.CharField(u'角色名称',max_length=100,unique=True)
	remark = models.CharField(u'描述',max_length=254)
	status = models.SmallIntegerField(default=1)
	rules = models.CharField(max_length=600,validators=['validate_comma_separated_integer_list'])

	class Meta:
		db_table = 'auth_rbac_role'

	def __str__(self):
		return self.name


@python_2_unicode_compatible
class RbacRoleAccess(models.Model):

	role = models.ForeignKey('RbacRole')
	user_id = models.IntegerField()
	# role_id = models.IntegerField()

	class Meta:
		db_table = 'auth_rbac_role_access'


@python_2_unicode_compatible
class RbacRule(models.Model):
	pid = models.IntegerField(u'上级权限',default=0)
	xlevel = models.SmallIntegerField(default=0)
	name = models.CharField(u'权限',max_length=80)
	title = models.CharField(u'权限名称',max_length=80)
	status = models.SmallIntegerField(default=1)
	condition = models.CharField(u'附加条件',max_length=100,blank=True,null=True)
	is_menu = models.BooleanField(u'是否作为菜单',default=False)

	class Meta:
		db_table = 'auth_rbac_rule'

	def __str__(self):
		return self.name



	




