from django.contrib import admin
from registered_users.models import (
    AppUser,
    UserDocument,
    TypeDocument,
    ContactInfo,
    Country
)


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "name", "last_name", "is_militar", "is_temporal", "time_create")
    search_fields = ("username", "email", "name", "last_name")
    readonly_fields = ("time_create",)
    fields = (
        "username", "email", "name", "last_name",
        "password", "is_militar", "is_temporal",
        "email_verified", "verification_token", "time_create"
    )


@admin.register(UserDocument)
class UserDocumentAdmin(admin.ModelAdmin):
    list_display = ("user", "document", "type_document", "place_expedition", "date_expedition")
    search_fields = ("document", "user__username", "user__email")
    fields = (
        "user", "type_document", "document",
        "place_expedition", "date_expedition"
    )


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ("user", "city", "phone", "cel_phone", "country")
    search_fields = ("user__username", "city", "cel_phone")
    fields = (
        "user", "address", "city", "phone", "cel_phone",
        "emergency_name", "emergency_phone", "country"
    )


@admin.register(TypeDocument)
class TypeDocumentAdmin(admin.ModelAdmin):
    list_display = ("id", "name_type_document",)
    search_fields = ("name_type_document",)
    fields = ("name_type_document",)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("country_code", "country_name",)
    search_fields = ("country_code", "country_name")
    fields = ("country_code", "country_name",)
