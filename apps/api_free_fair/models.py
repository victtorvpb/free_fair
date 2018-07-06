from django_extensions.db.models import TimeStampedModel
from django.db import models


class FreeFairModels(TimeStampedModel):

    id_file = models.IntegerField(blank=False, unique=True, null=False)
    longitude = models.BigIntegerField(blank=False, null=False)
    latitude = models.BigIntegerField(blank=False, null=False)
    setcens = models.BigIntegerField(blank=False, null=False)
    areap = models.BigIntegerField(blank=False, null=False)
    coddist = models.IntegerField(blank=False, null=False)
    district = models.CharField(null=False, blank=False, max_length=50)
    codsubpref = models.IntegerField(blank=False, null=False)
    subpref = models.CharField(null=False, blank=False, max_length=100)
    region_five = models.CharField(null=False, blank=False, max_length=15)
    region_eigth = models.CharField(null=False, blank=False, max_length=15)
    name_fair = models.CharField(null=False, blank=False, max_length=100)
    register = models.CharField(null=False, blank=False, max_length=100, unique=True)
    address = models.CharField(null=False, blank=False, max_length=100)
    number = models.CharField(null=False, blank=False, max_length=10)
    neighborhood = models.CharField(null=False, blank=False, max_length=50)
    reference_point = models.CharField(null=False, blank=False, max_length=150)
