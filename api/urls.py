""" route definitions for api app """
from django.urls import path

from .views import BookAPIView

urlpatterns = [
    path('', BookAPIView.as_view())
]
