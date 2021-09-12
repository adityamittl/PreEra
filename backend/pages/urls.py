from django.urls import path
from .views import *

urlpatterns = [
    path('dinos', dianos),
    path('stoneage', stoneage),
    path('', homepage),
]
