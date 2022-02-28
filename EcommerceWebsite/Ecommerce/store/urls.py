from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomepageView.as_view() , name="home"),
    path('register_user', views.RegisterBuyerView.as_view() , name="register"),
    path('login_user', views.login_user, name="login"),
    path('logout_user', views.logout_user, name="logout"),
    path("path/<slug:slug>", views.ItemDetailView.as_view(), name= "product"),
    path("cart", views.OrderSummaryView.as_view(), name="cart"),
    path("orders", views.OrdersView.as_view(), name="orders"),
    path("profile", views.ProfileView.as_view(), name="profile"),
    path("checkout", views.CheckoutView.as_view(), name="checkout"),
    path('add-to-cart/<slug>/', views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', views.remove_from_cart, name='remove-from-cart'),
]
