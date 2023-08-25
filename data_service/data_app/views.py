from rest_framework import viewsets
from .models import DataModel
from .serializers import DataModelSerializer


class DataModelViewSet(viewsets.ModelViewSet):
    queryset = DataModel.objects.all()
    serializer_class = DataModelSerializer
