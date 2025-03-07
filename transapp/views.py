from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def get(request):
    return render(request, 'get-a-quote.html')

def index(request):
    return render(request, 'index.html')

def prising(request):
    return render(request, 'pricing.html')


def service(request):
    return render(request, 'service-details.html')

def services(request):
    return render(request, 'services.html')

def starter(request):
    return render(request, 'starter-page.html')