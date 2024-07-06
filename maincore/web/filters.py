import django_filters
from .models import SimpleModel


class MonthFilter(django_filters.FilterSet):
    create_time = django_filters.NumberFilter(field_name='create_time', lookup_expr='month')

    class Meta:
        model = SimpleModel
        fields = ('create_time', )