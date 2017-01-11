from django.conf import settings
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from django.core.urlresolvers import reverse,resolve
from django.utils.deprecation import MiddlewareMixin

class AuthenticationMiddleware(MiddlewareMixin):

	def requiredLogin(self,urlName):
		if urlName == None:
			return False

		for a in settings.REQUIRED_LOGIN_APP:
			if urlName.startswith(a):
				return True
				
		return False

	def process_request(self, request):
		url_name = resolve(request.path_info).url_name
		if self.requiredLogin(url_name):
			if 'user_id' in request.session:
				if url_name not in request.session['rbac']:
					return HttpResponse('You dont have the access to this view')
				
			else:
				path = request.path_info.lstrip('/')
				if path != '':
					return HttpResponseRedirect(reverse('login'))
		else:
			pass

	def process_view(self,request,view,args,kwargs):
		pass



	def process_template_response(self, request, response):
		url_name = resolve(request.path_info).url_name
		response.context_data['menu'] = url_name.split('-')[0]
		response.context_data['submenu'] = url_name
		return response
		




