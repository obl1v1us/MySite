from django.http import HttpResponse, HttpResponseRedirect#, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Store, Item


class StoreView(generic.ListView):
    template_name = 'ims/index.html'
    context_object_name = 'store_list'
    
    def get_queryset(self):
        """Return the list of stores"""
        return Store.objects.order_by('store_id')


class ItemView(generic.ListView):
    template_name = 'ims/itemlist.html'
    context_object_name= 'item_list'
    
    def get_queryset(self):
        """Returns the list of items in the entire system"""
        return Item.objects.order_by('sku')