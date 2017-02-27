from django.conf.urls import url
from . import views

app_name = 'ims'
urlpatterns = [
    url(r'^stores/$', views.StoreView.as_view(), name='index'),
    url(r'^items/$', views.ItemView.as_view(), name='items'),
   # url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(),
   #      name='results'),
   # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]