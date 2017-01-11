"""ccpitcms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from auth import views as auth_views
from admin import views as admin_views
from front import views as front_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',front_views.index,name="front-index"),
    url(r'^login/',auth_views.login,name='login'),
    url(r'^register/',auth_views.register,name="register"),
    url(r'^checkUser/',auth_views.checkUser,name="checkUser"),
    url(r'^logout/',auth_views.logout,name="logout" ),
    url(r'^test/',auth_views.test,name="test"),
    url(r'^admin/$', admin_views.index, name="admin-index"),
    url(r'^admin/agencies/', admin_views.agencies, name="admin-agencies"),
    # url(r'^admin/addAgency/',admin_views.addAgency,name="admin-add-agency1"),
    url(r'^admin/addAgency/(\d+)/$',admin_views.addAgency,name="admin-add-agency"),
    url(r'^admin/editAgency/(\d+)/$',admin_views.editAgency,name="admin-edit-agency"),
    url(r'^admin/users/$',admin_views.users, name="admin-users"),
    url(r'^admin/addUser/$',admin_views.addUser,name="admin-add-user"),
    url(r'^admin/test/', admin_views.test, name="admin-test"),
    url(r'^admin/test2/', admin_views.test2, name="admin-test2"),
    url(r'^admin/editUser/(\d+)/$',admin_views.editUser,name="admin-edit-user"),
    url(r'^admin/rules/$',admin_views.rules, name="admin-rules"),
    url(r'^admin/addRule/(\d+)/$',admin_views.addRule,name="admin-add-rule"),
    url(r'^admin/editRule/(\d+)/$',admin_views.editRule,name="admin-edit-rule"),
    url(r'^admin/roles/$',admin_views.roles, name="admin-roles"),
    url(r'^admin/addRole/$',admin_views.addRole,name="admin-add-role"),
    url(r'^admin/editRole/(\d+)/$',admin_views.editRole,name="admin-edit-role"),
    url(r'^admin/setRole/(\d+)/$',admin_views.setRole,name="admin-set-role"),
    url(r'^admin/access/(\d+)/$',admin_views.access,name="admin-access"),
    url(r'^admin/test3/(\d+)/$',admin_views.test3,name="admin-test3"),
    url(r'^admin/testCheck/(.+)/$',admin_views.testCheck,name="admin-test-check"),

    url(r'^event/',include('event.urls')),
    url(r'^front/',include('front.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
