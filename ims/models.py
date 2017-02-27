from django.db import models

# A manager takes care of a store
class Manager(models.Model):
    manager_id = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    # Managers can exist without a store
    def __str__(self):
        return self.manager_id

# Stores are managed by a manager
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
    
    def __str__(self):
        return self.store_id

# Many items can belong in an inventory (InventoryItem)
class Item(models.Model):
    sku =  models.IntegerField(primary_key=True)
    item_name = models.CharField(max_length=30)
    cost = models.IntegerField()
        
# Inventory items have an Item, a Store it belongs to, and a qty in that store
class InventoryItem(Item):
    inv_item = models.ForeignKey(Item, on_delete=models.CASCADE,
                                  related_name="inv_item")
    _quantity = models.IntegerField()
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE,
                                 related_name="store_id")
    
    # The set of inventory item and store id is the primary key
    class Meta:
        unique_together=(("inv_item", "store_id"))
    
    @property
    def quantity(self):
        '''Get the current value of quantity'''
        return self.quantity
    
    @quantity.setter
    def quantity(self, value):
        '''Set the current value of quantity, return a variance'''
        return_val = self._quantity - value
        # TODO Check for negative values, null values??
        self._quantity = value
        return return_val
        
    def __str__(self):
        return self.inv_item.sku