from django.urls import path
from . import views
from .views import CreateVehicle, ListVehicle,DetailVehicle, UpdateVehicle
urlpatterns = [
    path('',ListVehicle.as_view(),name="navigation"),
    path('detailvehicle/<str:pk>',DetailVehicle.as_view(),name="detailvehicle"),
    path('addvehicle/',CreateVehicle.as_view(),name="createvehicle"),
    path('updatevehicle/<str:pk>',UpdateVehicle.as_view(),name="update_vehicle"),
]

