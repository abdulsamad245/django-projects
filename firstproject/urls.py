from django.urls import path
from firstproject.views import *


urlpatterns = [
    path('', myfunctioncall, name="index"),
    path('about', myfunctionabout, name="about"), 
    path('add/<int:a>/<int:b>',add, name="add"),  
    path('intro/<str:name>/<int:age>',intro, name="intro"),
    path('firstpage',firstpage, name="firstpage"),
    path('secondpage',secondpage, name="secondpage"),
    path('thirdpage',thirdpage, name="thirdpage"),
    path('image',image, name="imagepage"),
    path('form',form, name="form"),
    path('submitform',submitform, name="submitform"),
    path('form2',form2, name="form2")
]