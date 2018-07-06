from rest_framework import viewsets

from .models import FreeFairModels
from .serializers import FreeFairModelsSerializer
from .filtersapi import FreeFairModelsFilter


class FreeFairApiView(viewsets.ModelViewSet):
    queryset = FreeFairModels.objects.all()
    serializer_class = FreeFairModelsSerializer
    filter_class = FreeFairModelsFilter
