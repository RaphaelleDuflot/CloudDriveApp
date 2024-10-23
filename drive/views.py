from django.shortcuts import render

# Create your views here.

def exemple(request):
    return render(request, 'exemple.html')