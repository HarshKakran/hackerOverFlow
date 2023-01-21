from django.urls import path
from .views import UserDetailAPI, RegisterUserAPIView, ResumeListCreateView

urlpatterns = [
    path("get-user/", UserDetailAPI.as_view()),
    path('register/', RegisterUserAPIView.as_view()),
    path('resume/', ResumeListCreateView.as_view())
]