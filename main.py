from flask import Flask, jsonify, request
from tinydb import TinyDB, Query

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
db = TinyDB('db.json')

# # create tables with specific name and initialize them 
# MACTable = db.table('MAC')
# MACTable.insert(defaultGeo)
# ERUTable = db.table('ERU')
# ERUTable.insert(defaultGeo)
# MEATable = db.table('MEA')
# MEATable.insert(defaultGeo)

# create an instance of Query class that can help us search the database
vehicle = Query()

# db.drop_table('MEA')
print(db.all())


# function for debugging purpose
@app.route('/', methods=['GET', 'POST'])
def debug():
    print(db)
    return 0
'''
SUBMIT ALL: clear all data and add new submitted data
DELETE ALL: clear all data and leave it be
'''
@app.route('/geofence/<vehicle_id>', methods=['GET', 'POST'])
def submit_geofence(vehicle_id):
    response_object = {'status': 'success'}
    if request.method == 'POST':
        geoData = request.get_json(force=True)
        db.drop_table(vehicle_id) # remove the table for that vehicle
        if vehicle_id == 'MAC':
            table = db.table('MAC')
            table.insert(geoData)
        elif vehicle_id == 'ERU':
            table = db.table('ERU')
            table.insert(geoData)
        elif vehicle_id == 'MEA':
            table = db.table('MEA')
            table.insert(geoData)
        response_object['message'] = 'data added!'
    else:
        # target = db.search(vehicle.vehicle_id == )
        response_object['data'] = db
    return jsonify(response_object)

@app.route('/geofence/<vehicle_id>', methods=['DELETE'])
def remove_geofence(vehicle_id):
    return 0


if __name__ == '__main__':
    app.run(debug=True) # remove boolean value for production build