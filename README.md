# Simple CRUD API with dummy data

3. Use TinyDB to manipulate geofence data on json file 

### How To Run
1. Install `virtualenv`:
```
$ pip install virtualenv
```

2. Open a terminal in the project root directory and run:
```
$ virtualenv env
```

3. Then run the command:
```
$ .\env\Scripts\activate
or
$ source env/Scripts/activate (for GitBash)
```

4. Then install the dependencies:
```
$ (env) pip install -r requirements.txt
```

5. Finally start the web server:
```
$ (env) python app.py
```

### default geofence format
```
{
    "Geofence": [
        {
            "Coordinates": [
                {"lat": 30, "lng": 25.5},
                {"lat": 50.9, "lng": 10.5},
                {"lat": 20, "lng": 30},
                {"lat": 60, "lng": 52.3},
                {"lat": 71, "lng": 40.12}
            ],
            "Keep_in": true,
            "Circle_inputs": {
              "lng": null,
              "lat": null,
              "rad": null
            }
        },
        {
            "Coordinates": [
                {"lat": 40, "lng": 35.5},
                {"lat": 61.9, "lng": 12.5},
                {"lat": 30, "lng": 56}
            ],
            "Keep_in": false,
            "Circle_inputs": {
              "lng": -124,
              "lat": 37,
              "rad": null
            }
        }
    ]
}

```