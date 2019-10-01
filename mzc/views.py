from django.shortcuts import render
from django.http import HttpResponse
from .forms import faculityform
# Create your views here.
def indexpage(request):
    return render(request,'index.html')
def contactpage(request):
    return render(request,'contact.html')    
def homepage(request):    
    return render(request,'home.html')
def faculitypage(request):
    form = faculityform()
    return render(request,'faculity.html',{'form':form})    