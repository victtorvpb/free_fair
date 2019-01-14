import pandas
from django.db import transaction
from django.core.management.base import BaseCommand


from apps.api_free_fair.models import FreeFairModels


class Command(BaseCommand):
    help = 'Fetch update billing, will run all the files'

    def add_arguments(self, parser):
        parser.add_argument('--file_path', nargs="*", dest="file_path", type=str)

    def handle(self, *args, **options):
        if options['file_path']:
            file_path = options['file_path']
        else:
            return

        self.insert_csv_to_databse(file_path)

    @transaction.atomic
    def insert_csv_to_databse(file_path='DEINFO_AB_FEIRASLIVRES_2014.csv'):
        file_data_frame = pandas.read_csv(file_path, delimiter=',', skiprows=0)

        for index, row in file_data_frame.iterrows():
            print(row)
            FreeFairModels.objects.create(
                id_file=row.get('ID'),
                longitude=row.get('LONG'),
                latitude=row.get('LAT'),
                setcens=row.get('SETCENS'),
                areap=row.get('AREAP'),
                coddist=row.get('CODDIST'),
                district=row.get('DISTRITO'),
                codsubpref=row.get('CODSUBPREF'),
                subpref=row.get('SUBPREFE'),
                region_five=row.get('REGIAO5'),
                region_eigth=row.get('REGIAO8'),
                name_fair=row.get('NOME_FEIRA'),
                register=row.get('REGISTRO'),
                address=row.get('LOGRADOURO'),
                number=row.get('NUMERO'),
                neighborhood=row.get('BAIRRO'),
                reference_point=row.get('REFERENCIA'),
            )
