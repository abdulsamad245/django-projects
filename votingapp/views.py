from django.http import HttpResponse
from django.shortcuts import render
  

# Create your views here.
globalcount =  dict()
sorted_desc = False
arr = ['java', 'python', 'C++', 'Dotnet', 'javascript','php']

def index(request):
    dictionary  = {
        "arr":arr
    }
    return render (request, 'index.html', dictionary )

def getquery(request):
    q = request.GET['languages']
    if q in globalcount:
        globalcount[q] = globalcount[q]+1
    else:
        globalcount[q] = 1
    
    dictionary  = {
        "dictionary":globalcount,
        "arr":arr
    }
    # return HttpResponse(q)
    return render(request,'index.html',context=dictionary )

def sortdata(request):
    global globalcount 
    global sorted_desc
    if not sorted_desc:
            globalcount = dict(sorted(globalcount.items(), key=lambda x:x[1],reverse=True))
            sorted_desc = True
            # globalcount = {"a":1}
            dictionary  = {
                "dictionary":globalcount,
                "sorted":sorted_desc
        }
    else:
            globalcount = dict(sorted(globalcount.items(), key=lambda x:x[1]))
            sorted_desc = False
            # globalcount = {"a":1}
            dictionary  = {
                "dictionary":globalcount,
                "sorted":sorted_desc
        }       
        
    

    return render(request,'index.html',context=dictionary )
    
    
