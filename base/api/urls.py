from django.urls import path
from . import views
urlpatterns=[
    path('',views.routes),
    path('productos/',views.productos),
    path('producto/<int:id>',views.producto)
    
]