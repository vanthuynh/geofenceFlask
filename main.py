from urllib import response
from flask import Flask, jsonify, request
from tinydb import TinyDB, Query
import json

app = Flask(__name__)

# create db.json file for storing geofence data
db = TinyDB('geoDB.json')

# create tables with specific name and initialize them 
MACTable = db.table('MAC')
ERUTable = db.table('ERU')
MEATable = db.table('MEA')
dropCoordinatesTable = db.table('drop_coordinates')

# create an instance of Query class that can help us search the database
query = Query()

# # function for debugging purpose
# @app.route('/', methods=['GET', 'POST'])
# def debug():
#     # print(db.all())
#     return json.dumps(MACTable.all())

'''
SUBMIT ALL: clear all data and add new submitted data
DELETE ALL: clear all data and leave it be
'''
@app.route('/gcs/geofence/<vehicle_id>', methods=['GET', 'POST'])
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


@app.route('/gcs/geofence/<vehicle_id>', methods=['DELETE'])
def remove_geofence(vehicle_id):
    if(vehicle_id == 'MAC'):
        MACTable.truncate()
    elif(vehicle_id == 'ERU'):
        ERUTable.truncate()
    elif(vehicle_id == 'MEA'):
        MEATable.truncate()
    return "DELETE SUCCESS"

# @app.route('/gcs/<vehicle_id>/drop_location', method=['GET', 'POST'])
@app.route('/<vehicle_id>/submitDropLocation', methods=['POST'])
def submit_drop_location(vehicle_id):
    response_object = {'status': 'success'}
    if request.method == 'POST':
        drop_coordinates = request.get_json(force=True)
        if(vehicle_id == 'MAC'):
            db.upsert(drop_coordinates, query.vehicle=='MAC')
        elif(vehicle_id == 'ERU'):
            db.upsert(drop_coordinates, query.vehicle=='ERU')
        elif(vehicle_id == 'MEA'):
            db.upsert(drop_coordinates, query.vehicle=='MEA')
        response_object['message'] = 'data added!'
    return jsonify(response_object)

@app.route('/<vehicle_id>/getDropLocation', methods=['GET'])
def get_drop_location(vehicle_id):
    response_object = {'status': 'success'}
    if request.method == 'GET':
        if(vehicle_id == 'MAC'):
            result=db.search(query.vehicle == 'MAC')
        elif(vehicle_id == 'ERU'):
            result=db.search(query.vehicle == 'ERU')
        elif(vehicle_id == 'MEA'):
            result=db.search(query.vehicle == 'MEA')
        response_object['data'] = result
    return jsonify(response_object)


if __name__ == '__main__':
    app.run(debug=True) # remove boolean value for production build