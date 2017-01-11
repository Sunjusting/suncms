from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
import urllib

class extpaginator(Paginator):
	def _page_range_ext(self):
		num_count = 2 * 5 + 1
		if self.num_pages <= num_count:
			return range(1, self.num_pages + 1)
		num_list = []
		num_list.append(self.page_num)
		for i in range(1, self.range_num + 1):
			if self.page_num - i <= 0:
				num_list.append(num_count + self.page_num - i)
			else:
				num_list.append(self.page_num - i)

			if self.page_num + i <= self.num_pages:
				num_list.append(self.page_num + i)
			else:
				num_list.append(self.page_num + i - num_count)

		num_list.sort()
		return num_list

	page_range_ext = property(_page_range_ext)

	def countStr(self) :
		return '<li class="disable"><span>'+str(self.count)+'条记录</span></li>'
	
	def firstPage(self,pn,kwargs):
		urlstr ='&' + urllib.parse.urlencode(kwargs)
		if self.page(pn).has_previous():
			return '<li><a href="' + reverse('admin-users') + '?p=1'+ urlstr +'"> << </a></li>'
		else:
			return ''

	def lastPage(self,pn,kwargs):
		urlstr = '&' + urllib.parse.urlencode(kwargs)
		if self.page(pn).has_next():
			return '<li><a href="' + reverse('admin-users') + '?p=' + str(self.num_pages) + urlstr + '"> >> </a></li>'
		else:
			return ''

	def prevPage(self,pn,kwargs):
		urlstr = '&' + urllib.parse.urlencode(kwargs)
		if self.page(pn).has_previous():
			return '<li><a href="' + reverse('admin-users') + '?p=' + str(int(pn)-1) + urlstr + '"> < </a></li>'
			# return '<li><a href="' + reverse('admin-users',args=[int(pn)-1]) + '"> < </a></li>'
		else:
			return ''

	def nextPage(self,pn,kwargs):
		urlstr = '&' + urllib.parse.urlencode(kwargs)
		if self.page(pn).has_next():
			return '<li><a href="' + reverse('admin-users') + '?p=' + str(int(pn)+1) + urlstr + '"> > </a></li>'
			# return '<li><a href="' + reverse('admin-users',args=[int(pn)+1]) + '"> > </a></li>'
		else:
			return ''

	def pageList(self,pn,kwargs):
		urlstr = '&' + urllib.parse.urlencode(kwargs)
		pl = ''
		for p in self.page_range_ext:
			if p == int(pn) :
				pl = pl + '<li><span>' + str(p) + '</span></li>'
			else:
				pl = pl + '<li><a href="' + reverse('admin-users') + '?p=' + str(p) + urlstr + '">' + str(p) + '</a></li>'
		return pl

	
	def pagestr(self,pn,kwargs):
		pstr = '<ul class="pagination">'+self.countStr()+self.firstPage(pn,kwargs)+self.prevPage(pn,kwargs)+self.pageList(pn,kwargs)+self.nextPage(pn,kwargs)+self.lastPage(pn,kwargs)+'</ul>'
		return pstr