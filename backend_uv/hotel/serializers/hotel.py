from rest_framework import serializers

from booking.models import Booking
from hotel.models import Hotel, HotelSuite


class _BookingListSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ("customers", "suite")
        model = Booking


class _HotelSuiteListSerializer(serializers.ModelSerializer):
    booking_set = _BookingListSerializer(many=True, read_only=True)

    class Meta:
        exclude = ("hotel",)
        model = HotelSuite

    def get_bookings(self, obj):
        return []


class HotelListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Hotel


class HotelDetailSerializer(serializers.ModelSerializer):
    hotelsuite_set = _HotelSuiteListSerializer(many=True, read_only=True)

    class Meta:
        fields = '__all__'
        model = Hotel
