from django.contrib import admin
from django.urls import path

from hub.views import *

urlpatterns = [
    path('',mobiles_catagory,name='mobiles_catagory'),

]
