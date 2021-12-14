import json


class ViewHelpers:

    @staticmethod
    def get_url_parameter(request, parameters):
        pass

    @staticmethod
    def handle_get_request(request, model_processed, specific_id=None):

        if specific_id:
            try:
                data = model_processed.objects.get(pk=specific_id)
            except:
                data = ('Not found', 404)

        else:
            data = model_processed.objects.values()

        return data

    @staticmethod
    def handle_post_request(request, model_processed):
        print(json.loads(request.body))
        try:
            model_instance = model_processed(**json.loads(request.body))
            model_instance.full_clean()
            model_instance.save()
            data = ('Created successfully', 201)
        except:
            data = ('Bad request', 400)

        return data

    @staticmethod
    def handle_put_request(request, model_processed, specific_id=None):

        if model_processed.objects.filter(pk=specific_id).exists():
            try:
                model_processed.objects.filter(pk=specific_id).update(**json.loads(request.body))
                model_processed.objects.get(pk=specific_id).save()
                data = ('Updated successfully', 200)
            except:
                data = ('Bad request', 400)
        else:
            try:
                model_processed.objects.create(pk=specific_id, **json.loads(request.body))
                data = ('Created successfully', 201)
            except:
                data = ('Bad request', 400)

        return data

    @staticmethod
    def handle_delete_request(request, model_processed, specific_id=None):

        if model_processed.objects.filter(pk=specific_id).exists():
            model_instance = model_processed.objects.get(id=specific_id)
            model_instance.delete()
            data = ('Deleted successfully', 200)
        else:
            data = ('Not found', 404)

        return data
