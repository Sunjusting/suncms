from .models import RbacRole,RbacRule,RbacRoleAccess

class rbac():

	def getRole(self,user_id):
		roles = RbacRoleAccess.objects.filter(user_id=user_id)
		return roles

	def getRuleList(self,user_id):
		roles = self.getRole(user_id)
		rs = []
		for r in roles:
			rl = r.role.rules.split(',')
			rs.extend(rl)
		rss = []
		for r in rs:
			if int(r) not in rss:
				rss.append(int(r))
		return rss

	def getRbacList(self,request,user_id):
		if 'rbac' in request.session:
			return request.session['rbac']
		else:
			rules = self.getRuleList(user_id)
			rs = RbacRule.objects.filter(id__in=rules).values_list('name',flat=True)
			rss = []
			for r in rs:
				rss.append(r)
			request.session['rbac'] = rss
			return request.session['rbac']

	def check(self,name,user_id):
		rbacList = self.getRbacList(user_id)
		if name in rbacList:
			return True
		else:
			return False

	


		
		
	