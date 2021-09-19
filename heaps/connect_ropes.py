from heapq import *


def minimum_cost_to_connect_ropes(ropeLengths):
    result = 0

    heapify(ropeLengths)

    while len(ropeLengths) > 1:
        topElem = heappop(ropeLengths)
        secondTopElem = heappop(ropeLengths)

        newElem = topElem + secondTopElem
        heappush(ropeLengths, newElem)
        result += newElem

    return result


def main():

    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))


main()
