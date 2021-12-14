from django.urls import path
from .views import handle_drivers


urlpatterns = [
    path('driver/', handle_drivers),
    path('driver/<int:specific_driver_id>/', handle_drivers),
]