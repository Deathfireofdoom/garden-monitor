from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse

from gardensensors import GardenSensor

app = Flask(__name__)
api = Api(app)


class GardenMonitor(Resource):
    def __init__(self):
        super().__init__()
    def get(self, selection='all'):
        sensors = GardenSensor()
        if selection == 'all':
            return jsonify(sensors.all)
        
        if selection == 'temp':
            return jsonify(sensors.temp)
            
        if selection == 'hum':
            return jsonify(sensors.hum)

        if selection == 'soil':
            return jsonify(sensors.soil)

api.add_resource(GardenMonitor, '/gardenmonitor/<string:selection>')



if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
