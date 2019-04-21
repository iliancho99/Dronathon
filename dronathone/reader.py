import json


def read_drones_from_json():
    drones = []
    with open('data/drones/drones.json') as json_file:
        for drone in json.load(json_file):
            drones.append(json.loads(drone[0]))
    return drones


def read_parcels_from_json():
    parcels = []
    for i in range(1, 6):
        with open('data/parcels/parcel' + str(i) + '.json') as json_file:
            for parcel in json.load(json_file):
                parcels.append(json.loads(parcel[0]))
    return parcels


def read_stations_from_json():
    stations = []
    with open('data/stations/station.json') as json_file:
        for station in json.load(json_file):
            stations.append(json.loads(station[0]))
    return stations

