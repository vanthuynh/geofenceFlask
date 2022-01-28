from flask import Flask, jsonify, request
from tinydb import TinyDB, Query
import json

#instantiate the app
app = Flask(__name__)

defaultGeo = {
    "Geofence": [
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
}

# create db.json file for storing geofence data
db = TinyDB('geoDB.json')

# # create tables with specific name and initialize them 
MACTable = db.table('MAC')
# MACTable.insert(defaultGeo)
ERUTable = db.table('ERU')
# ERUTable.insert(defaultGeo)
MEATable = db.table('MEA')
# MEATable.insert(defaultGeo)

# create an instance of Query class that can help us search the database
vehicle = Query()

# # db.drop_table('MEA')
# print(db.all())


# # function for debugging purpose
# @app.route('/', methods=['GET', 'POST'])
# def debug():
#     # print(db.all())
#     return json.dumps(MACTable.all())

'''
SUBMIT ALL: clear all data and add new submitted data
DELETE ALL: clear all data and leave it be
'''
@app.route('/geofence/<vehicle_id>', methods=['GET', 'POST'])
def submit_geofence(vehicle_id):
    response_object = {'status': 'success'}
    if request.method == 'POST':
        geoData = request.get_json(force=True)
        if vehicle_id == 'MAC':
            MACTable.truncate()
            MACTable.insert(geoData)
        elif vehicle_id == 'ERU':
            ERUTable.truncate()
            ERUTable.insert(geoData)
        elif vehicle_id == 'MEA':
            MEATable.truncate()
            MEATable.insert(geoData)
        response_object['message'] = 'data added!'
    else:
        # target = db.search(vehicle.vehicle_id == )
        # result = []
        if vehicle_id == 'MAC':
            result = json.dumps(MACTable.all())
        elif vehicle_id == 'ERU':
            result = json.dumps(ERUTable.all())
        elif vehicle_id == 'MEA':
            result = json.dumps(MEATable.all())
        response_object['data'] = result
    return jsonify(response_object)


@app.route('/geofence/<vehicle_id>', methods=['DELETE'])
def remove_geofence(vehicle_id):
    MACTable.truncate()
    ERUTable.truncate()
    MEATable.truncate()


if __name__ == '__main__':
    app.run(debug=True) # remove boolean value for production build