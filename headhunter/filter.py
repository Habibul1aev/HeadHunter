from random import choice

import django_filters
from django.forms import TextInput, NumberInput, Select
from headhunter.models import Work, Country, Category, City


class SearchWork(django_filters.FilterSet):
    class Meta:
        model = Work
        fields = ['name', 'category',]


# class SearchCountry(django_filters.FilterSet):
#     countries = django_filters.CharFilter(lookup_expr='icontains', label='Поиск по странам')
#
#     class Meta:
#         model = Country
#         fields = ['countries',]


class Filter(django_filters.FilterSet):
    category = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        label='Категория',
        widget=Select(attrs={'class': 'form-select'})
    )
    from_price = django_filters.NumberFilter(
        field_name='from_price', lookup_expr='gte', label='Минимальная цена',
        widget=NumberInput(attrs={'placeholder': 'Минимальная цена', 'class': 'form-input'})
    )
    city = django_filters.ModelChoiceFilter(
        queryset=City.objects.all(),
        label='Город',
        widget=Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Work
        fields = ('category', 'from_price', 'city', 'education', 'test', 'employment', 'graphic', 'time', 'format')