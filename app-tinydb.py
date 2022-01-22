from msilib import Table
from flask import Flask, jsonify, request
from tinydb import TinyDB, Query
import json

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

# create an instance of Query class that can help us search the database
# vehicle = Query()

# # change the name for the default table
TinyDB.default_table_name = 'vehicleDB'

# '''
# CREATe tables
# '''
# # # create tables with specific name and initialize them 
MACTable = db.table('MAC')
# # MACTable.insert(defaultGeo)
ERUTable = db.table('ERU')
# # ERUTable.insert(defaultGeo)
MEATable = db.table('MEA')
# # MEATable.insert(defaultGeo)

test = db.table('TEST')
# # test.insert(defaultGeo)

'''
DELETE all tables
'''
MACTable.truncate()
ERUTable.truncate()
MEATable.truncate()
test.truncate()



# db.drop_table('MEA')
# print(json.dumps(db.all(), indent = 2))
print(db)

