from django.shortcuts import render
from .models import prueba

# Create your views here.
def main(request):
    r1 = len(prueba.objects.all())
    r = prueba.objects.all()[r1-100:]
    data = []
    time = []
    for i in range(len(r)):
        data.append(r[i].V1)
        time.append(i)
    return render(request,'main.html',context={'tiempo': time,'datos': data})


def index(request):
   return render(request, 'main2.html')


def dashboard(request):
   return render(request, 'dashboard.html')


def canal1(request):
   return render(request, 'canal1.html')


def canal2(request):
   return render(request, 'canal2.html')


def canal3(request):
   return render(request, 'canal3.html')


def canal4(request):
   return render(request, 'canal4.html')


def canal5(request):
   return render(request, 'canal5.html')


def canal6(request):
   return render(request, 'canal6.html')


def canal7(request):
   return render(request, 'canal7.html')


def canal8(request):
   return render(request, 'canal8.html')


def canal9(request):
   return render(request, 'canal9.html')


def canal10(request):
   return render(request, 'canal10.html')


def canal11(request):
   return render(request, 'canal11.html')


def canal12(request):
   return render(request, 'canal12.html')
