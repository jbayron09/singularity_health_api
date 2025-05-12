from django_filters import FilterSet
from registered_users.models import (
    AppUser,
    UserDocument,
    ContactInfo,
    Country,
    TypeDocument
)


class TypeDocumentFilterSet(FilterSet):
    class Meta:
        model = TypeDocument
        fields = {
            "name_type_document": ["exact", "icontains"]
        }


class CountryFilterSet(FilterSet):
    class Meta:
        model = Country
        fields = {
            "country_name": ["exact", "icontains"]
        }


class AppUserFilterSet(FilterSet):
    class Meta:
        model = AppUser
        fields = {
            "username": ["exact", "icontains"]
        }


class UserDocumentFilterSet(FilterSet):
    class Meta:
        model = UserDocument
        fields = {
            "document": ["exact", "icontains"]
        }


class ContactInfoFilterSet(FilterSet):
    class Meta:
        model = ContactInfo
        fields = {
            "phone": ["exact", "icontains"]
        }
