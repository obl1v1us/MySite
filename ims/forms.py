from django.forms import ModelForm
from .models import StoreItem#, Manager
from django.contrib.auth.models import User

class StoreItemsForm(ModelForm):
    class Meta:
        model = StoreItem
        #fields = ['store', 'item', 'qty',]
        fields = ['qty',]

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']