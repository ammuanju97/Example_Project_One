from .models import UserRegister, SignUpModel
from django import forms
from django.core.validators import RegexValidator
import re
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.hashers import make_password

EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"


# defining form class
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        # model name using this model form is made
        model = UserRegister
        # custom fields
        fields = "__all__"

    def clean_fullname(self):
        fullname = self.cleaned_data["fullname"]
        if len(fullname) < 4:
            raise forms.ValidationError("full name must be 4 letters")
        return fullname

    def clean_username(self):
        username = self.cleaned_data["username"]
        if len(username) < 5:
            raise forms.ValidationError("user name must be 5 letters")
        return username

    def clean_email(self):
        email = self.cleaned_data["email"]
        if not re.match(EMAIL_REGEX, email):
            raise forms.ValidationError("Invalid email format")
        return email

    def clean_password(self):
        password = self.cleaned_data["password"]
        if len(password) < 4:
            raise forms.ValidationError("password must be 4 letters")
        return password


class UserLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserRegister
        fields = ["username", "password"]


class SignUpForm(UserCreationForm):
    """
    user register form using signup model"""

    class Meta:
        model = SignUpModel
        # fields = '__all__'
        fields = [
            "fullname",
            "username",
            "email",
            "address1",
            "address2",
            "city",
            "state",
            "pin_code",
        ]


class UserSignUpViewForm(forms.ModelForm):
    """
    user signup form
    """

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = SignUpModel
        # fields = '__all__'
        fields = [
            "fullname",
            "username",
            "email",
            "password",
            "address1",
            "address2",
            "city",
            "state",
            "pin_code",
        ]
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password:
            # hash the password using Django's make_password function
            password = make_password(password)
        return password

class UserLoginViewForm(forms.Form):
    """
    user login using abstract user
    """

    username = forms.CharField(label="Your name", max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class UserSignInForm(AuthenticationForm):
    class Meta:
        model = SignUpModel
        # fields = '__all__'
        fields = ["username", "password"]
