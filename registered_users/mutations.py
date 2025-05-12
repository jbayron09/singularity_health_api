from graphene import relay, Field, String, Boolean, Date
from graphql import GraphQLError
from registered_users.models import AppUser, UserDocument, ContactInfo, Country, TypeDocument
from registered_users.nodes import AppUserNode
from django.contrib.auth.hashers import make_password


class RegisterUserInput:
    name = String(required=True)
    last_name = String(required=True)
    username = String(required=True)
    email = String(required=True)
    password = String(required=True)
    is_militar = Boolean(required=False)
    is_temporal = Boolean(required=False)

    # Documento
    type_document_id = String(required=True)
    document = String(required=True)
    place_expedition = String(required=True)
    date_expedition = Date(required=True)

    # Contacto
    address = String(required=True)
    city = String(required=True)
    phone = String(required=True)
    cel_phone = String(required=True)
    emergency_name = String(required=True)
    emergency_phone = String(required=True)
    country_id = String(required=True)


class RegisterUser(relay.ClientIDMutation):
    user = Field(AppUserNode)

    class Input(RegisterUserInput):
        pass

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        from graphql_relay import from_global_id

        if AppUser.objects.filter(email=input["email"]).exists():
            raise GraphQLError("Email already registered.")

        if UserDocument.objects.filter(document=input["document"]).exists():
            raise GraphQLError("Document already registered.")

        user = AppUser(
            name=input["name"],
            last_name=input["last_name"],
            username=input["username"],
            email=input["email"],
            password=make_password(input["password"]),
            is_militar=input.get("is_militar", False),
            is_temporal=input.get("is_temporal", False)
        )
        user.save()

        # Decode global ID de type_document_id y country_id
        _, type_document_id = from_global_id(input["type_document_id"])
        _, country_id = from_global_id(input["country_id"])

        # Crear UserDocument
        UserDocument.objects.create(
            user=user,
            document=input["document"],
            type_document_id=type_document_id,
            place_expedition=input["place_expedition"],
            date_expedition=input["date_expedition"]
        )

        # Crear ContactInfo
        ContactInfo.objects.create(
            user=user,
            address=input["address"],
            city=input["city"],
            phone=input["phone"],
            cel_phone=input["cel_phone"],
            emergency_name=input["emergency_name"],
            emergency_phone=input["emergency_phone"],
            country_id=country_id
        )

        return RegisterUser(user=user)
