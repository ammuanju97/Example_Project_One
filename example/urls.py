from django.urls import path
from . views import MyView, Greetings

urlpatterns = [
    path('about/', MyView.as_view(), name='about'),
    path('greet/', Greetings.as_view(), name='greet'),
]