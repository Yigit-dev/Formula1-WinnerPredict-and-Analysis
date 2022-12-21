from rest_framework import viewsets
from formula1.models import Teams, Races, Drivers, Formula1
from .serializers import TeamsSerializer, RacesSerializer, DriversSerializer, Formula1Serializer

class Formula1(viewsets.ReadOnlyModelViewSet):
    queryset = Formula1.objects.all()
    serializer_class = Formula1Serializer

class Team(viewsets.ReadOnlyModelViewSet):
    queryset = Teams.objects.all()
    serializer_class = TeamsSerializer

class Races(viewsets.ReadOnlyModelViewSet):
    queryset = Races.objects.all()
    serializer_class = RacesSerializer

class Drivers(viewsets.ReadOnlyModelViewSet):
    queryset = Drivers.objects.all()
    serializer_class = DriversSerializer