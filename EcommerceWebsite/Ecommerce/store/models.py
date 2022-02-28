from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'seller'),
        (2, 'buyer'),
        (3, 'admin'),
    )
    user_type = models.PositiveSmallIntegerField(default=3,choices=USER_TYPE_CHOICES)

class BuyerModel(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_no = models.CharField(max_length=15)



class SellerModel(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_no = models.CharField(max_length=15)


class CategoryModel(models.Model):
    type = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)


class ProductModel(models.Model):
    title = models.CharField(max_length=150)
    quantity = models.IntegerField(null=True)
    image = models.ImageField(upload_to="posts", null=True)
    slug = models.SlugField(unique=True, db_index=True)
    price = models.IntegerField()
    description = models.TextField(validators=[MinLengthValidator(10)])
    seller = models.ForeignKey(
        SellerModel, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(
        CategoryModel, null=True, on_delete=models.SET_NULL)
        

    def get_add_to_cart_url(self):
        return reverse("add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("remove-from-cart", kwargs={
            'slug': self.slug
        })

class AddressModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Address'
    
class OrderModel(models.Model):
    f_name = models.CharField(max_length=120, null=True)
    l_name = models.CharField(max_length=120, null=True)
    o_email = models.EmailField(null=True)
    order_date = models.DateField(auto_now=True)
    status = models.CharField(max_length=120)
    product = models.ForeignKey(ProductModel,default=None, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, null=True)
    def get_total_item_price(self):
        return self.quantity * self.product.price

    def get_total_discount_item_price(self):
        return self.quantity * self.product.price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.product.price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()

    def get_total(self):
        total = 0
        for order_item in OrderModel.objects.filter(status=False):
            total += order_item.get_final_price()
        return total

    def get_order_total(self):
        total = 0
        for order_item in OrderModel.objects.filter(status=True):
            total += order_item.get_final_price()
        return total
