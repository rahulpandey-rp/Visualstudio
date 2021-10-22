from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_months_index, name= "index"),
    path("<int:month>", views.month_by_no, name="month-by-no"),
    path("<str:month>", views.monthly_task, name="month-challenge")
]
