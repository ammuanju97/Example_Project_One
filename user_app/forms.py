from django import forms
from core.models import SignUpModel
from .models import PostCategory, AddPost


class EditProfileForm(forms.ModelForm):
    """
    edit user profile
    """

    class Meta:

        model = SignUpModel
        # fields = "__all__"
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


class ChangePasswordForm(forms.Form):
    """
    change user password, update existing password with new password
    """

    current_password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)
    confirm_new_password = forms.CharField(widget=forms.PasswordInput)


class AddPostForm(forms.ModelForm):
    
    class Meta:
        model=AddPost
        fields = [
            "post_name",
                  "content",
                  "category",
                  "image"
        ]
          