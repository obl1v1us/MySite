from django.forms import ModelForm
from .models import StoreItem#, Manager

class StoreItemsForm(ModelForm):
    class Meta:
        model = StoreItem
        #fields = ['store', 'item', 'qty',]
        fields = ['qty',]