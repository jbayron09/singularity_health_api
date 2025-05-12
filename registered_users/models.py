from django.db import models
from django.utils import timezone


class TypeDocument(models.Model):
    name_type_document = models.CharField(max_length=50)

    def __str__(self):
        return self.name_type_document


class Country(models.Model):
    country_code = models.CharField(max_length=4)
    country_name = models.CharField(max_length=100)

    def __str__(self):
        return self.country_name


class AppUser(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    email_verified = models.BooleanField(default=False)
    verification_token = models.CharField(max_length=64, blank=True)

    is_militar = models.BooleanField(default=False)
    is_temporal = models.BooleanField(default=False)
    time_create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} {self.last_name} ({self.username})"


class UserDocument(models.Model):
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE)
    type_document = models.ForeignKey(TypeDocument, on_delete=models.PROTECT)
    document = models.CharField(max_length=20, unique=True)
    place_expedition = models.CharField(max_length=60)
    date_expedition = models.DateField()

    def __str__(self):
        return f"{self.document} - {self.type_document.name_type_document}"


class ContactInfo(models.Model):
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=60)
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    cel_phone = models.CharField(max_length=20)
    emergency_name = models.CharField(max_length=100)
    emergency_phone = models.CharField(max_length=20)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)

    def __str__(self):
        return f"Contact info for {self.user.username}"
