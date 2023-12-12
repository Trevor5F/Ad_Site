import django_filters
from ads.models import Ad


class MyModelFilter(django_filters.rest_framework.FilterSet):
    # CharFilter — специальный фильтр, который позволяет искать совпадения в текстовых полях модели
    title = django_filters.CharFilter(field_name="title", lookup_expr="icontains", )

    class Meta:
        model = Ad
        fields = ("title",)
