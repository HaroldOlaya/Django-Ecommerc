from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home),
    path('login/',views.login),
    path('crear/',views.crear),
    path('productos/',views.productos)
]
