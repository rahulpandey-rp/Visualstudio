from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import View
from .forms import BuyerForm, CheckoutForm
from django.core.exceptions import ObjectDoesNotExist
from .models import ProductModel, User, OrderModel
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from .models import *
# Create your views here.
class HomepageView(ListView):
    paginate_by = 2
    template_name = "store/homepage.html"
    model = ProductModel
    ordering = ["-id"]

class ItemDetailView(DetailView):
    model = ProductModel
    template_name = "store/product.html"

class CartView(ListView):
    model = OrderModel
    template_name = "store/cart.html"
    def get_queryset(self):
        data = super().get_queryset()
        return data

class ProfileView(View):
    def get(self, *args, **kwargs):
        profile = self.request.user
        objects = BuyerModel.objects.get(user=self.request.user)
        context = {
            'object': profile,
            'objects': objects
        }
        return render(self.request, 'store/profile.html', context)

class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = OrderModel.objects.filter(user=self.request.user, status=False)
            context = {
                'object': order
            }
            return render(self.request, 'store/cart.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("/store")

class CheckoutView(View):
    def get(self, *args, **kwargs):
        try:
            order = OrderModel.objects.filter(user=self.request.user, status=False)
            form = CheckoutForm()
            context = {
                'form': form,
                'order': order
            }
            return render(self.request, "store/checkout.html", context)
        except ObjectDoesNotExist:
            messages.info(self.request, "You do not have an active order")
            return redirect("cart")

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        order = OrderModel.objects.filter(user=self.request.user, status=False)
        print(order)
        form.is_valid()
        for orders in order:
            product = ProductModel.objects.get(id = orders.product_id)
            product.quantity  -= orders.quantity
            product.save()
            orders.f_name = form.cleaned_data.get('first_name')
            orders.l_name = form.cleaned_data.get('last_name')
            orders.o_email = form.cleaned_data.get('email')
            orders.address = form.cleaned_data.get('address')
            orders.status = True
            orders.save()
        return render(self.request,'store/thank-you.html')

class OrdersView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = OrderModel.objects.filter(user=self.request.user, status=True)
            context = {
                'object': order
            }
            return render(self.request, 'store/orders.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("/store")

class RegisterBuyerView(CreateView):
    model = User
    form_class = BuyerForm
    template_name = 'store/register_user.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if form.is_valid():
            if user.user_type == 2:
                login(request,user)
                return redirect("home")
        else:
            return redirect("login")
    else:
        form = AuthenticationForm()
        return render(request, "store/login.html", {"form":form})

def logout_user(request):
    logout(request)
    return redirect('home')


@login_required
def add_to_cart(request, slug):
    product = get_object_or_404(ProductModel, slug=slug)
    order_item, created = OrderModel.objects.get_or_create(
        product=product,
        user=request.user,
        status=False
    )
    order_qs = OrderModel.objects.filter(
        user = request.user,
        status=False,
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.quantity==1:
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("cart")
        else:
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("cart")
    return redirect("home")

@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(ProductModel, slug=slug)
    order_qs = OrderModel.objects.filter(
        user=request.user,
        status=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if OrderModel.objects.filter(product__slug=item.slug).exists():
            order_item = OrderModel.objects.filter(
                product=item,
                user=request.user,
                status=False
            )[0]
            #order.product_id.remove(order_item)
            order_item.delete()
            messages.info(request, "This item was removed from your cart.")
            return redirect("cart")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("product", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("product", slug=slug)
