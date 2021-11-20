from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': "form-control", 'placeholder': "ایمیل شما..."})
    )

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control" ,'placeholder':"کلمه عبور..."}))

class RegisterForm(forms.Form):
    user_name = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control" ,'placeholder':"نام کاربری خود را وارد کنید..."}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control" ,'placeholder':"نام خود را وارد کنید..."}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control" ,'placeholder':"نام خانوادگی خود را وارد کنید..."}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':"form-control" ,'placeholder':"ایمیل شما..."}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control" ,'placeholder':"کلمه عبور..."}))
    re_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control" ,'placeholder':"تکرار کلمه عبور..."}))

    def clean_email(self):
        email = self.cleaned_data.get("email")

        is_exists_user_by_email = User.objects.filter(email=email).exists()

        if is_exists_user_by_email:
            raise forms.ValidationError("کاربری با این ایمیل قبلا ثبت نام کرده است")
        return email

    def clean_user_name(self):
        user_name = self.cleaned_data.get("user_name")

        is_exists_user_by_username = User.objects.filter(username=user_name).exists()

        if is_exists_user_by_username:
           raise forms.ValidationError("کاربری قبلا با این نام کاربری ثبت نام کرده است")

        return user_name



    def clean_re_password(self):
        password = self.cleaned_data.get("password")
        re_password = self.cleaned_data.get("re_password")

        if password != re_password:
            raise forms.ValidationError("کلمه های عبور مغایرت دارند")

        return re_password