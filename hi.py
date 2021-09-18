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
