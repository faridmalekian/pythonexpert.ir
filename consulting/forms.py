import re

from django import forms
from django.core.validators import RegexValidator
from .models import Consulting

class RegisterForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "نام خود را وارد کنید..."}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': "form-control", 'placeholder': "ایمیل شما..."}))
    tel = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "شماره تماس شما..."}))
    add = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "ادرس شما..."}))

    def clean_tel(self):

        tel = self.cleaned_data["tel"]
        consulting_number = Consulting.objects.filter(tel=tel)

        if not re.match(r"^09[0-9]{9}",tel):
            raise forms.ValidationError("شماره وارد شده معتبر نیست...")
        else:
            if consulting_number:
                raise forms.ValidationError("این شماره قبلا استفاده شده است...")
            else:
                return tel

