from flask import Flask, jsonify, request
from geofenceFormat import *

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
geoERU = [
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
geoMEA = [
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

# @app.route('/ping', methods=['GET',])
# def ping_pong():
#     return jsonify('pong!')

'''
SUBMIT ALL: clear all data and add new submitted data
DELETE ALL: clear all data and leave it be
'''
@app.route('/MAC', methods=['GET', 'POST'])
def add_geo_MAC():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        geoData = request.get_json()
        geoData.clear()
        #add keep in data
        geoMAC.append({
            'Coordinates': geoData[0].get('Coordinates'),
            'Keep_in': geoData[0].get('Keep_in'),
            'read': geoData[0].get('read')
        })
        #add keep out data
        geoMAC.append({
            'Coordinates': geoData[1].get('Coordinates'),
            'Keep_in': geoData[1].get('Keep_in'),
            'read': geoData[1].get('read')
        })
        response_object['message'] = 'data added!'
    else:
        response_object['data'] = geoMAC
    return jsonify(response_object)


@app.route('/MAC', methods=['DELETE'])
def remove_geo_MAC():
    response_object = {'status': 'success'}
    geoMAC.clear()
    response_object['message'] = 'data removed!'
    return jsonify(response_object)

'''
SUBMIT ALL: clear all data and add new submitted data
DELETE ALL: clear all data and leave it be
'''
@app.route('/ERU', methods=['GET', 'POST'])
def add_geo_ERU():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        geoData = request.get_json()
        geoData.clear()
        #add keep in data
        geoERU.append({
            'Coordinates': geoData[0].get('Coordinates'),
            'Keep_in': geoData[0].get('Keep_in'),
            'read': geoData[0].get('read')
        })
        #add keep out data
        geoERU.append({
            'Coordinates': geoData[1].get('Coordinates'),
            'Keep_in': geoData[1].get('Keep_in'),
            'read': geoData[1].get('read')
        })
        response_object['message'] = 'data added!'
    else:
        response_object['data'] = geoERU
    return jsonify(response_object)


@app.route('/ERU', methods=['DELETE'])
def remove_geo_ERU():
    response_object = {'status': 'success'}
    geoERU.clear()
    response_object['message'] = 'data removed!'
    return jsonify(response_object)
'''
SUBMIT ALL: clear all data and add new submitted data
DELETE ALL: clear all data and leave it be
'''
@app.route('/ERU', methods=['GET', 'POST'])
def add_geo_ERU():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        geoData = request.get_json()
        geoData.clear()
        #add keep in data
        geoERU.append({
            'Coordinates': geoData[0].get('Coordinates'),
            'Keep_in': geoData[0].get('Keep_in'),
            'read': geoData[0].get('read')
        })
        #add keep out data
        geoERU.append({
            'Coordinates': geoData[1].get('Coordinates'),
            'Keep_in': geoData[1].get('Keep_in'),
            'read': geoData[1].get('read')
        })
        response_object['message'] = 'data added!'
    else:
        response_object['data'] = geoERU
    return jsonify(response_object)


@app.route('/ERU', methods=['DELETE'])
def remove_geo_ERU():
    response_object = {'status': 'success'}
    geoERU.clear()
    response_object['message'] = 'data removed!'
    return jsonify(response_object)
        
    

if __name__ == '__main__':
    app.run(debug=True) # remove boolean value for production build