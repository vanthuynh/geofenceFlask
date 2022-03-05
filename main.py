from urllib import response
from flask import Flask, jsonify, request
from tinydb import TinyDB, Query
import json
# from flask_cors import CORS, cross_origin

app = Flask(__name__)

# create db.json file for storing geofence data
db = TinyDB('geoDB.json')

# create tables with specific name and initialize them 
MACTable = db.table('MAC')
ERUTable = db.table('ERU')
MEATable = db.table('MEA')
dropCoordinatesTable = db.table('drop_coordinates')
searchAreaTable = db.table('search_area_coordinates')

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
            dropCoordinatesTable.upsert(drop_coordinates, query.vehicle=='MAC')
        elif(vehicle_id == 'ERU'):
            dropCoordinatesTable.upsert(drop_coordinates, query.vehicle=='ERU')
        elif(vehicle_id == 'MEA'):
            dropCoordinatesTable.upsert(drop_coordinates, query.vehicle=='MEA')
        response_object['message'] = 'data added!'
    return jsonify(response_object)

@app.route('/<vehicle_id>/getDropLocation', methods=['GET'])
def get_drop_location(vehicle_id):
    response_object = {'status': 'success'}
    if request.method == 'GET':
        if(vehicle_id == 'MAC'):
            result=dropCoordinatesTable.search(query.vehicle == 'MAC')
        elif(vehicle_id == 'ERU'):
            result=dropCoordinatesTable.search(query.vehicle == 'ERU')
        elif(vehicle_id == 'MEA'):
            result=dropCoordinatesTable.search(query.vehicle == 'MEA')
        response_object['data'] = result
    return jsonify(response_object)

@app.route('/postSearchArea', methods=['POST'])
def submit_search_area():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        search_area_coordinates = request.get_json(force=True)
        searchAreaTable.truncate()
        searchAreaTable.insert(search_area_coordinates)
        response_object['message'] = 'data added!'
    return jsonify(response_object)

@app.route('/getSearchArea', methods=['GET'])
def get_search_area():
    response_object = {'status': 'success'}
    if request.method == 'GET':
        result = json.dumps(searchAreaTable.all())
        response_object['data'] = result
    return jsonify(response_object)



####### commands that modify database without requests
# db.drop_table('_default')
# db.drop_table('search_area_coordinates')

if __name__ == '__main__':
    app.run(host="localhost", port=9000, debug=True) # remove boolean value for production build