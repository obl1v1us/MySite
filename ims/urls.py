from django.conf.urls import url
from . import views

# gDefine which app this URL will find it's patterns
app_name = 'ims'
urlpatterns = [
    # URL for a user to input their own qty into a specific store
    url(r'^stores/(?P<store_num>[0-9]+)/count', views.storerecount, \
                                                name='storerecount'),
               
    # Details for a particular store, including inventory totals
    url(r'^stores/(?P<store_id>[0-9]+)/', views.storedetail, name='storedetail'),
    
    url(r'^stores/$', views.StoreView.as_view(), name='stores'),
    
    # A Debug URL that shows every StoreItem row with a form
    #DEBUG
    url(r'^storeitemsform/$', views.storeitemsform, name='storeitemsform'),
    
    # URL for a list of all managers
    url(r'^managers/$', views.ManagerView.as_view(), name='managers'),
    
    # URL for a list of all items
    url(r'^items/$', views.ItemView.as_view(), name='items'),
    
    # URL for a list of all storeitems
    url(r'^storeitems/$', views.StoreItemView.as_view(), name='storeitems'),
    
    # Front page of IMS, Shows a login page or the user's Store view as default
    url(r'$', views.StoreView.as_view(), name='home_page'),
]