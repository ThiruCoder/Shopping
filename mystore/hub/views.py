from django.shortcuts import redirect, render
import os
from django.conf import settings
from hub.models import *


# Create your views here.

def mobiles_catagory(request):
    catagories = CatagoryHub.objects.all()
    mobile_product = MobileProductDetail.objects.all()
    highLights = Highlight.objects.all()
    

    context = {'catagory':catagories,
               'products':mobile_product,
               'highLights':highLights,
               }

    return render(request, 'home.html',context)

# def product_details(request):
#     mobile_product = MobileProductDetail.objects.all()
#     context = {'products':mobile_product}
#     return render(request, 'home.html',context)

