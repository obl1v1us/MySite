from django.contrib import admin

from .models import Store, Item#, InventoryItem, Manager

admin.site.register(Store)
admin.site.register(Item)