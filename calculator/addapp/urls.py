from django.urls import path
from addapp import views

urlpatterns = [
    path('',views.index),
    path('calculator',views.calculator),
]
