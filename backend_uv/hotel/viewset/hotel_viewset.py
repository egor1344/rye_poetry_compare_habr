from typing import Type

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from drf_spectacular.utils import extend_schema
from rest_framework.serializers import Serializer
from rest_framework.viewsets import ReadOnlyModelViewSet

from hotel.models import Hotel
from hotel.serializers import HotelListSerializer
from hotel.serializers.hotel import HotelDetailSerializer


@extend_schema(tags=["Hotel"])
class HotelViewSet(ReadOnlyModelViewSet):

    def get_queryset(self):
        queryset = Hotel.objects.all()
        if self.action == self.retrieve.__name__:
            queryset = queryset.prefetch_related('hotelsuite_set__booking_set')
        return queryset

    def get_serializer_class(self):
        serializer_class: Type[Serializer] = HotelListSerializer
        if self.action == self.retrieve.__name__:
            serializer_class = HotelDetailSerializer
        return serializer_class

    @method_decorator(cache_page(60 * 10))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 10))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

