import heapq


class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department


people = [{"name": "Pedro", "dept": "IT"},
          {"name": "Maria", "dept": "HR"},
          {"name": "Juana", "dept": "IT"},
          {"name": "Maida", "dept": "IT"},
          {"name": "Jesus", "dept": "IT"},
          {"name": "Luke", "dept": "HR"},
          {"name": "Rene", "dept": "Management"},
          ]

employees = {}


# create a dictionary
# where the key is the department and the value is the employees in said department
for person in people:
    currentDepartment = person["dept"]
    newEmployee = Employee(person["name"], currentDepartment)

    if currentDepartment in employees:
        employees[currentDepartment] = employees[currentDepartment] + [newEmployee]
    else:
        employees[currentDepartment] = [newEmployee]

# make a list with tuples containing number of employees in the department eg: [(3, "IT"), (2 "HR"))]
# this is so the heap has a way to order the data
max_heap = []
for key, value in employees.items():
    numOfEmployeesInDept = len(value)
    max_heap.append((numOfEmployeesInDept * -1, key))

# convert the tuple created before into a heap
heapq.heapify(max_heap)

print(max_heap)

pairs = []

# from the maxheap, pop the two departments with most people
# if there is only one department, then we stop.
while len(max_heap) > 1:
    maxNum, maxDepartment = heapq.heappop(max_heap)
    secondMaxNum, secondMaxDepartment = heapq.heappop(max_heap)

    print(maxDepartment, secondMaxDepartment)
    newMaxNum = (abs(maxNum) - 1) * -1
    secondMaxNum = (abs(secondMaxNum) - 1) * -1

    # only push in the heap again if the number of employees is more than zero
    if abs(newMaxNum) > 0:
        heapq.heappush(max_heap, (newMaxNum, maxDepartment))
    if abs(secondMaxNum) > 0:
        heapq.heappush(max_heap, (secondMaxNum, secondMaxDepartment))

    # then from our dictionary created in the beginning, we can get the employees data
    employeeOne = employees[maxDepartment].pop()
    employeeTwo = employees[secondMaxDepartment].pop()

    # finally, we append the data to our final result
    pairs.append((employeeOne.name, employeeTwo.name))


# pairs now contain tuples of employees from different departments
# we could return pairs
# return pairs

print(pairs)
