from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import datetime
# from django.forms.models import ModelForm

''' Managers manage a store
    They are defined and created by a User object initiation
'''
class Manager(models.Model):
    # Manager's ID is the primary key
    manager_id = models.AutoField(primary_key=True)
    # A Manager's user according to Django
    user = models.OneToOneField(User, related_name="user")
    # A manager's hire date
    hire_date = models.DateTimeField(blank=True, default=datetime.datetime.now())
    # A managers casted to a string is the user's First name and Last name
    def __str__(self):
        return_val = self.user.first_name + " " + self.user.last_name
        return return_val
    
        
def create_manager(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        new_manager = Manager(user=user)
        new_manager.save()
        
post_save.connect(create_manager, sender=User)

# Many items can belong in an inventory (InventoryItem)
class Item(models.Model):
    # Item's SKU number is the primary key
    sku =  models.AutoField(primary_key=True)
    # Name of the item restricted to 30 chars
    item_name = models.CharField(max_length=30)
    """TODO Change this to a value restricted to a dollar amount"""
    #The cost of the item
    cost = models.IntegerField()
    description = models.CharField(max_length=30, blank=True, default="DEFAULT DESCRIPTION")
    
    # An Item casted to a string is just its name
    def __str__(self):
        return self.item_name
    
    def __unicode__(self):
        return self.name
    
# Stores are managed by a Manager
# Stores contain items (through StoreItem)
class Store(models.Model):
    # Store ID number is the Primary key (auto filled)
    store_id = models.AutoField(primary_key=True)
    # Store name restricted to 30 chars
    store_name = models.CharField(max_length=30)
    # Store manager - One to One relationship
    store_manager = models.OneToOneField(
        Manager,
        # Stores don't need a manager 
        blank = True, null = True,
        on_delete = models.CASCADE
    )
    address = models.CharField(blank=True, default="Dream St", max_length=100)
    phone_number = models.CharField(blank=True, default="555-555-5555", max_length=20)
    
    # Items and Stores have a many-to-many relationship through the StoreItem
    # class. This allows a combination of store/item to remain unique, and contain
    # more information such as quantity
    items = models.ManyToManyField(Item, through='StoreItem')
    
    # A store turned to string is just the store's name
    def __str__(self):
        return self.store_name
    
    def __unicode__(self):
        return self.name
    '''TODO Create a modified __init__ to add all items to stores on creation'''

# Adds all items into a store
def create_store_inventory(sender, **kwargs):
    new_store = kwargs["instance"]
    if kwargs["created"]:
        for item in Item.objects.all():
            new_storeitem = StoreItem(store=new_store, item=item)
            new_storeitem.save()
    
post_save.connect(create_store_inventory, sender=Store)


# StoreItems are an intermediary field that manages the items within a store
class StoreItem(models.Model):
    # each of these links two foreign keys (Store, Item) to a single StoreItem
    # row in the table. 
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    # represents the quantity an item has at a particular store
    qty = models.IntegerField(default=0)
    
    # These will be used by function calls in other classes to change a item's 
    # quantity.
    @property
    def quantity(self):
        # Get the current value of quantity
        return self.qty
    
    # A quantity setter that changes the value while returning a variance
    @quantity.setter
    def quantity(self, value):
        # find the variance
        return_val = self.qty - value
        # TODO Check for negative values, null values??
        # set the new quantity
        self._quantity = value
        # return the variance
        return return_val
    
    # Defines how a StoreItem looks. Typically not used except in debugg
    def __str__(self):
        return_val = self.store.__str__() + " - " + self.item.__str__()
        return return_val
    
    '''TODO Create internal method to populate a given store with all items?'''
        
# DEPRECATED, Does not work
'''
class InventoryItem(models.Model):
    inv_item = models.ForeignKey(Item, on_delete=models.CASCADE,
                                  related_name="inv_item_rel")
    _quantity = models.IntegerField()
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE,
                                 related_name="store_id_rel")
    
    # The set of inventory item and store id is the primary key
    class Meta:
        unique_together=(("inv_item", "store_id"))
    
    @property
    def quantity(self):
        Get the current value of quantity
        return self.quantity
    
    @quantity.setter
    def quantity(self, value):
        Set the current value of quantity, return a variance
        return_val = self._quantity - value
        # TODO Check for negative values, null values??
        self._quantity = value
        return return_val
        
    def __str__(self):
        return self.inv_item.sku
'''