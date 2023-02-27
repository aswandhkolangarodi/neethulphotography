# Create web/urls.py and paste the following
from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "menucard"

urlpatterns = [
    path("<uid>/", views.index, name="index"),
]
