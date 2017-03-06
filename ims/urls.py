from django.conf.urls import url
from . import views

app_name = 'ims'
urlpatterns = [
    url(r'^stores/$', views.StoreView.as_view(), name='stores'),
    url(r'^managers/$', views.ManagerView.as_view(), name='managers'),
    url(r'^items/$', views.ItemView.as_view(), name='items'),
    url(r'^storeitems/$', views.StoreItemView.as_view(), name='storeitems')
]