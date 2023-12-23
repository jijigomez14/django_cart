
from django.urls import path
from .views import index, login_view, forgot_password_view, signup_view, product_view
from . import views
urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('forgot-password/', forgot_password_view, name='forgot_password'),
    path('signup/', signup_view, name='signup'),
    path('products/', product_view, name='products'),
    path('cart/', views.cart_view, name='cart_view'),  # URL for displaying the cart
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),  # URL for adding to cart
    path('update_cart/', views.update_cart, name='update_cart'),  # URL for updating cart
    path('remove_from_cart/', views.remove_from_cart, name='remove_from_cart'),  # URL for removing from cart
]
  # Update the name to 'products'

