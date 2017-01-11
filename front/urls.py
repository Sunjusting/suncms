from django.conf.urls import url
from front import views as front_views

urlpatterns = [    
    url(r'^show/(\d+)/$',front_views.show,name="front-show"),
]