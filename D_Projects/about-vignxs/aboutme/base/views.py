from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def legacy(request):
    return render(request, "legacy.html")
  
def version2(request):
    return render(request, "version2.html")
