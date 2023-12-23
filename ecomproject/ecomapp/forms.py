from django import forms
from django.contrib.auth.models import User  
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ForgotPasswordForm(forms.Form):
    # Add fields for the forgot password form, if needed
    email = forms.EmailField()

class SignupForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match")

    # Additional validation and custom logic can be added as needed
from django import forms

class AddToCartForm(forms.Form):
    product_id = forms.IntegerField(widget=forms.HiddenInput())  # Hidden input to store product ID
    quantity = forms.IntegerField(min_value=1, initial=1)  # Quantity field with a minimum value of 1

class UpdateCartForm(forms.Form):
    cart_item_id = forms.IntegerField(widget=forms.HiddenInput())  # Hidden input to store cart item ID
    quantity = forms.IntegerField(min_value=1)  # Quantity field with a minimum value of 1

class RemoveFromCartForm(forms.Form):
    cart_item_id = forms.IntegerField(widget=forms.HiddenInput())  # Hidden input to store cart item ID
