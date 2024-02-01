from django.shortcuts import render

# Create your views here.
def one(request):
    return render(request, 'te/1.html')

def twu(request):
    return render(request, 'te/2.html')

def fri(request):
    return render(request, 'te/3.html')