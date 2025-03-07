from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Product, Feedback, Contact
from .forms import FeedbackForm

def index(request):
    # Получение последних пяти товаров
    latest_products = Product.objects.all().order_by('-created_at')[:5]
    # Получение двух последних добавленных товаров для каждой категории
    categories = Category.objects.all()
    latest_products_by_category = {
        category: Product.objects.filter(category=category).order_by('-created_at')[:2]
        for category in categories
    }
    print(latest_products)  # Вывод последних пяти товаров в консоль
    return render(request, 'main/index.html', {
        'latest_products': latest_products,
        'latest_products_by_category': latest_products_by_category
    })

def contact(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Спасибо за ваш отзыв!')
    else:
        form = FeedbackForm()

    contacts = Contact.objects.all()
    return render(request, 'main/contact.html', {'form': form, 'contacts': contacts})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'catalog/product_detail.html', {'product': product})

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'catalog/category_detail.html', {'category': category, 'products': products})
