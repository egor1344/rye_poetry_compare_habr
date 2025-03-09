import factory

from booking.models import Customer, Booking
from tests.hotel.factories import HotelSuiteFactory


class CustomerFactory(factory.django.DjangoModelFactory):
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    middle_name = factory.Faker("first_name")

    phone = factory.Faker('phone_number', locale='ru_RU')
    email = factory.Faker('email')

    class Meta:
        model = Customer


class BookingFactory(factory.django.DjangoModelFactory):
    suite = factory.SubFactory(HotelSuiteFactory)
    from_date = factory.Faker('date_between', start_date='-1y', end_date='now')
    to_date = factory.Faker('date_between', start_date='-1y', end_date='now')

    @factory.post_generation
    def customers(self, create, extracted, **kwargs):
        if not create or not extracted:
            return

        self.customers.add(*extracted)

    class Meta:
        model = Booking
