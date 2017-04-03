from django.conf.urls import url
from . import views, forms

app_name = 'ims'
urlpatterns = [
    url(r'^stores/$', views.StoreView.as_view(), name='stores'),
    url(r'^stores/(?P<store_id>[0-9]+)/', views.storedetail, name='storedetail'),
    #url(r'^stores/(?P<store_id>[0-9]+)/count', views.storerecount, name='storerecount'),
    url(r'^storeitemsform/$', views.storeitemsform, name='storeitemsform'),
    url(r'^managers/$', views.ManagerView.as_view(), name='managers'),
    url(r'^items/$', views.ItemView.as_view(), name='items'),
    url(r'^storeitems/$', views.StoreItemView.as_view(), name='storeitems')
]