from rest_framework.serializers import ModelSerializer
from .models import (
    Data,
    Drink
)


class DrinkSerializer(ModelSerializer):
    class Meta:
        model = Drink
        fields = ("_id", "name", "flavor")


class DataSerializer(ModelSerializer):
    favorite_drink = DrinkSerializer()

    class Meta:
        model = Data
        exclude = ("collector", )
