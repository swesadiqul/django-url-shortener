from django.urls import path
from .views import *

urlpatterns = [
    path('', urlShort, name='home'),
    path("u/<str:slug>", urlRedirect, name="redirect")

]
