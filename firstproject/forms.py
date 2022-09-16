import email
from django import forms

class FormFeedback(forms.Form):
    title = forms.CharField(label='Title',min_length=1, max_length=50,widget=forms.TextInput)
    subject = forms.CharField(label='Subject',min_length=1, max_length=200,widget=forms.Textarea)
    email = forms.CharField(label='email ',min_length=1, max_length=200,widget=forms.Textarea)
    