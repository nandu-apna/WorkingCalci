from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.

def index(request):
    return render(request,'index.html')

def submit(request):
    
    try:
        q=request.GET['query']
        ans=eval(q)
        mydict={
            "q":q,
            "ans":ans,
            "error":False,
        }
        return render(request,"index.html",context=mydict)
    
    except :
        
        mydict={
            "error":True
        }
        return render(request,"index.html",context=mydict)
    
def about(request):
    return render(request,'about.html')