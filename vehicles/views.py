import json

from .models import Vehicle
from drivers.models import Driver
from django.views.decorators.csrf import csrf_exempt

from common_functional.handlers import ViewHelpers as _ViewHelpers
from common_functional.helpers import send_data_as_json, get_url_parameter


registered_parameters = [
    'with_drivers',
]


class ViewHelpers(_ViewHelpers):

    @staticmethod
    def set_or_unset_driver(request, specific_vehicle_id, model_processed):
        try:
            vehicle = model_processed.objects.get(pk=specific_vehicle_id)
            data = json.loads(request.body)

            if not vehicle.driver:
                if not Driver.objects.filter(**data).exists():
                    ViewHelpers.handle_post_request(request, Driver)
                driver_to_be_set = Driver.objects.get(**data)
                if not model_processed.objects.filter(driver=driver_to_be_set):
                    vehicle.driver = driver_to_be_set
                    vehicle.save()
                    data = ('Driver successfully set', 200)
                else:
                    data = ('Driver unavailable', 404)
            else:
                vehicle.driver = None
                vehicle.save()
                data = ('Driver successfully unset', 200)
        except:
            data = ('Not found', 404)

        return data

    @staticmethod
    def handle_get_request(request, model_processed, specific_driver_id):
        data = _ViewHelpers.handle_get_request(request, model_processed, specific_driver_id)

        url_param = get_url_parameter(request, registered_parameters)
        if url_param:
            value = url_param[1]

            if value == 'yes':
                data = model_processed.objects.filter(driver__isnull=False).values()
            elif value == 'no':
                data = model_processed.objects.filter(driver__isnull=True).values()

        return data


@csrf_exempt
def handle_vehicles(request, specific_vehicle_id=None):

    model_processed = Vehicle

    if request.method == 'GET':
        data = ViewHelpers.handle_get_request(request, model_processed, specific_vehicle_id)

    elif request.method == 'POST' and not specific_vehicle_id:
        data = ViewHelpers.handle_post_request(request, model_processed)

    elif request.method == 'POST' and specific_vehicle_id:
        data = ViewHelpers.set_or_unset_driver(request, specific_vehicle_id, model_processed)

    elif request.method == 'PUT' and specific_vehicle_id:
        data = ViewHelpers.handle_put_request(request, model_processed, specific_vehicle_id)

    elif request.method == 'DELETE' and specific_vehicle_id:
        data = ViewHelpers.handle_delete_request(request, model_processed, specific_vehicle_id)

    return send_data_as_json(data)