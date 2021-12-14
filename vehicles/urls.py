from django.urls import path
from .views import handle_vehicles


urlpatterns = [
    path('vehicle/', handle_vehicles),
    path('vehicle/<int:specific_vehicle_id>/', handle_vehicles),
    path('set_driver/<int:specific_vehicle_id>/', handle_vehicles),
]