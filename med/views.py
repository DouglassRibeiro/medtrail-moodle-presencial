from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'med/homepage.html')

def teste(request):
    return render(request, 'med/teste.html')

def teste_1(request):
    return render(request, 'med/teste_1.html')