from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name="index"),
    path("opportunity/<int:pk>/",  views.opportunity_detail, name="opportunity_detail"),
]