import json
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.mixins import (ListModelMixin,
                                   RetrieveModelMixin)

from .models import *
from .serializers import *


class CountryViewSet(ListModelMixin,
                     RetrieveModelMixin,
                     viewsets.GenericViewSet):
    """
    list:
    Return countries

    retrieve:
    Return country by id
    """

    serializer_class = CountrySerializer
    queryset = Country.objects.all()


class RegionViewSet(ListModelMixin,
                     RetrieveModelMixin,
                     viewsets.GenericViewSet):
    """
    list:
    Return regions

    retrieve:
    Return region by id
    """

    serializer_class = RegionSerializer
    queryset = Region.objects.all()


class AreaViewSet(ListModelMixin,
                     RetrieveModelMixin,
                     viewsets.GenericViewSet):
    """
    list:
    Return areas

    retrieve:
    Return area by id
    """

    serializer_class = AreaSerializer
    queryset = Area.objects.all()


class QualityViewSet(ListModelMixin,
                     RetrieveModelMixin,
                     viewsets.GenericViewSet):
    """
    list:
    Return quality

    retrieve:
    Return quality by id
    """

    serializer_class = QualitySerializer
    queryset = Quality.objects.all()


class DrinkViewSet(ListModelMixin,
                     RetrieveModelMixin,
                     viewsets.GenericViewSet):
    """
    list:
    Return drinks

    retrieve:
    Return drink by id
    """

    serializer_class = DrinkSerializer
    queryset = Drink.objects.all()


def get_region(request):
    id = request.GET.get('id', '')
    result = list(Region.objects.filter(country__in=[int(id)]).values('id', 'name'))
    return HttpResponse(json.dumps(result), content_type="application/json")


def get_area(request):
    id = request.GET.get('id', '')
    result = list(Area.objects.filter(region_id=int(id)).values('id', 'name'))
    return HttpResponse(json.dumps(result), content_type="application/json")
