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
    #finalize data format
    def data_formal():
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
    def setCoordinates(self, newCoordinates):
        

        # list of dictionaries
        for item in newCoordinates:
            if item.value == float:
                self.jsonFormat[0].update("Coordinates".append(item))
                
        # 2D array     

    def getCoordinates(self, newCoordinates):
        return 