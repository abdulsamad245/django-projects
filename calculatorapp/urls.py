from django.urls import path, include 
from calculatorapp.views import *

urlpatterns = [
    path('',index,name='index'),
    path('submitquery',submitquery,name='submitquery')
]
