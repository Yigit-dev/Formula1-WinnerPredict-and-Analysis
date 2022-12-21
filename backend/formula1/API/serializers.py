from rest_framework import serializers
from formula1.models import Teams, Races, Drivers, Formula1


class Formula1Serializer(serializers.ModelSerializer):

    class Meta:
        model = Formula1
        fields = "__all__"

class TeamsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teams
        fields = "__all__"

class RacesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Races
        fields = "__all__"

class DriversSerializer(serializers.ModelSerializer):

    class Meta:
        model = Drivers
        fields = "__all__"