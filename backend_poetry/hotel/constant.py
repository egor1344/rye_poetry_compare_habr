from django.db import models


class HotelSuiteType(models.IntegerChoices):
    STD = 0, "Standard"
    SUPERIOR = 1, "Superior room"
    APT = 2, "Apartment"
    LUXE = 3, "Luxe"
    DUPLEX = 4, "Two floors"
