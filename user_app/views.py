from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, CreateView
from core.models import SignUpModel
from .forms import EditProfileForm, ChangePasswordForm, AddPostForm
from django.contrib.auth import authenticate
from .models import PostCategory, AddPost
from django.urls import reverse_lazy

# Create your views here.
class UserHome(TemplateView):
    template_name = "user_app/userhome.html"


class UserProfile(View):
    """
    view user profile
    """

    def get(self, request):
        user_details = SignUpModel.objects.get(username=request.user)
        return render(
            request, "user_app/view_profile.html", {"user_details": user_details}
        )


class EditProfile(View):
    """
    edit user profile
    """

    def get(self, request):
        user_details = SignUpModel.objects.get(username=request.user)
        form = EditProfileForm(instance=user_details)
        return render(request, "user_app/edit_profile.html", {"form": form})

    def post(self, request):
        user_details = SignUpModel.objects.get(username=request.user)
        form = EditProfileForm(request.POST, instance=user_details)

        if form.is_valid():
            form.save()
            return redirect("user_home")
        return render(request, "user_app/edit_profile.html", {"form": form})


class ChangePasswordView(View):
    """
    change user passord with new one
    """

    def get(self, request):
        form = ChangePasswordForm()
        return render(request, "user_app/change_password.html", {"form": form})

    def post(self, request):
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data["new_password"]
            username = request.user
            password = form.cleaned_data["current_password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                user.set_password(new_password)
                user.save()
                return redirect("login4")
            return render(request, "user_app/change_password.html", {"form": form})


class AddPostView(CreateView):
    """
    Add multiple post to a user
    """

    model = AddPost
    form_class = AddPostForm
    template_name = "user_activity/add_post.html"
    success_url = reverse_lazy("user_home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostDisplayView(View):
    """
    display the user added post
    """

    def get(self, request):
        post_details = AddPost.objects.filter(user=request.user)
        return render(
            request, "user_activity/view_post.html", {"post_details": post_details}
        )


class EditPOst(View):
    pass