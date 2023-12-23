from django.shortcuts import render
from django.contrib.auth.models import User
def index(request):
    # Your logic for the index view goes here
    return render(request, 'index.html')
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm, ForgotPasswordForm, SignupForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                # Redirect to a success page
                return redirect('products')  # Change 'success_page' to your success page URL
            else:
                # Invalid login credentials, handle accordingly
                pass
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def forgot_password_view(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            # Process the form data, send email, etc.
            pass
    else:
        form = ForgotPasswordForm()
    return render(request, 'forgotpassword.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, email=email, password=password)
            # Redirect to the login page after successful signup
            return redirect('login')  # Change 'login' to your login page URL
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def product_view(request):
    # Your logic for the product view goes here
    return render(request, 'product.html')
from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import AddToCartForm, UpdateCartForm, RemoveFromCartForm

# For simplicity, let's assume a dummy cart structure using session for this example.
# In a real-world scenario, you'd likely be using a database to manage cart items.
def cart_view(request):
    # Fetch cart items from the session or database. For now, we'll use a dummy list.
    cart_items = [
        {"id": 1, "name": "Men's Shirt", "price": 75, "quantity": 1},
        {"id":2,"name": "Men's Shirt", "price": 80, "quantity": 1},
        {"id":3,"name": "Women's dress", "price": 68, "quantity": 1},
        {"id":4,"name": "Women's dress", "price": 70, "quantity": 1},

        # ... add other products as needed
    ]
    total_price = sum(item["price"] * item["quantity"] for item in cart_items)
    
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, product_id):
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            product_id = form.cleaned_data['product_id']
            quantity = form.cleaned_data['quantity']

            # Here, you'd typically add the product to the cart (e.g., session or database).
            # For this example, we're just redirecting back to the cart view.
            return redirect('cart_view')
    else:
        form = AddToCartForm(initial={'product_id': product_id})

    return render(request, 'add_to_cart.html', {'form': form})

def update_cart(request):
    if request.method == 'POST':
        form = UpdateCartForm(request.POST)
        if form.is_valid():
            cart_item_id = form.cleaned_data['cart_item_id']
            quantity = form.cleaned_data['quantity']

            # Update the quantity of the item in the cart (e.g., session or database).
            # For this example, we're just redirecting back to the cart view.
            return redirect('cart_view')
    else:
        form = UpdateCartForm()

    return render(request, 'update_cart.html', {'form': form})

def remove_from_cart(request):
    if request.method == 'POST':
        form = RemoveFromCartForm(request.POST)
        if form.is_valid():
            cart_item_id = form.cleaned_data['cart_item_id']

            # Remove the item from the cart (e.g., session or database).
            # For this example, we're just redirecting back to the cart view.
            return redirect('cart_view')
    else:
        form = RemoveFromCartForm()

    return render(request, 'remove_from_cart.html', {'form': form})
