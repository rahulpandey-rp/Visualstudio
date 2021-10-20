from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

month_dict = {
    "january": "january",
    "february": "feb",
    "march": "mar",
    "april": "apr",
    "may": "may",
    "june": "jun",
    "july": "july",
    "august": "My birthday month",
    "september": "sep",
    "october": "Birthday on 23rd",
    "november": "nov",
    "december": "dec"
}

def view_months_index(request):
    list_items = ""
    months = list(month_dict.keys())
    for month in months:
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href='{month_path}'>{month}</a></li>"
    return HttpResponse(f"<ol>{list_items}</ol>")

def month_by_no(request, month):
    months_no = list(month_dict.keys())
    if month > len(months_no):
        return HttpResponseNotFound("Invalid Address")
    redirect_month = months_no[month - 1]
    redirect_url = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_url)


def monthly_task(request, month):
    try:
        msg = month_dict[month]
        html_msg = f"<h2>{msg}</h2>"
    except:
        return HttpResponseNotFound("This is invalid address")
    else:
        return HttpResponse(html_msg)
