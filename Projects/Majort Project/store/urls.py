from django.urls import path
from . import views
from paypal.standard.ipn.views import ipn

urlpatterns=[
    path('',views.home,name="home"),
    path('laptops/',views.shop,name="shop"),
    path('brand/<int:brand_id>/', views.brand_products, name='brand_products'),
    path('laptop/<int:laptop_id>/', views.laptop_detail, name='laptop_detail'),
    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:laptop_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('checkout/', views.checkout, name='checkout'),
    path('paypal/', views.paypal_return, name='paypal_return'),
    path('paypal-cancel/', views.paypal_cancel, name='paypal_cancel'),
    path('paypal-ipn/', ipn, name='paypal-ipn'),
    path('my-orders/', views.my_orders, name='my_orders'),
]