from rest_framework import serializers
from .models import FormulaDetail


class FormulaDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = FormulaDetail
        fields = "__all__"

    