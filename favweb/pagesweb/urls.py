from django.urls import path
from pagesweb import views

urlpatterns = [
    path("", views.home, name='home'),
]
