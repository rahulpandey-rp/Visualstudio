from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from store.models import OrderModel, User, BuyerModel, AddressModel

class BuyerForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone_no = forms.CharField(required=True)
    address = forms.CharField(max_length=300, required=False)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.user_type = 2
        user.save()
        buyer = BuyerModel.objects.create(user=user)
        buyer.first_name = self.cleaned_data.get('first_name')
        buyer.last_name = self.cleaned_data.get('last_name')
        buyer.phone_no = self.cleaned_data.get('phone_no')
        buyer.email = self.cleaned_data.get('email')
        AddressModel.address = self.cleaned_data.get('address')
        AddressModel.default = True
        buyer.save()
        return user


class SellerForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone_no = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.user_type = 2
        user.save()
        buyer = BuyerModel.objects.create(user=user)
        buyer.first_name = self.cleaned_data.get('first_name')
        buyer.last_name = self.cleaned_data.get('last_name')
        buyer.phone_no = self.cleaned_data.get('phone_no')
        buyer.email = self.cleaned_data.get('email')
        buyer.save()
        return user

class CheckoutForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    address = forms.CharField(required=False)

    class Meta(forms.Form):
        model = OrderModel

