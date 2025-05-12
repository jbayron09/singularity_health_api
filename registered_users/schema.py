from graphene import ObjectType, relay
from graphene_django.filter import DjangoFilterConnectionField

from registered_users.nodes import (
    AppUserNode,
    UserDocumentNode,
    ContactInfoNode,
    CountryNode,
    TypeDocumentNode
)

from registered_users.mutations import RegisterUser


class Query(ObjectType):
    app_user = relay.Node.Field(AppUserNode)
    app_users = DjangoFilterConnectionField(AppUserNode)

    user_document = relay.Node.Field(UserDocumentNode)
    user_documents = DjangoFilterConnectionField(UserDocumentNode)

    contact_info = relay.Node.Field(ContactInfoNode)
    contact_infos = DjangoFilterConnectionField(ContactInfoNode)

    country = relay.Node.Field(CountryNode)
    countries = DjangoFilterConnectionField(CountryNode)

    type_document = relay.Node.Field(TypeDocumentNode)
    type_documents = DjangoFilterConnectionField(TypeDocumentNode)


class Mutation(ObjectType):
    register_user = RegisterUser.Field()
