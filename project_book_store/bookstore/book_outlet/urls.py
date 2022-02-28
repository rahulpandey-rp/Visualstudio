from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("register", views.register_request, name="register"),
    path("<slug:slug>", views.book_detail, name="book-detail")
]