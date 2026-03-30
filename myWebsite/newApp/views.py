from django.shortcuts import render

def app(request):
    return render(request, 'newApp/app.html')

def about(request):
    return render(request, 'newApp/about.html')

def contact(request):
    return render(request, 'newApp/contact.html')

# Create your views here.
