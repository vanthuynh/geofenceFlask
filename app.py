from flask import Flask, jsonify, request
from geofenceFormat import *

#instantiate the app
app = Flask(__name__)

''' dummy data
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

'''

# @app.route('/ping', methods=['GET',])
# def ping_pong():
#     return jsonify('pong!')

@app.route('/', methods=['GET', 'POST'])
def geofenceInOut():
    if request.method == 'GET':
        return jsonify(GEOFENCE)

@app.route('/geofence', methods=['PUT','DELETE'])
def updateGeofence():
    if request.method == 'PUT':
        
    

if __name__ == '__main__':
    app.run(debug=True) # remove boolean value for production build