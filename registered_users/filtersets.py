import django_filters
from registered_users.models import (
    AppUser,
    UserDocument,
    ContactInfo,
)


class AppUserFilterSet(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    username = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    is_militar = django_filters.BooleanFilter()
    is_temporal = django_filters.BooleanFilter()

    class Meta:
        model = AppUser
        fields = ['name', 'last_name', 'username', 'email', 'is_militar', 'is_temporal']


class UserDocumentFilterSet(django_filters.FilterSet):
    document = django_filters.CharFilter(lookup_expr='icontains')
    type_document__name_type_document = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = UserDocument
        fields = ['document', 'type_document__name_type_document']


class ContactInfoFilterSet(django_filters.FilterSet):
    city = django_filters.CharFilter(lookup_expr='icontains')
    phone = django_filters.CharFilter(lookup_expr='icontains')
    cel_phone = django_filters.CharFilter(lookup_expr='icontains')
    emergency_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = ContactInfo
        fields = ['city', 'phone', 'cel_phone', 'emergency_name']
