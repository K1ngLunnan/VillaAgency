import django_filters
from .models import House


class HouseFilter(django_filters.FilterSet):
    price_gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price_lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')

    class Meta:
        model = House
        fields = (
            'category',
            'address',
            'region',
            'area',
            'floor',
            'bedroom',
            'bathroom',
            'parking_lot',
            'is_security',
            'authorization_type',
            'payment_method',
        )