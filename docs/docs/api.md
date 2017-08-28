# Data collection

### Login
	method: POST
	endpoint: /login/
	payload: {
		"username": "jamesbond",
		"password": "********"
	}
	response-success 200 OK: {
	  	"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InZhYXRpZXN0aGVyQGdtYWlsLmNvbSIsInVzZXJfaWQiOiI2YjZjNjVkMi1lN2EzLTRmOGUtYTc1MS1hOTMzMWZlMzBiZWMiLCJlbWFpbCI6InZhYXRpZXN0aGVyQGdtYWlsLmNvbSIsImV4cCI6MTQ4NTI2MTM0Mn0._NOMWY_oijHaXdvqy1M3wnuEyyA9IRM4OvjGFDk0D1c",
	}
	response-error 400 BAD REQUEST: {
		"error": "can not authenticate with the given credentials"		
	}

### Retrieve all drinks.
    method: GET
	endpoint: /data/drinks/
    headers: Authorization Token <token>
	response-success 200 OK: [
    {
        "_id": "f986ff0b-210b-42b3-938e-321cd8c1e549",
        "name": "Cocacola",
        "flavor": ""
    },
    {
        "_id": "dffae2f9-836b-49ed-b0a1-89149af44296",
        "name": "Sprite",
        "flavor": ""
    }]
	
 _Returns a list of all cocacola drinks in the system_

 _When adding data, users select drinks from this list_.

 _This ensures data consistency_.

### Save a record/data.
    method: POST
    headers: Authorization Token <token>
	endpoint: /data/data_collected/
    request-payload: {
        "drink_id": "6be7a37e-d47e-4a47-8fad-35ac289a6ba6",
        "location_longitude": "112.255515",
        "consumer_name": "mike sonko",
        "location_latitude": "74.2245",
        "location": "south b"
    }	
    response-success 201 Created: {
        "success": "created"
    }

### Retrive all data collected by a user.
    method: GET
    headers: Authorization Token <token>
    endpoint: /data/data_collected/
    response-payload 200 OK: [
        {
            "_id": "8fcb178f-4359-4f1d-bafc-d3925f8ee30b",
            "favorite_drink": {
                "_id": "a0483525-bd42-44f8-940b-ede14c4b3913",
                "name": "Fanta",
                "flavor": "passion"
            },
            "consumer_name": "dirk nowitzki",
            "location": "langata",
            "location_longitude": "112.255515",
            "location_latitude": "74.224500",
            "modified": "2017-08-27T10:07:53.469699Z",
            "created": "2017-08-27T10:07:53.469760Z"
        },
        {
            "_id": "6275f436-3160-4bbe-b6ae-7c4a19393b42",
            "favorite_drink": {
                "_id": "41977df3-ca43-4795-9ba6-933331d4a241",
                "name": "Krest",
                "flavor": ""
            },
            "consumer_name": "mike sonko",
            "location": "south b",
            "location_longitude": "25.255515",
            "location_latitude": "56.224500",
            "modified": "2017-08-27T10:08:39.856084Z",
            "created": "2017-08-27T10:08:39.856142Z"
        }
    ]

### Retrive a particular record collected by a user.
    method: GET
    headers: Authorization Token <token>
    endpoint: /data/record/<record_id>/
    response-payload 200 OK: {
            "_id": "8fcb178f-4359-4f1d-bafc-d3925f8ee30b",
            "favorite_drink": {
                "_id": "a0483525-bd42-44f8-940b-ede14c4b3913",
                "name": "Fanta",
                "flavor": "passion"
            },
            "consumer_name": "dirk nowitzki",
            "location": "langata",
            "location_longitude": "112.255515",
            "location_latitude": "74.224500",
            "modified": "2017-08-27T10:07:53.469699Z",
            "created": "2017-08-27T10:07:53.469760Z"
        }        


### Update a particular record collected by a user.
    method: PUT
    headers: Authorization Token <token>
    endpoint: /data/record/<record_id>/
    request-payload: { 
        "drink_id": "a9304b25-d589-49e6-b38d-cf06dccc5b24",
        "consumer_name": "erick omondi",
        "location": "buruburu",
        "location_longitude": "55.255",
        "location_latitude": "74.2245"
    }        

    response-success 200 OK: {
        "success": "updated"
    }

### Delete a record
    method: DELETE
    headers: Authorization Token <token>
    endpoint: /data/record/<record_id>/
    response-success 204 No content
