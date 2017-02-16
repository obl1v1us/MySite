from django.http import HttpResponse, HttpResponseRedirect#, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from . import Store

# Create your views here.
class StoreView(generic.ListView):
    template_name = 'IMS/index.html'
    context_object_name = 'store_list'
    
    def get_queryset(self):
        """Return the list of stores"""
        return Store.objects.order_by('store_id')