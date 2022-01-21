'''
    - OOP implementation of Geofence data
    Note: 
        + possible to add circle inputs later (if required)
        + 
'''

class Geofence():
    def __init__(self):
        self.jsonFormat = [
            {
                "Coordinates": [
                    {"lat": 0.0, "lng": 0.0},
                ],
                "Keep_in": True
            },
            {
                "Coordinates": [
                    {"lat": 0.0, "lng": 0.0}
                ],
                "Keep_in": False
            }
        ]
    # initial instance of geofence data
    def data_format():
        jsonFormat = [
            {
                "Coordinates": [
                    {"lat": 0.0, "lng": 0.0},
                ],
                "Keep_in": True
            },
            {
                "Coordinates": [
                    {"lat": 0.0, "lng": 0.0}
                ],
                "Keep_in": False
            }
        ]

    def addKeepInCoordinates(self, newCoordinates):
        # Note: should handle type checking
        self.jsonFormat[0]["Coordinates"].append(newCoordinates)
        #### list of dictionaries
        # for item in newCoordinates:
        #     if item.value == float:
        #         self.jsonFormat[0].update("Coordinates".append(item))
                
        #### 2D array

    def addKeepOutCoordinates(self, newCoordinates):
        self.jsonFormat[1]["Coordinates"].append(newCoordinates)

    def getCoordinates(self, bound):
        if bound == True:
            return self.jsonFormat[0]
        return self.jsonFormat[1]