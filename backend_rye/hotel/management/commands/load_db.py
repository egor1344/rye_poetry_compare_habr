from django.core.management import BaseCommand
from django.db import transaction

from tests.booking.factories import BookingFactory, CustomerFactory
from tests.hotel.factories import HotelSuiteFactory, HotelFactory


class Command(BaseCommand):
    def handle(self, *args: tuple, **options: dict) -> None:
        for _ in range(500):
            h = HotelFactory()
            for _ in range(100):
                hsf = HotelSuiteFactory(hotel=h)
                for _ in range(100):
                    c = CustomerFactory()
                    BookingFactory(suite=hsf,customers=[c])
