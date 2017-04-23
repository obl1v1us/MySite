from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.views import generic
from django.forms import modelformset_factory
from django.forms.models import inlineformset_factory
from .models import Store, Item, Manager, StoreItem
from .forms import StoreItemsForm, UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied


class StoreView(generic.ListView):
    template_name = 'ims/storelist.html'
    context_object_name = 'store_list'
    
    def get_queryset(self):
        """Return the list of stores"""
        return Store.objects.order_by('store_id')
    
@login_required
def storedetail(request, store_id):
    store = get_object_or_404(Store, pk=store_id)
    return render(request, 'ims/storedetail.html',
                               {'store': store})

#DEBUG

def storeitemsform(request):
    StoreItemsFormSet = modelformset_factory(StoreItem, extra=0, 
                                             form=StoreItemsForm)
    if (request.method == 'POST'):
        #POSTING A FORM
        siformset = StoreItemsFormSet(request.POST)
        if siformset.is_valid():
            siformset.save()
            #RETURN TO STORE DETAIL PAGE
    else:
        siformset = StoreItemsFormSet()
    return render(request, 'ims/storerecount.html',
                                {'siformset' : siformset})

@login_required
def storerecount(request, store_num):
    StoreItemsFormSet = modelformset_factory(StoreItem, 
                                extra=0, form=StoreItemsForm)
    # TODO get object or 404
    store = Store.objects.get(store_id=store_num)
    
    if (request.method == 'POST'):
        #POSTING A FORM
        siformset = StoreItemsFormSet(request.POST,
                                queryset=StoreItem.objects.filter(store_id=store_num))
        if siformset.is_valid():
            #TODO Add testing here
            siformset.save()
            return render(request, 'ims/storedetail.html',
                               {'store': store})
    else:
    # 
        siformset = StoreItemsFormSet(queryset=StoreItem.objects.filter(store_id=store_num))
    return render(request, 'ims/storerecount.html',
                                {'siformset' : siformset, 'store' : store})
                            
class ItemView(generic.ListView):
    template_name = 'ims/itemlist.html'
    context_object_name= 'item_list'
    
    def get_queryset(self):
        """Returns the list of items in the entire system"""
        return Item.objects.order_by('sku')
    
class ManagerView(generic.ListView):
    template_name = 'ims/managerlist.html'
    context_object_name= 'manager_list'
    
    def get_queryset(self):
        """Returns the list of managers in the entire system"""
        return Manager.objects.order_by('manager_id')


# Use this to grant each manager the ability to change their own names
@login_required() # only logged in users should access this
def edit_manager(request, pk):
    # querying the User object with pk from url
    user = User.objects.get(pk=pk)

    # prepopulate UserProfileForm with retrieved user values from above.
    user_form = UserForm(instance=user)

    # Use inlineformset to include the user and manager in the same formset
    ManagerInlineFormset = inlineformset_factory(User, Manager)
    formset = ManagerInlineFormset(instance=user)

    if request.user.is_authenticated() and request.user.id == user.id:
        # The HTTP request has a completed form
        if request.method == "POST":
            # Process the first form to get a User formset
            user_form = UserForm(request.POST, request.FILES, instance=user)
            formset = ManagerInlineFormset(request.POST, request.FILES, instance=user)
            # Check if the form is valid
            if user_form.is_valid():
                # Process the second form to get the Manager formset
                created_user = user_form.save(commit=False)
                formset = ManagerInlineFormset(request.POST, request.FILES, instance=created_user)

                if formset.is_valid():
                    created_user.save()
                    formset.save()
                    return HttpResponseRedirect('/accounts/profile/')

        return render(request, "account/account_update.html", {
            "noodle": pk,
            "noodle_form": user_form,
            "formset": formset,
        })
    else:
        raise PermissionDenied

#DEBUG
class StoreItemView(generic.ListView):
    template_name= 'ims/storeitems.html'
    context_object_name='storeitems_list'
    
    def get_queryset(self):
        return StoreItem.objects.order_by('store', 'item')

def itemdetail(request, item_id):
    item = get_object_or_404(Item, sku=item_id)
    return render(request, 'ims/itemdetail.html',
                               {'item': item})
