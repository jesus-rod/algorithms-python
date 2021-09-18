from heapq import *


class MaximizeCapital:
    minCapitalHeap = []
    maxProfitHeap = []

    savedCapital = 0

    def find_maximum_capital(self, capital, profits, numberOfProjects, initialCapital):

        # My saved capital is my initialCapital
        self.savedCapital = initialCapital
        self.fill_min_heap_with_capital(capital)

        while numberOfProjects > 0:
            numberOfProjects -= 1
            print("did this", self.savedCapital)
            # we continue going through or minHeap while it's not empty
            # and the "cheapest" project is less or equal that our savedCapital
            while self.minCapitalHeap and self.minCapitalHeap[0][0] <= self.savedCapital:
                capital, index = heappop(self.minCapitalHeap)
                heappush(self.maxProfitHeap, -profits[index])

            if len(self.maxProfitHeap) == 0:
                break

            self.savedCapital += -heappop(self.maxProfitHeap)

        return self.savedCapital

    # Filling out minheap with a tuple (capital, index)
    # Then we can use the index of the capitals to match the profits

    def fill_min_heap_with_capital(self, capital):
        for index, unit in enumerate(capital):
            heappush(self.minCapitalHeap, (unit, index))


def main():
    maximizer = MaximizeCapital()
    print("Maximum capital: " +
          str(maximizer.find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))
    print("Maximum capital: " +
          str(maximizer.find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))


main()
