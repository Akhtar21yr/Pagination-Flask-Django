from django.urls import path
from .views import StudentView

urlpatterns = [
    path('students/', StudentView.as_view(), name='student-list'),
    path('students/<int:rollno>/', StudentView.as_view(), name='student-detail'),
]
