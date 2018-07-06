import rest_framework_filters as filters

from .models import FreeFairModels


class FreeFairModelsFilter(filters.FilterSet):
    district = filters.AllLookupsFilter(name='district')
    region_five = filters.AllLookupsFilter(name='region_five')
    name_fair = filters.AllLookupsFilter(name='name_fair')
    neighborhood = filters.AllLookupsFilter(name='neighborhood')

    class Meta:
        model = FreeFairModels
        exclude = ('created', 'modified')
