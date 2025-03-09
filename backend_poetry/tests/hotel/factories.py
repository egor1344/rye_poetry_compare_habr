import factory
from factory import fuzzy

from hotel.constant import HotelSuiteType
from hotel.models import Hotel, HotelSuite


class HotelFactory(factory.django.DjangoModelFactory):
    """Фабрика Отелей."""

    name = factory.Faker("company")

    class Meta:
        model = Hotel


class HotelSuiteFactory(factory.django.DjangoModelFactory):
    """Фабрика Отелей."""

    hotel = factory.SubFactory(HotelFactory)
    number = factory.Faker("pyint", min_value=0, max_value=100)
    type = fuzzy.FuzzyChoice(HotelSuiteType.choices, getter=lambda c: c[0])
    floor = factory.Faker("pyint", min_value=0, max_value=10)
    rooms = factory.Faker("pyint", min_value=0, max_value=3)

    class Meta:
        model = HotelSuite
