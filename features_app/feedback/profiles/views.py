from django.forms import fields
from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView

from .forms import ProfileForm
from .models import UserProfile
# Create your views here.
'''
def store_files(file):
    with open("/home/rahul/Visualstudio/features_app/temp/image.png", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)

'''
class CreateProfileView(CreateView):
    model= UserProfile
    #form_class = ProfileForm
    template_name = "profiles/create_profile.html"
    fields = "__all__"
    success_url = "/profiles"

class ProfileView(ListView):
    model = UserProfile
    template_name = "profiles/userprofile.html"
    context_object_name = "profiles"



'''class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, "profiles/create_profile.html",{
            "form": form
        })

    def post(self, request):
        submitted_form = ProfileForm(request.POST, request.FILES)

        if submitted_form.is_valid():
            profile = UserProfile(image=request.FILES['user_image'])
            profile.save()
            return HttpResponseRedirect("/profiles")

        return render(request, "profiles/create_profile.html",{
            "form": submitted_form
        })'''