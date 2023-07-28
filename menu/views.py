from django.shortcuts import render
from .models import Menu, Category, Cuisine
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    return HttpResponse('Hi')

def show_category(request):
    category = Category.objects.all()
    data=[]

    for item in category:
        data.append({
            'category': item.name
        })
    
    return JsonResponse(data, safe=False)

def show_menu(request):
    menu_items = Menu.objects.select_related().all()
    print(menu_items)
    data = []

    for food in menu_items:
        data.append({
            'name': food.name,
            'description': food.description,
            'price': int(food.price),
            'spicy_level': food.spice_level,
            'category': food.category.name,
            'cuisine': food.cuisine.name
        })

    return JsonResponse(data, safe=False)