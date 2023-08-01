from . import views
from django.urls import path

urlpatterns = [
    path("", views.init_meals, name="meals"),
]
