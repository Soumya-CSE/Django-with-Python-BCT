from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Product

def app(request):
    query = request.GET.get('q', '').strip()
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    else:
        products = Product.objects.all()
    return render(request, 'newApp/app.html', {'products': products, 'query': query})

def about(request):
    return render(request, 'newApp/about.html')

def contact(request):
    return render(request, 'newApp/contact.html')

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'newApp/product_detail.html', {'product': product})

# Create your views here.
