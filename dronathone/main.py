import reader as r
import tools as t
import sys
import json
import math

drones = r.read_drones_from_json()
station = r.read_stations_from_json()
parcels = r.read_parcels_from_json()

drone_delivery = {}
total_drones = len(drones)
total_parsels = 0
for i in range(0, len(parcels)):
    total_parsels += len(parcels[i])

parcels_percentage_of_all = []

for i in range(0, len(parcels)):
    parcels_percentage_of_all.append((len(parcels[i])/ total_parsels) * 100)

print(parcels_percentage_of_all)
drones_per_area = []

for i in range(len(parcels_percentage_of_all)):
    drones_per_area.append(int(round(parcels_percentage_of_all[i] * total_drones)/100))


print(drones_per_area)
# for drone in drones:
#
#     drone_delivery[drone_count] = sys.maxsize
#
#     for parcel in parcels:
#
#         dist = t.distance(parcel['location'], drone['location'])
#         print(dist)