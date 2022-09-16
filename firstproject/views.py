from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import *

# Create your views here.
def error_404_view(request,exception):
    return render(request,'404.html')

def myfunctioncall(request):
    return HttpResponse("Hello world!")

def myfunctionabout(request):
    return HttpResponse("About...!") 

def add (request,a,b):
    return HttpResponse(a+b ) 


def intro (request,name,age):
    mydictionary = {
        "name" : name,
        "age"  : age
    }
    return JsonResponse(mydictionary) 

def firstpage (request):
    return render(request,'index.html')

def secondpage (request):
    return render(request,'second.html')

def thirdpage (request):
    var = "Hello"
    fruits = ['apple','orange']
    dictionary = {"var":var, "fruits":fruits, "ans":False}
    return render(request,'third.html',context = dictionary)
 
def image (request):
    return render(request,'image.html')

def form (request):
    return render(request,'form.html')

def submitform (request):
    dictionary = {
        "var1": request.POST['name'],
        "var2": request.POST['textarea'],
        "method":request.method
    }
    return JsonResponse(dictionary)

def form2 (request):
    if request.method == "POST":
       form = FormFeedback(request.POST)
       if form.is_valid():
        title = request.POST['title']
        subject = request.POST['subject']
        dictionary = {
                "form":FormFeedback()
            }
        
        errorflag = False
        Errors = []
        if title != title.upper():
            # dictionary['error'] = True
            errormsg = "Title should be in capital"
            errorflag = True
            Errors.append(errormsg)
            # return render (request, 'form2.html', dictionary)
        
        import re
        if subject != 'Subject':
            errorflag = True
            errormsg = "Not a subject"
            Errors.append(errormsg)
            
        if errorflag != True:
            dictionary['success'] = True
            dictionary['successmsg'] = 'Form Submitted'
            return render (request, 'form2.html', dictionary)

            
        dictionary['error'] = errorflag
        dictionary['errors'] = Errors
        return render (request, 'form2.html', dictionary)
            
            

        # else:    
        #     dictionary['success'] = True
        #     dictionary['successmsg'] = 'Form Submitted'
        # return render (request, 'form2.html', dictionary)
       
               
               
    elif request.method =='GET':
        form = FormFeedback()
        dictionary = {
            "form":form
        }
        
    return render (request, 'form2.html', dictionary)
 

