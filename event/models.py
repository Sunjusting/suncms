from django.db import models
from PIL import Image
from django.utils.encoding import force_text, python_2_unicode_compatible
import uuid
import os

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('images/', filename)


# Create your models here.
@python_2_unicode_compatible
class Event(models.Model):
	user = models.ForeignKey('auth.User')
	name = models.CharField(u'活动名称',max_length=50)
	ename = models.CharField(u'Event Name',max_length=50)
	hosts = models.CharField(u'主办',max_length=254)
	organizer = models.CharField(u'承办',max_length=254)
	contact = models.CharField(u'联系人',max_length=50)
	address = models.CharField(u'联系地址',max_length=254)
	phone = models.CharField(u'电话',max_length=50)
	email = models.EmailField(u'电子邮件')
	website = models.URLField(u'网址')
	city = models.ForeignKey('City')
	venue = models.CharField(u'场馆',max_length=254)
	vaddress = models.CharField(u'地址',max_length=254)
	category = models.ForeignKey('Category')
	start_at = models.DateTimeField(u'开始时间')
	end_at = models.DateTimeField(u'结束时间')	
	intro = models.TextField(u'简介')
	create_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)
	status = models.SmallIntegerField(default=1)
	verfied = models.BooleanField(u'审核状态',default=False)
	image = models.ImageField(u'活动海报',upload_to=get_file_path)


	def __str__(self):
		return self.name

		


@python_2_unicode_compatible
class City(models.Model):
	city = models.CharField(u'城市',max_length=50)
	encity = models.CharField(u'City',max_length=50)

	def __str__(self):
		return self.city


@python_2_unicode_compatible
class Category(models.Model):
	name = models.CharField(u'分类',max_length=50)
	ename = models.CharField(u'Category',max_length=50)

	def __str__(self):
		return self.name

@python_2_unicode_compatible
class Agenda(models.Model):
	event = models.ForeignKey('Event')
	day = models.DateField(u'日期')
	start_time = models.TimeField(u'开始时间')
	end_time = models.TimeField(u'结束时间')
	subject = models.CharField(u'主题',max_length=60)
	place = models.CharField(u'地点',max_length=100)
	sort = models.SmallIntegerField(u'排序',default=1)
	intro = models.TextField(u'简介')

	def __str__(self):
		return self.subject