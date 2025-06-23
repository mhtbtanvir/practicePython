# # import csv
# # with open("226 weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     # # print a row
# #     # for i, row in enumerate(data):
# #     #     if i == 1:
# #     #         print(row)

# #     temperatures = []
# #     for col in data:
# #         if col[1] != "temp":
# #             temperatures.append(int(col[1]))
# #     print(temperatures)

# import pandas

# pandas_data = pandas.read_csv("./226 weather_data.csv")
# # temperatures = pandas_data["temp"]
# # print(pandas_data)
# # print(temperatures)
# # avg_temp = sum(temperatures) / len(temperatures)
# # avg_temp = round(pandas_data["temp"].mean(), 2)
# # max_temp = pandas_data.temp.max()

# # for i in range(len(temperatures)):
# #     if temperatures[i] == max_temp:
# #         print(pandas_data.loc[i])
# # print(".......", pandas_data[temperatures == max_temp])


# # for i in temperatures:
# #     print(i)
# # # pandas act as a dictionary and an object

# monday = pandas_data[pandas_data.day == "Saturday"]
# print(monday.temp)

# data_dict = {
#     "students": ["tanvir", "arman ", "rishad", "pleto"],
#     "score": [90, 65, 66, 91]

# }
# data = pandas.DataFrame(data_dict)

# data.to_csv("./cooked_data.csv")


import pandas

cp_data = pandas.read_csv(
    "./228 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

sqrl_color = cp_data["Primary Fur Color"]

Gray_sqrl_count = len(cp_data[sqrl_color == "Gray"])
Cinnamon_sqrl_count = len(cp_data[sqrl_color == "Cinnamon"])
Black_sqrl_count = len(cp_data[sqrl_color == "Black"])
print(Gray_sqrl_count)
print(Cinnamon_sqrl_count)
print(Black_sqrl_count)

data_dict = {
    "fur color": ["Gray", "Cinnamon", "Black"],
    "Squirrels_Count": [Gray_sqrl_count, Cinnamon_sqrl_count, Black_sqrl_count]

}

data_by_color = pandas.DataFrame(data_dict)
data_by_color.to_csv("./squirrel_data_byColor.csv",index=False)
