# names = ['alex', 'bob', 'charlie', 'dave', 'emily', 'frank', 'george', 'harry', 'idris', 'joe', 'kate', 'lisa',
#          'mike', 'nancy', 'olivia', 'paul', 'quinn', 'robert', 'sally', 'tom', 'victor', 'william', 'xavier', 'yvonne', 'zoe']
# selected = [name.upper() for name in names if len(name) > 5]
# print(selected)

# ...................................................
# numbers = [0, 1]
# print(numbers)
# for _ in range(10):
#     numbers.append(numbers[-1] + numbers[-2])
# print(numbers[1:-1])

# sqrder_num = [num*num for num in numbers]
# print(sqrder_num)

# ....................................................
# with open("file1.txt") as file1:
#     file1_data = file1.readlines()

# with open("file2.txt") as file2:
#     file2_data = file2.readlines()
# with open("file3.txt") as file3:
#     file3_data = file3.readlines()

# result = [int(num)
#           for num in file1_data if num in file2_data and num in file3_data]
# print(result)

# ...................................................


# dict_comprhension

# report_card = {"alex": 59,
#                "bob": 80,
#                "charlie": 50,
#                "dave": 70,
#                "emily": 90,
#                "frank": 60,
#                "george": 80,
#                "harry": 50,
#                "idris": 70,
#                "joe": 90,
#                "kate": 60,
#                "lisa": 80,
#                "mike": 50,
#                "nancy": 70,
#                "olivia": 90,
#                "paul": 60,
#                "quinn": 80,
#                "robert": 50,
#                "sally": 70,
#                "tom": 90,
#                "victor": 60,
#                "william": 80,
#                "xavier": 50,
#                "yvonne": 70,
#                "zoe": 90
#                }

# passed_students = {student: value for (
#     student, value) in report_card.items() if value >= 80}
# print(passed_students)


# ...................................................

# wordinthesentense = "What is the Airspeed Velocity of an Unladen Swallow?"


# result = {word: len(word) for word in wordinthesentense.split()}
# print(result)
# ...................................................

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24}

weather_f = {key: value*9/5+32 for (key, value) in weather_c.items()}
weather_c = {**weather_c, "dryday": 20}  # add new item
print(weather_c)
