from django.urls import path
from .views import RegisterUserView, ListUsersView, CustomUserDetailView, CustomTokenObtainPairView, GroupDetailView, ListGroupView

urlpatterns = [
    path('register', RegisterUserView.as_view()),
    path('users', ListUsersView.as_view()),
    path('users/<int:pk>', CustomUserDetailView.as_view()),
    path('login', CustomTokenObtainPairView.as_view()),
    path('group', ListGroupView.as_view()),
    path('group/<int:pk>', GroupDetailView.as_view()),
]
