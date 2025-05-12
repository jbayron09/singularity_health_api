from graphene import relay
from graphene_django import DjangoObjectType

from registered_users.models import (
    AppUser,
    UserDocument,
    TypeDocument,
    ContactInfo,
    Country
)

from registered_users.filtersets import (
    CountryFilterSet,
    AppUserFilterSet,
    UserDocumentFilterSet,
    ContactInfoFilterSet,
    TypeDocumentFilterSet
)


class TypeDocumentNode(DjangoObjectType):
    class Meta:
        model = TypeDocument
        filterset_class = TypeDocumentFilterSet
        interfaces = (relay.Node,)


class CountryNode(DjangoObjectType):
    class Meta:
        model = Country
        filterset_class = CountryFilterSet
        interfaces = (relay.Node,)


class AppUserNode(DjangoObjectType):
    class Meta:
        model = AppUser
        exclude = ("password", "verification_token", "email_verified")
        filterset_class = AppUserFilterSet
        interfaces = (relay.Node,)


class UserDocumentNode(DjangoObjectType):
    class Meta:
        model = UserDocument
        filterset_class = UserDocumentFilterSet
        interfaces = (relay.Node,)


class ContactInfoNode(DjangoObjectType):
    class Meta:
        model = ContactInfo
        filterset_class = ContactInfoFilterSet
        interfaces = (relay.Node,)
