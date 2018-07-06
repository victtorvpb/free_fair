from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from django.utils.http import urlencode

from apps.api_free_fair.serializers import FreeFairModelsSerializer
from apps.api_free_fair.models import FreeFairModels


class TestsFreeFairApi(TestCase):
    def setUp(self):
        self.insert_free_fair = FreeFairModels.objects.create(
            id_file=1,
            longitude=-46550164,
            latitude=-23558733,
            setcens=355030885000091,
            areap=3550308005040,
            coddist=87,
            district='VILA FORMOSA',
            codsubpref=26,
            subpref='ARICANDUVA-FORMOSA-CARRAO',
            region_five='Leste',
            region_eigth='Leste1',
            name_fair='VILA FORMOSA',
            register='4041-0',
            address='RUA MARAGOJIPE',
            number='S/N',
            neighborhood='VL FORMOSA',
            reference_point='TV RUA PRETORIA',
        )

    def test_get_api_free_fair_to_name(self):
        url = reverse('api_free_fair:FreeFair-list')

        query = urlencode({'name_fair': 'VILA FORMOSA'})

        url = '{}?{}'.format(url, query)

        response = self.client.get(url)
        free_fair = FreeFairModels.objects.filter(name_fair='VILA FORMOSA')
        serializer = FreeFairModelsSerializer(free_fair, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
