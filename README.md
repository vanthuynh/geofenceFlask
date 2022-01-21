# Different approaches for geofence API

1. Implement geofence format using object oriented programming (it's easier to manipulate data and add/retrieve from database this way)

2. Implement simple CRUD API provided 3 lists of 3 vehicles

3. Use tinyDB to add/retrieve geofence data from json files

``` default format for geofence
GEOFENCE = [
            {
                "Coordinates": [
                    {"lat": 30, "lng": 25.5},
                    {"lat": 50.9, "lng": 10.5},
                    {"lat": 20, "lng": 30},
                    {"lat": 60, "lng": 52.3},
                    {"lat": 71, "lng": 40.12}
                ],
                "Keep_in": True,
                "Circle_inputs": {
                    "lng": 60,
                    "lat": -120,
                    "rad": None
                }
            },
            {
                "Coordinates": [
                    {"lat": 40, "lng": 35.5},
                    {"lat": 61.9, "lng": 12.5},
                    {"lat": 30, "lng": 56}
                ],
                "Keep_in": False,
                "Circle_inputs": {
                    "lng": -124,
                    "lat": 37,
                    "rad": None
                }
            }
        ]
```