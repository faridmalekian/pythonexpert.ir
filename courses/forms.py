from .models import Comment
from django import forms


class CommentForm(forms.Form):
    # name = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control" ,'placeholder':"نام خود را وارد کنید..."}))
    # email =  forms.EmailField(widget=forms.EmailInput(attrs={'class':"form-control" ,'placeholder':"ایمیل شما..."}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class':"form-control" ,'placeholder':"نظرات شما..."}))
