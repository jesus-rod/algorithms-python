from __future__ import print_function
from heapq import *
from math import *


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')

    def find_euclidean_distance(self):
        return self.x ** 2 + self.y ** 2


def find_closest_points(points, k):
    minHeap = []
    result = []

    for point in points:
        heappush(minHeap, (point.find_euclidean_distance(), point))

    for i in range(k):
        distance, point = heappop(minHeap)
        result.append(point)

    return result


def main():

    result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
    print("Here are the k points closest the origin: ", end='')
    for point in result:
        point.print_point()


main()
