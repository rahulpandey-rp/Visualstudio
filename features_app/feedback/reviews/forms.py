from django import forms
from django.forms import fields

from .models import Review
'''
class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your Name", max_length=100, error_messages={
        "required":"Your name must not be empty",
        "max_length": "Please enter a shorter number"
    })
    review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
    rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)
'''

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        #fields = ['user_name', 'review_text', 'rating']
        # exclude = ['owner_comment'] to exclude unwanted out of all
        fields = '__all__'
        labels = {
            "user_name": "Your Name",
            "review_text": "Your Review",
            "rating": "Your Rating"
        }
        error_messages = {
            "user_name":{
                "required":"Your name must not be empty!",
                "max_length": "Please enter a shorter number"
            }
        }