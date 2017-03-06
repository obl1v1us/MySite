from django.db import models

# A manager takes care of a store
class Manager(models.Model):
    manager_id = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    # Managers can exist without a store
    def __str__(self):
        return_val = self.manager_id.__str__() + ": " + self.fname + \
            " " + self.lname
        return return_val


# Many items can belong in an inventory (InventoryItem)
class Item(models.Model):
    sku =  models.IntegerField(primary_key=True)
    item_name = models.CharField(max_length=30)
    
    """TODO Change this to a value restricted to a dollar amount"""
    cost = models.IntegerField()
    
    def __str__(self):
        return_val = self.sku.__str__() + ": " + self.item_name
        return return_val
    
# Stores are managed by a StoreItem
# Stores have items (InventoryItem)
class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    store_name = models.CharField(max_length=30)
    store_manager = models.OneToOneField(
        Manager,
        # Stores don't need a manager 
        blank = True, null = True,
        on_delete = models.CASCADE
    )
    items = models.ManyToManyField(Item, through='StoreItem')
    
    def __str__(self):
        return_val = self.store_id.__str__() + ": " + self.store_name.__str__()
        return return_val
    
    # TODO Create a modified create to add all items to stores on creation?
    
# store Items are an intermediate field that manages the 
class StoreItem(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    _qty = models.IntegerField()
    
    @property
    def quantity(self):
        # Get the current value of quantity
        return self._qty
    
    @quantity.setter
    def quantity(self, value):
        # Set the current value of quantity, return a variance
        return_val = self._qty - value
        # TODO Check for negative values, null values??
        self._quantity = value
        return return_val
    
    def __str__(self):
        return_val = self.store.__str__() + " - " + self.item.__str__()
        return return_val
    
    # TODO Create internal method to populate a given store with all items?
    
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