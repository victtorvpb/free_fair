from django.test import TestCase
from apps.api_free_fair.models import FreeFairModels
from annoying.functions import get_object_or_None


class TestsFreeFairModel(TestCase):

    def setUp(self):
        self.insert_free_fair = FreeFairModels.objects.create(id_file=1,
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
                                                              reference_point='TV RUA PRETORIA')

    def test_insert_free_fair(self):
        free_fair_get = FreeFairModels.objects.get(id_file = 1)
        self.assertEqual(self.insert_free_fair,free_fair_get )
    
    def test_edit_region_five_free_fair(self):
        self.insert_free_fair.region_five = 'Oeste'
        self.insert_free_fair.save()

        free_fair_insert = FreeFairModels.objects.get(id_file = 1)

        self.assertEqual(free_fair_insert.region_five, 'Oeste')
    
    def test_delete_free_fair(self):
        self.insert_free_fair.delete()
        delete_free_fair = get_object_or_None(FreeFairModels,id_file = 1 )

        self.assertEqual(delete_free_fair, None)
