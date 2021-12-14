from django.http import JsonResponse
from django.db.models import QuerySet
from django.db import models


def get_url_parameter(request, registered_parameters):
    for el in registered_parameters:
        if request.GET.get(el, None):
            return el, request.GET.get(el, None)


def dt_formatter(data):
    if isinstance(data, dict):
        data['created_at'] = data['created_at'].strftime("%d/%m/%Y")
        data['updated_at'] = data['updated_at'].strftime("%d/%m/%Y %H:%M:%S")

        return data


def send_data_as_json(data):
    response_data = None
    status = None
    if isinstance(data, models.Model):
        response_data = dt_formatter(data.to_dict())

    if isinstance(data, QuerySet):
        response_data = {
            'drivers' : list(map(dt_formatter, data))
        }

    if isinstance(data, tuple):
        response_data = {
            'message': data[0]
        }
        status = data[1]

    return JsonResponse(response_data, status=status) if status else JsonResponse(response_data)