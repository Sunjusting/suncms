from django.conf.urls import url
from event import views as event_views

urlpatterns = [    
    url(r'^$',event_views.index,name="event-index"),
    url(r'^add/$',event_views.add,name="event-add"),
    url(r'^edit/(\d+)/$',event_views.edit,name="event-edit"),
    url(r'^show/(\d+)/$',event_views.show,name="event-show"),
    url(r'^agendas/(\d+)/$',event_views.agendas,name="event-agendas"),
    url(r'^addAgenda/(\d+)/$',event_views.addAgenda,name="event-add-agenda"),
    url(r'^editAgenda/(\d+)/$',event_views.editAgenda,name="event-edit-agenda"),
    url(r'^deleteAgenda/(\d+)/$',event_views.deleteAgenda,name="event-delete-agenda"),
]