import json


def read_drones_from_json():
    drones = []
    with open('data/drones/drones.json') as json_file:
        for drone in json.load(json_file):
            drones.append(json.loads(drone[0]))
    return drones


def read_parcels_from_json():
    parcels = []
    for i in range(0,7):
        parcels_in_area = []
        with open('data/parcels/parcel' + str(i)+'.json') as json_file:
            for parcel_in_area in json.load(json_file):
                parcels_in_area.append(json.loads(parcel_in_area[0]))
        parcels.append(parcels_in_area)
    return parcels


def read_stations_from_json():
    stations = []
    with open('data/stations/station.json') as json_file:
        for station in json.load(json_file):
            stations.append(json.loads(station[0]))
    return stations

def read_warehouses_from_json():
    warehouses = [
    {"name" : "NETWORKING: Premium Coworking Space [Dronathon]", "id" : 0, "location": [42.7058171,23.3287061]},
    {"name" : "Business Center Serdika", "id":1, "location": [42.691163,23.294588] },
    {"name" : "Bulgaria Mall","id":2, "location": [42.6643476,23.289005]},
    {"name" : "Airport Sofia Terminal 1",  "id":3, "location": [42.6895872,23.4027335000001]},
    {"name" : "SoftUni", "id":4, "location": [42.6666605,23.3506835000001]},
    {"name" : "NBU", "id":5, "location": [42.67786, 23.25269]},
    {"name" : "Lyulin, Sofia", "id":6, "location": [42.723894,23.2375028]}
]

    return warehouses
