import reader as r
import tools as t
import sys
import json

drones = r.read_drones_from_json()
station = r.read_stations_from_json()
parcels = r.read_parcels_from_json()

drone_delivery = {}
drone_count = 0
for drone in drones:

    drone_delivery[drone_count] = sys.maxsize

    for parcel in parcels:

        dist = t.distance(parcel['location'], drone['location'])
        print(dist)
