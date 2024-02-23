from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

from shop.models import CustomUser
from shop.utils import generate_random_code


class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label='Email',
        widget=forms.TextInput(attrs={'autofocus': True}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget.attrs.update({'autocomplete': 'current-password'})


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=30, required=True)
    customer_code = forms.CharField(max_length=6, required=False, widget=forms.HiddenInput())

    class Meta:
        model = CustomUser
        fields = ["email", "username", "customer_code", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.customer_code = generate_random_code()
        if commit:
            user.save()
        return user


class OrderForm(forms.Form):
    item_id = forms.IntegerField()
    amount = forms.DecimalField()
