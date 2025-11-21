import django_filters

from headhunter.models import Work


class FilterWork(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(lookup_expr='gte', field_name='from_price')
    max_price = django_filters.NumberFilter(lookup_expr='lte', field_name='to_price')

    class Meta:
        model = Work
        fields = {
            'category',
            'skill',
            'city',
            'is_publish'
        }