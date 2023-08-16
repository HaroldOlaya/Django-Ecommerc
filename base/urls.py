from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home),
    path('ejemplo/',views.ejemplo)
]
