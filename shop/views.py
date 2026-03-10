from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Product
from django.contrib import messages

def home(request):
    return render(request, 'shop/home.html')

def product_list(request):
    products = Product.objects.all()
    cart = request.session.get('cart', {})
    cart_count = sum(cart.values()) if cart else 0
    
    return render(request, 'shop/list.html', {
        'products': products, 
        'cart_count': cart_count
    })

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart
    return redirect('product_list')

def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    for p_id, quantity in cart.items():
        product = get_object_or_404(Product, id=p_id)
        subtotal = product.price * quantity
        total += subtotal
        cart_items.append({'product': product, 'quantity': quantity, 'subtotal': subtotal})
    return render(request, 'shop/cart.html', {'cart_items': cart_items, 'total': total})

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    
    p_id = str(product_id)
    cart[p_id] = cart.get(p_id, 0) + 1
    
    request.session['cart'] = cart
    request.session.modified = True 
    
    messages.success(request, "Товар додано до вашої колекції")
    return redirect('product_list')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')
    else:
        form = UserCreationForm()
    return render(request, 'shop/register.html', {'form': form})

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    p_id = str(product_id)
    if p_id in cart:
        del cart[p_id]
        request.session['cart'] = cart
        request.session.modified = True
    return redirect('view_cart')

def checkout(request):
    request.session['cart'] = {}
    request.session.modified = True
    return render(request, 'shop/success.html')