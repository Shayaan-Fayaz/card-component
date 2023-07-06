from django.urls import path
from . import views

urlpatterns = [
    path("", views.CardPageView.as_view())
]