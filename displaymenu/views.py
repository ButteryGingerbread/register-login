from django.shortcuts import render
from .models import DisplayMenuModel

# Create your views here.

def display_all(request):
    all_data = DisplayMenuModel.objects.all()
    context = {
        'all_data': all_data,
    }
    return render(request, 'index.html', context)

def display_data_by_category(request, menu_category):
    menu_items = DisplayMenuModel.objects.filter(menu_category=menu_category)
    context = {
        'menu_category': menu_category,
        'menu_items': menu_items,
    }
    return render(request, 'index2.html', context)