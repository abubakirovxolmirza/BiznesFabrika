from django.urls import path
from .views import RegisterUserView, ListUsersView, CustomUserDetailView

urlpatterns = [
    path('register', RegisterUserView.as_view()),
    path('users', ListUsersView.as_view()),
    path('users/<int:pk>', CustomUserDetailView.as_view())
]
