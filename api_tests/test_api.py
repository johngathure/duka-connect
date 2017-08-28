import json
import random

from django.test import TestCase
from django.contrib.auth.models import User

from rest_framework.test import APIClient
from rest_framework import status

from datacollection.models import (
    Drink,
    Data
)


class ApiTestCase(TestCase):
    """
    Runs tests for the endpoints
    """
    def setUp(self):
        # client for simulating http requests
        self.client = APIClient()

        # test user for authenticaction
        user = User.objects.create_user(username='test_user',
                                        email='test_usere@gmail.com',
                                        password='test_password')

        # test data used in the test cases
        with open("api_tests/data.json") as data_file:
            self.test_data = json.load(data_file)

        self.user = user

        # force authentication for all requests
        self.client.force_authenticate(user=user)

    def test_user_can_log_in(self):
        """
        Test the login endpoint
        /login/
        """
        # create a user
        User.objects.create_user(username='john',
                                 email='juangathure@gmail.com',
                                 password='test_password')

        credentials = {
            "username": "john",
            "password": "test_password"
        }

        # use credentials of the user created to test the log in
        response = self.client.post('/login/', credentials,
                                    format='json')

        # assert the login was successful
        self.assertEqual(response.status_code,
                         status.HTTP_200_OK)

        data = response.json()

        # assert a token is returned for every successfull login
        assert "token" in data

    def test_if_user_can_retrive_drinks(self):
        """
        Test the retrieve drinks enpoint
        /data/drinks"
        """
        # take data from the ones extracted from the json file 
        drinks = self.test_data["drinks"]
        save_drinks = []
        for drink in drinks:
            drink = Drink(**drink)
            save_drinks.append(drink)
        Drink.objects.bulk_create(save_drinks)

        drink_count = Drink.objects.count()

        # assert the saving of the drinks was successful
        self.assertEqual(drink_count, 10)

        # retrieve the data via a request
        response = self.client.get("/data/drinks/")

        # assert the request was successful
        self.assertEqual(response.status_code,
                         status.HTTP_200_OK)

        recieved_data_count = len(response.json())

        # assert the number of drinks recieved is correct
        self.assertEqual(recieved_data_count, 10)

    def test_if_user_can_add_and_retrieve_data(self):
        """
        Test the add data endpoint
        /data/data_collected/
        """
        # take the first three drinks
        drinks = self.test_data["drinks"][:3]
        # create drink objects from the json data
        drinks = [Drink(**i) for i in drinks]
        Drink.objects.bulk_create(drinks)

        data = self.test_data["data"][0]
        # use drink ids added to the db for this particular
        # test
        data["drink_id"] = drinks[random.randint(0, 2)]._id

        response = self.client.post("/data/data_collected/",
                                    data, format='json')

        # assert it data was added correctly
        self.assertEqual(response.status_code,
                         status.HTTP_201_CREATED)

        # retrieve the data added
        response = self.client.get("/data/data_collected/")

        # assert if the response is 200
        self.assertEqual(response.status_code, 200)

        # get the number of added data records
        data_added_count = len(response.json())

        # assert if the data added is one
        self.assertEqual(data_added_count, 1)

    def test_if_user_can_update_data_added(self):
        """
        Test the retrieve one, update and delete endpoint
        /data/record/<record_id>/
        """
        drink_data = self.test_data["drinks"][0]
        # save a drink
        drink = Drink(**drink_data)
        drink.save()

        record_data = self.test_data["data"][0]
        data = Data(
            favorite_drink=drink,
            consumer_name=record_data["consumer_name"],
            location=record_data["location"],
            collector=self.user,
            location_longitude=record_data["location_longitude"],
            location_latitude=record_data["location_latitude"]
        )
        # save a data record
        data.save()

        # retrieve the added data record
        url = "/data/record/%s/" % data._id
        get_response = self.client.get(url)

        self.assertEqual(get_response.status_code,
                         status.HTTP_200_OK)
        recieved_data = get_response.json()
        self.assertEqual(recieved_data["consumer_name"],
                         "dirk nowitzki")

        # update the data record
        update_payload = {
            "drink_id": str(drink._id),
            "consumer_name": "erick omondi",
            "location": "buruburu",
            "location_longitude": "55.255",
            "location_latitude": "74.2245"
        }

        put_response = self.client.put(url, update_payload, format="json")
        self.assertEqual(put_response.status_code,
                         status.HTTP_200_OK)

        # retrieve the updated record
        updated_data = Data.objects.all()[0]
        # assert it has been updated
        self.assertNotEqual(updated_data.consumer_name,
                            recieved_data["consumer_name"])

        # delete the record
        delete_response = self.client.delete(url)
        # assert the status code is 204 no content
        self.assertEqual(delete_response.status_code,
                         status.HTTP_204_NO_CONTENT)
        # assert the record was actually deleted from the database
        data_count = Data.objects.count()
        self.assertEqual(data_count, 0)
