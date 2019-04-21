from math import cos, asin, sqrt
from reader import read_drones_from_json, read_warehouses_from_json, read_areas_from_json


def distance(loc1, loc2):
    lat1 = loc1[0]
    lon1 = loc1[1]
    lat2 = loc2[0]
    lon2 = loc2[1]

    p = 0.017453292519943295
    a = 0.5 - cos((lat2 - lat1) * p) / 2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a))


def move_drones_by_area_parcels(area_needs):
    drones = read_drones_from_json()
    areas_temp = read_areas_from_json()
    areas = []
    result = []
    for i in range(0, len(area_needs)):
        areas.append(Area(areas_temp[i], area_needs[i]))

    for j in range(0, len(drones)):
        for area in sort_areas_by_coord_to_drone(drones, j, areas):
            result.append({'drone_id': drones[j]['id'], 'warehouse_id': area['warehouse'],
                           'warehouse_loc': read_warehouses_from_json()[area['warehouse']]['location']})

    return result


def sort_areas_by_coord_to_drone(drones, j, areas):
    return sorted(areas, cmp=lambda x, y: cmp(x.closest_coord(drones[j]['location']),
                                              y.closest_coord(drones[j]['location'])))


class Area(object):
    def __init__(self, coord, needs):
        self.coord = coord
        self.needs = needs

    def __repr__(self):
        return '{}: {} {}'.format(self.__class__.__name__,
                                  self.coord,
                                  self.needs)

    def __cmp__(self, other):
        if hasattr(other, 'coord'):
            return self.coord.__cmp__(other.coord)

    def closest_coord(self, drone_coord):
        return min(sorted(self.coord, cmp=lambda x, y: cmp(distance(drone_coord, x), distance(drone_coord, y))))
