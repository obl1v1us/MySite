#from django.http import HttpResponse, HttpResponseRedirect#, Http404
from django.shortcuts import get_object_or_404, render, render_to_response
#from django.urls import reverse
from django.views import generic
from django.forms import modelformset_factory
from .models import Store, Item, Manager, StoreItem
from .forms import StoreItemsForm


class StoreView(generic.ListView):
    template_name = 'ims/storelist.html'
    context_object_name = 'store_list'
    
    def get_queryset(self):
        """Return the list of stores"""
        return Store.objects.order_by('store_id')


def storedetail(request, store_id):
    store = get_object_or_404(Store, pk=store_id)
    return render_to_response('ims/storedetail.html',
                               {'store': store})

#DEBUG
def storeitemsform(request):
    StoreItemsFormSet = modelformset_factory(StoreItem, extra=0, 
                                             form=StoreItemsForm)
    if (request.method == 'POST'):
        #POSTING A FORM
        siformset = StoreItemsFormSet(request.POST)
        if siformset.is_valid():
            siformset.save()
            #RETURN TO STORE DETAIL PAGE
    else:
        siformset = StoreItemsFormSet()
    return render(request, 'ims/storerecount.html',
                                {'siformset' : siformset})
    
def storerecount(request, store_num):
    StoreItemsFormSet = modelformset_factory(StoreItem, 
                                extra=0, form=StoreItemsForm)
    # TODO get object or 404
    store = Store.objects.get(store_id=store_num)
    
    if (request.method == 'POST'):
        #POSTING A FORM
        siformset = StoreItemsFormSet(request.POST,
                                queryset=StoreItem.objects.filter(store_id=store_num))
        if siformset.is_valid():
            #TODO Add testing here
            siformset.save()
            return render_to_response('ims/storedetail.html',
                               {'store': store})
    else:
    # 
        siformset = StoreItemsFormSet(queryset=StoreItem.objects.filter(store_id=store_num))
    return render(request, 'ims/storerecount.html',
                                {'siformset' : siformset, 'store' : store})
                            
class ItemView(generic.ListView):
    template_name = 'ims/itemlist.html'
    context_object_name= 'item_list'
    
    def get_queryset(self):
        """Returns the list of items in the entire system"""
        return Item.objects.order_by('sku')
    
class ManagerView(generic.ListView):
    template_name = 'ims/managerlist.html'
    context_object_name= 'manager_list'
    
    def get_queryset(self):
        """Returns the list of managers in the entire system"""
        return Manager.objects.order_by('manager_id')
    
class StoreItemView(generic.ListView):
    template_name= 'ims/storeitems.html'
    context_object_name='storeitems_list'
    
    def get_queryset(self):
        return StoreItem.objects.order_by('store', 'item')
