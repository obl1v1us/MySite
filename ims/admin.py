from django.contrib import admin

from .models import Store, Item, Manager, StoreItem
from ims.models import StoreItem

admin.site.register(Store)
admin.site.register(Item)
admin.site.register(Manager)
admin.site.register(StoreItem)