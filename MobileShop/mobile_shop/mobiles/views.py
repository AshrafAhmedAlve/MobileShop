from django.shortcuts import render, get_object_or_404, redirect
from .models import Mobile
from .forms import MobileForm
from .models import Category


# views.py
from django.shortcuts import render
from .models import Mobile

def mobile_list(request):
    search_query = request.GET.get('search', '')
    category_filter = request.GET.get('category', '')
    
    # Filtering mobiles based on the search query and category
    mobiles = Mobile.objects.all()
    
    if search_query:
        mobiles = mobiles.filter(name__icontains=search_query)
    
    if category_filter:
        mobiles = mobiles.filter(category=category_filter)
    
    return render(request, 'mobiles/mobile_list.html', {'mobiles': mobiles})



def add_mobile(request):
    if request.method == 'POST':
        form = MobileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mobile_list')
    else:
        form = MobileForm()
    return render(request, 'mobiles/add_mobile.html', {'form': form})



def edit_mobile(request, id):  # Accept the 'id' argument here
    mobile = get_object_or_404(Mobile, id=id)  # Get the mobile by its ID

    if request.method == 'POST':
        form = MobileForm(request.POST, request.FILES, instance=mobile)
        if form.is_valid():
            form.save()
            return redirect('mobile_list')
    else:
        form = MobileForm(instance=mobile)

    return render(request, 'mobiles/edit_mobile.html', {'form': form, 'mobile': mobile})


def delete_mobile(request, id):  # Accept the 'id' argument
    mobile = get_object_or_404(Mobile, id=id)  # Get the mobile by its ID

    if request.method == 'POST':  # Confirm the deletion with POST
        mobile.delete()  # Delete the mobile
        return redirect('mobile_list')  # Redirect to mobile list after deletion

    return render(request, 'mobiles/confirm_delete.html', {'mobile': mobile})  # Optional confirmation page

