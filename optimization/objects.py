
import geopy.distance

def kmDist(locA, locB):
    """ Measrue geodesic distance in kilometers between to Location objects."""
    set1 = locA.get_pos()
    set2 = locB.get_pos()
    return geopy.distance.distance(set1,set2).km


def isClose(locA, locB, km = 1):
    """ Check if two Location objects are within a distance """
    check = True if kmDist(locA, locB) <= km else False
    return check


class Location:
    """ Super class of Location """
    def __init__(self, lat, long, id, neighbors):
        self.lat = lat
        self.long = long
        self.id = id
        self.neighborhood = neighbors

    def get_pos(self):
        """ get lat long tupel of the location """
        return (self.lat, self.long)


    def findNeighbors(self, neighborList, km = 1):
        """ Find Locations within km radius """
        for neighbor in neighborList:

            if isClose(self, neighbor, km):
                self.neighborhood.append(neighbor)

        return self.neighborhood



class BusStop(Location):
    """ Bus stop class"""
    def __init__(self, lat, long, id, blocks):
        super().__init__(lat, long, id, blocks)
        self.demand = 0
        self.weight = 0
        self.connectedness = 0
        self.serving = []

    def __repr__(self):
        return f'busStop id:{self.id}'

class Block(Location):
    """ Demand point, can be Dissemintaion Area or Dissemintaion Block """
    def __init__(self, lat, long, id, pop, dwel, stops):
        super().__init__(lat, long, id, stops)
        self.pop = pop
        self.dwel = dwel

    def __repr__(self):
        return f'block id:{self.id}'



if __name__ == '__main__':
    stop1 = BusStop(52,10,101,[])
    stop2 = BusStop(52.01,10.1,102,[])
    stops = [stop1, stop2]

    block1 = Block(52.0002,10.0002,101, 10, 10,[])
    block2 = Block(52.0003,10.0003,102, 10, 10,[])
    blocks = [block1, block2]

    stop1.findNeighbors(blocks)
    print(stop1.neighborhood)

    block1.findNeighbors(stops)
    print(block1.neighborhood)
