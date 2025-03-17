from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Laptop,CartItem,Order,Brand
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid

def home(request):
    brands = Brand.objects.all() 
    laptops = Laptop.objects.all().order_by('-created_at')[:8]  # Show latest 8 laptops
    return render(request, 'store/home.html', {'brands':brands,'laptops': laptops})

def shop(request):
    laptops=Laptop.objects.all()
    return render(request,"store/shop.html",{"laptops":laptops})

def brand_products(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)  # Get brand by ID
    laptops = Laptop.objects.filter(brand=brand)  # Filter products by brand
    return render(request, 'store/brand.html', {'brand': brand, 'laptops': laptops})

def laptop_detail(request, laptop_id):
    laptops=Laptop.objects.all()
    laptop = get_object_or_404(Laptop, id=laptop_id)
    return render(request, 'store/laptop_detail.html', {'laptop': laptop,'laptops':laptops})

@login_required(login_url='login')
def add_to_cart(request, laptop_id):
    laptop = get_object_or_404(Laptop, id=laptop_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, laptop=laptop)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

@login_required(login_url='login')
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.total_price() for item in cart_items)
    return render(request, 'store/cart.html', {'cart_items': cart_items, 'total': total})

@login_required
def remove_from_cart(request, cart_id):
    cart_item = get_object_or_404(CartItem, id=cart_id, user=request.user)
    cart_item.delete()
    return redirect('cart')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'store/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'store/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.total_price() for item in cart_items)

    invoice_id = str(uuid.uuid4())  # Generate a unique invoice ID

    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": total,
        "item_name": "Laptop Purchase",
        "invoice": invoice_id,
        "currency_code": "USD",
        "notify_url": request.build_absolute_uri("/paypal-ipn/"),
        "return_url": request.build_absolute_uri("/paypal/"),
        "cancel_return": request.build_absolute_uri("/paypal-cancel/"),
    }

    form = PayPalPaymentsForm(initial=paypal_dict)

    return render(request, "store/checkout.html", {"form": form, "total": total,"items":cart_items})

def paypal_return(request):
    # Clear the cart after successful payment
    CartItem.objects.filter(user=request.user).delete()
    return render(request, "store/paypal_success.html")

def paypal_cancel(request):
    return render(request, "store/paypal_cancel.html")

def paypal_return(request):
    total = sum(item.total_price() for item in CartItem.objects.filter(user=request.user))

    # Create an order record
    order = Order.objects.create(user=request.user, total_amount=total)

    # Clear the cart after successful payment
    CartItem.objects.filter(user=request.user).delete()

    return render(request, "store/paypal_success.html", {"order": order})

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, "store/my_orders.html", {"orders": orders})

