from django.urls import path
from votingapp.views import *
# import views

urlpatterns = [
    path('',index, name="index"),
    path('getquery',getquery, name="getquery"),
    path('sortdata',sortdata, name="sortdata"),
]