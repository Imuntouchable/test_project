from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .db import db
from .utils import determine_field_type


class FormValidationViewSet(ViewSet):
    """Проверка данных на соответствие шаблонов в базе данных."""
    def create(self, request):
        data = request.data
        field_types = {key: determine_field_type(value)
                       for key, value in data[0].items()
                       }
        templates = db.all()
        for template in templates:
            if all(field in field_types
                   and field_types[field] == template[field]
                   for field in template if "name" not in field
                   ):
                return Response({"template_name": template["name"]})
        return Response(field_types, status=status.HTTP_404_NOT_FOUND)
