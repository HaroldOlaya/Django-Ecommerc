from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home),
    path('login/',views.loginPage),
    path('crear/',views.crear),
    path('crear/<int:id>',views.crear),
    path('productos/',views.productos)
]
