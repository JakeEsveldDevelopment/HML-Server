from django.urls import path, include
from django.conf.urls import include

from hml import api

urlpatterns = [
    path('user/', api.getUser)
]