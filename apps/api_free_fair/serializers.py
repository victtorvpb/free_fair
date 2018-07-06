from rest_framework import serializers

from .models import FreeFairModels


class FreeFairModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeFairModels
        exclude = ('created', 'modified')
        read_only_fields = ('register', 'id')
