from django.shortcuts import render

# Create your views here.
def doraemon(request):
    return render(request,'doraemon.html')

def Nobita(request):
    return render(request,'Nobita.html')