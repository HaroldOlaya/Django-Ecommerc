from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home),
    path('logout/',views.logoutPage),
    path('login/',views.loginPage),
    path('crear/',views.crear),
    path('registro/',views.registro),
    path('crear/<int:id>',views.crear),
    path('productos/',views.productos),
    path('apii/',views.api)
    
    
]
