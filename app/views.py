from django.shortcuts import render

# Create your views here.

def local_bootstrap(request):
    return render(request,'local_bootstrap.html')