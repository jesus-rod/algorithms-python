# from pprint import pprint

# valuesDict = {1: "one", 2: "two"}

# for elem in valuesDict.items():
#     pprint(elem)
#     key, value = elem
#     print(key, "->", value)

# print(elem.value)


# def cyclic_sort(nums):
#     print(nums)
#     i = 0
#     while i < len(nums):
#         j = nums[i] - 1
#         if nums[j] != nums[i]:
#             nums[i], nums[j] = nums[j], nums[i]
#         else:
#             i += 1

#     return nums


# print(cyclic_sort([3, 1, 5, 4, 2]))

testArray = [1, 2, 3]

testArray.insert(0, 4)

testArray.append(5)
print(testArray)

# order
tuple_list = [(1, 2), (3, 4), (2, 3)]
tuple_list.sort()
print(tuple_list)


class People:
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return "this aint workin"

    def __repr__(self):
        return f'this person is {self.age}'


kid = People(8)
adult = People(21)
toddler = People(4)
teenager = People(14)


people_list = [toddler, kid, teenager, adult]
people_list.sort(key=lambda x: x.age)
print(people_list)
