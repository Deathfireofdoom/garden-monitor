from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse

from gardensensors import GardenSensor

app = Flask(__name__)
api = Api(app)


class GardenMonitor(Resource):
    def __init__(self):
        super().__init__()
        self.sensors = GardenSensor()

    def get(self, selection='all'):
        if selection == 'all':
            return jsonify(self.sensors.all)
        
        if selection == 'temp':
            return jsonify(self.sensors.temp)
            
        if selection == 'hum':
            return jsonify(self.sensors.hum)

        if selection == 'soil':
            return jsonify(self.sensors.soil)

    def post(self, selection):
        if selection == 'water':
            self.sensors.water_plants()

api.add_resource(GardenMonitor, '/gardenmonitor/<string:selection>')



if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
