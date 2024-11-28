from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'pages/homepage.html')

def homepage_register(request):
    return render(request, 'pages/homepage_register.html')

def just_register(request):
    return render(request, 'pages/just_register.html')