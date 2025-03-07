from home.views import index
from home.views import person
from django.urls import path

urlpatterns = [
    path('index/', index),
    path('people',person)
]
