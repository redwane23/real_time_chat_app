import django_filters
from home.models import Room
from django.contrib.auth.models import User

class RoomsFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(field_name="name", lookup_expr="istartswith")

    class Meta:
        model = Room
        fields = ["search"]


class UsersFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(field_name="username", lookup_expr="istartswith")

    class Meta:
        model = User
        fields = ["search"]