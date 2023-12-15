from django.shortcuts import render

# Create your views here.
def index(request):
   return render(request, 'dashboard.html')

def main(request):
   return render(request,'main.html',context={'text': 'Hellow world'})

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