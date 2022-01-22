from flask import Flask, jsonify, request
from tinydb import TinyDB


#instantiate the app
app = Flask(__name__)

geoMAC = [
            {
                "Coordinates": [
                    {"lat": 0.0, "lng": 0.0}
                ],
                "Keep_in": True,
                "Circle_inputs": {
                    "lng": 0.0,
                    "lat": 0.0,
                    "rad": None
                }
            },
            {
                "Coordinates": [
                    {"lat": 0.0, "lng": 0.0}
                ],
                "Keep_in": False,
                "Circle_inputs": {
                    "lng": 0.0,
                    "lat": 0.0,
                    "rad": None
                }
            }
        ]
# @app.route('/',methods = ['GET'])
# def ping():
#     return jsonify(geoMEA)

'''
SUBMIT ALL: clear all data and add new submitted data
DELETE ALL: clear all data and leave it be
'''
@app.route('/geofence/<vehicle_id>', methods=['GET', 'POST'])
def submit_geofence():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        geoData = request.get_json()
        
        response_object['message'] = 'data added!'
    else:
        response_object['data'] = geoMAC
    return jsonify(response_object)

@app.route('/geofence/<vehicle_id>', methods=['DELETE'])
def remove_geofence(vehicle_id):
    


if __name__ == '__main__':
    app.run(debug=True) # remove boolean value for production build