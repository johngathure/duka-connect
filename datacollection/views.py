from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import (
    Drink,
    Data
)
from .serializers import (
    DrinkSerializer,
    DataSerializer
)

# Create your views here.


class DrinksList(generics.ListAPIView):
    """
    Endpoint: /data/drinks/
    Description:
        - Returns a list of cocacola drinks in the system.
        - When users are entering the data, they select the drink rather
          than filling in the name itself.
        - This ensures there is consistency in the data entered.
    """

    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer


class DataList(generics.ListCreateAPIView):
    """
    Endpoint: /data/collected_data/
    Description:
    :get
        - Returns a list of all collected data by a particular user.
    :post
        - Saves a new data collection.
    """
    def create(self, request):
        data = request.data
        drink_id = data.pop("drink_id")
        serializer = DataSerializer(data)

        if serializer.is_valid:
            user = request.user
            drink = Drink.objects.get(
                _id=drink_id
            )
            Data.objects.create(
                collector=user,
                favorite_drink=drink,
                **data
            )
            return Response({"success": "created"},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        data = Data.objects.filter(
            collector=request.user
        ).select_related("favorite_drink")
        serializer = DataSerializer(data, many=True)

        return Response(serializer.data)


class DataDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    endpoint: /data/record/<record_id>/
    description:
    :get
    returns a particular data collection by a user

    :put
    updates a data record.

    :delete
    deletes a data record
    """

    queryset = Data.objects.all()
    serializer_class = DataSerializer

    def update(self, request, pk):
        data_collected = Data.objects.get(
            _id=pk
        )
        data = request.data
        drink_id = data["drink_id"]
        if drink_id is not data_collected.favorite_drink_id:
            drink = Drink.objects.get(
                _id=drink_id
            )
            data_collected.favorite_drink = drink
        for key, value in data.iteritems():
            setattr(data_collected, key, value)
        data_collected.save()

        return Response({"success": "updated"})
