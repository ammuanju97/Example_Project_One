from django.urls import path
from .views import (
    Home,
    Signup,
    SignUpView,
    LoginPage,
    LoginPgaeFormView,
    UserRegistrationView,
    UserSignUpView,
    UserLoginView,
    UserSignInView,
    LogoutPageView,
)

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("signup/", Signup.as_view(), name="signup"),
    path("signup1/", SignUpView.as_view(), name="signup-one"),
    path("signup3/", UserRegistrationView.as_view(), name="signup-three"),
    path("signup4/", UserSignUpView.as_view(), name="signup4"),
    path("loginpage/", LoginPage.as_view(), name="loginpage"),
    path("loginpage-view/", LoginPgaeFormView.as_view(), name="login-one"),
    path("login3/", UserLoginView.as_view(), name="login3"),
    path("login4/", UserSignInView.as_view(), name="login4"),
    path("logout/", LogoutPageView.as_view(), name="logout"),
]
