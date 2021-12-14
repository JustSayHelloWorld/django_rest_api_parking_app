from django.db import models

from drivers.models import Driver


class Vehicle(models.Model):

    driver = models.ForeignKey(Driver, blank=True, null=True, on_delete=models.SET_NULL)
    make = models.CharField(max_length=20, editable=False)
    model = models.CharField(max_length=20, editable=False)
    plate_number = models.CharField(blank=False, max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def to_dict(self):

        return {
            'id': self.id,
            'driver_id': self.driver,
            'make': self.make,
            'model': self.model,
            'plate_number': self.plate_number,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }