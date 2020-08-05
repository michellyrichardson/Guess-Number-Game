from django.urls import path
from . import views

urlpatterns = [
    path('', views.numbergame),
    path('decision', views.decision),
    path('reset', views.reset),
]