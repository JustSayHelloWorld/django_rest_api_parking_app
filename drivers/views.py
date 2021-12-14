import re
from datetime import datetime

from .models import Driver
from django.views.decorators.csrf import csrf_exempt

from common_functional.handlers import ViewHelpers as _ViewHelpers
from common_functional.helpers import send_data_as_json, get_url_parameter


date_pattern = r'((?:0?[1-9]|[12][0-9]|3[01])-(?:0?[1-9]|1[0-2])-(?:19[0-9][0-9]|20[0-9][0-9]))'
how_pattern = r'(lte|gte)'

registered_parameters = [
    'created_at__gte',
    'created_at__lte'
]


class ViewHelpers(_ViewHelpers):

    @staticmethod
    def handle_get_request(request, model_processed, specific_driver_id):
        data = _ViewHelpers.handle_get_request(request, model_processed, specific_driver_id)

        url_param = get_url_parameter(request, registered_parameters)
        if url_param:
            how = re.findall(how_pattern, url_param[0])[0]
            date = re.findall(date_pattern, url_param[1])[0]
            date_converted = datetime.strptime(date, '%d-%m-%Y')

            if how == 'lte':
                data = model_processed.objects.filter(created_at__lte=date_converted).values()
            else:
                data = model_processed.objects.filter(created_at__gte=date_converted).values()

        return data


@csrf_exempt
def handle_drivers(request, specific_driver_id=None):

    model_processed = Driver

    if request.method == 'GET':
        data = ViewHelpers.handle_get_request(request, model_processed, specific_driver_id)

    elif request.method == 'POST' and not specific_driver_id:
        data = ViewHelpers.handle_post_request(request, model_processed)

    elif request.method == 'PUT' and specific_driver_id:
        data = ViewHelpers.handle_put_request(request, model_processed, specific_driver_id)

    elif request.method == 'DELETE' and specific_driver_id:
        data = ViewHelpers.handle_delete_request(request, model_processed, specific_driver_id)

    return send_data_as_json(data)

