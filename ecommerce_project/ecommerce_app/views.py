# ecommerce_app/views.py
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product

def home(request):
    query = request.GET.get('q', '')
    all_products = Product.objects.filter(
        Q(product_no__icontains=query) |
        Q(description__icontains=query) |
        Q(price__icontains=query) |
        Q(category__icontains=query)
    )

    paginator = Paginator(all_products, 10)
    page = request.GET.get('page', 1)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    # Get categories with counts
    categories_with_counts = Product.objects.values('category').annotate(count=Count('category')).order_by('-count')[:5]

    return render(request, 'home.html', {'products': products, 'query': query, 'categories_with_counts': categories_with_counts})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    # Get categories with counts
    categories_with_counts = Product.objects.values('category').annotate(count=Count('category')).order_by('-count')[:5]
    return render(request, 'product_detail.html', {'product': product, 'categories_with_counts': categories_with_counts})

def category_search(request, category):
    # Use exact match for category
    products = Product.objects.filter(category__exact=category)
    # Get categories with counts
    categories_with_counts = Product.objects.values('category').annotate(count=Count('category')).order_by('-count')[:5]
    return render(request, 'search_results.html', {'search_results': products, 'query': category, 'categories_with_counts': categories_with_counts})
