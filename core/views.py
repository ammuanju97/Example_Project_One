from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView, View
from .models import UserRegister
from .forms import (
    UserRegistrationForm,
    UserLoginForm,
    SignUpForm,
    UserSignUpViewForm,
    UserLoginViewForm,
    UserSignInForm,
)
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LogoutView

# Create your views here.


class Home(TemplateView):
    template_name = "core/home.html"


class Signup(View):
    """
    user registration using normal user register model and html form"""

    def get(self, request):
        return render(request, "core/signup.html")

    def post(self, request):
        fullname = request.POST["fullname"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        # confirm_password = request.POST['confirm_password']
        address = request.POST["address"]
        address2 = request.POST["address2"]
        city = request.POST["city"]
        state = request.POST["state"]
        zip = request.POST["zip"]
        user_register = UserRegister.objects.create(
            fullname=fullname,
            username=username,
            email=email,
            password=make_password(password),
            address1=address,
            address2=address2,
            city=city,
            state=state,
            pin_code=zip,
        )
        user_register.save()
        return render(request, "core/home.html")


class SignUpView(View):
    """
    User register using djnago forms"""

    def get(self, request):
        form = UserRegistrationForm()
        return render(request, "core/signup1.html", {"form": form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            sign_up = form.save()
            sign_up.password = make_password(form.cleaned_data["password"])
            sign_up.save()
            return render(request, "core/home.html", {"form": form})
        return render(request, "core/signup1.html", {"form": form})


class UserRegistrationView(CreateView):
    """
    signup using abstract user and createview"""

    form_class = SignUpForm
    success_url = reverse_lazy("loginpage")
    template_name = "core/signup3.html"


class UserSignUpView(View):
    """
    signup using view and absstactuser
    """

    def get(self, request):
        form = UserSignUpViewForm()
        return render(request, "core/signup4.html", {"form": form})

    def post(self, request):
        form = UserSignUpViewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login4')
        return render(request, "core/signup4.html", {"form": form})


class LoginPage(View):
    """
    user login using html form"""

    def get(self, request):
        return render(request, "core/loginpage.html")

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = UserRegister.objects.get(username=username)
        hash_password = user.password
        match_password = check_password(password, hash_password)
        if match_password:
            return render(request, "user_app/userhome.html", {"user": user})
        else:
            messages.error(request, "username or password not correct")
        return redirect("loginpage")


class LoginPgaeFormView(View):
    """
    user login using django forms"""

    def get(self, request):
        form = UserLoginForm()
        return render(request, "core/loginpage1.html", {"form": form})

    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = UserRegister.objects.get(username=username)
            hash_password = user.password
            match_password = check_password(password, hash_password)
            if match_password:
                return render(request, "user_app/userhome.html", {"user": user})
            else:
                messages.error(request, "username or password not correct")
            return redirect("login-one")
        return render(request, "core/loginpage1.html", {"form": form})


class UserLoginView(View):
    """
    user login using abstract user
    """

    def get(self, request):
        form = UserLoginViewForm()
        return render(request, "core/login3.html", {"form": form})

    def post(self, request):
        form = UserLoginViewForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            # print(username)
            # print(type(username))
            password = form.cleaned_data.get("password")
            # print(password)
            # print(type(password))

            user = authenticate(username=username, password=password)
            # print(user)
            if user is not None:
                login(request, user)
                return render(request, "user_app/userhome.html", {"form": form})
        messages.error(request, "username or password not correct")
        return render(request, "core/login3.html", {"form": form})


class UserSignInView(View):
    """
    login using authentication form
    """

    def get(self, request):
        form = UserSignInForm()
        return render(request, "core/login4.html", {"form": form})

    def post(self, request):
        form = UserSignInForm(request, data=request.POST)
        # print(request.POST)
        # print(form)
        if form.is_valid():
            # print("jj")
            username = form.cleaned_data.get("username")
            # print(username)
            password = form.cleaned_data.get("password")
            # print(password)
            user = authenticate(username=username, password=password)
            # print(user)
            if user is not None:
                login(request, user)
                return render(request, "user_app/userhome.html", {"form": form})
        return render(request, "core/login4.html", {"form": form})


class LogoutPageView(LogoutView):
    next_page = "home"
