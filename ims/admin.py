from django.contrib import admin

from .models import Store, Item, StoreItem, Manager

admin.site.register(Store)
admin.site.register(Item)
admin.site.register(Manager)
admin.site.register(StoreItem)