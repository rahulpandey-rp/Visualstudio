from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string         
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
    "october": None,
    "november": "nov",
    "december": "dec"
}

def view_months_index(request):
    list_items = ""
    months = list(month_dict.keys())
    
    return render(request, "challenges/index.html",{
        "months_list": months
    })

def month_by_no(request, month):
    months_no = list(month_dict.keys())
    if month > len(months_no):
        return HttpResponseNotFound("Invalid Address")
    redirect_month = months_no[month - 1]
    redirect_url = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_url)


def monthly_task(request, month):
    try:
        message = month_dict[month]
        return render(request, "challenges/challenge.html", {
            "month": month,
            "msg": message
        })
    except:
        raise Http404()
