from django.urls import path
from .views import UserProfile, UserHome,EditProfile, ChangePasswordView, AddPostView,PostDisplayView

urlpatterns = [
    path('user-home/', UserHome.as_view(), name='user_home'),
    path('view-profile/', UserProfile.as_view(), name='view-profile'),
    path('edit-profile/', EditProfile.as_view(), name='edit-profile'),
    path('change-password/', ChangePasswordView.as_view() ,name='change_password'),
    path('add-post/', AddPostView.as_view(), name='add_post'),
    path('view-post/',PostDisplayView.as_view(), name='view_post'),
]