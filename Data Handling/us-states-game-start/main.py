# import csv
# with open("226 weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     # # print a row
#     # for i, row in enumerate(data):
#     #     if i == 1:
#     #         print(row)

#     temperatures = []
#     for col in data:
#         if col[1] != "temp":
#             temperatures.append(int(col[1]))
#     print(temperatures)

import pandas

pandas_data = pandas.read_csv("226 weather_data.csv")
temperatures = pandas_data["temp"].to_list()
print(pandas_data)
print(temperatures)
print(pandas_data.loc[1])
