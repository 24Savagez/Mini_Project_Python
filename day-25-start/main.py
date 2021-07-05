# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #
# #     print(temperatures)
#
# import pandas
#
# # data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(data["temp"])
#
# # data_dict = data.to_dict()
# # print(data_dict)
# #
# # temp_list = data["temp"].to_list()
# # print(temp_list)
# #
# # print(data["temp"].mean())
# # print(data["temp"].max())
# #
# # # Get data in columns
# # print(data["condition"])
# # print(data.condition)
#
# # Get data in row
# # print(data[data.day == "Monday"])
# # print(data[data.temp == data.temp.max()])
#
# # monday = data[data.day == "Monday"]
# # monday_temp = int(monday.temp)
# #
# # print(monday.temp * 9/5 + 32)
#
# # Create a dataframe for scratch
# data_dict = {
#     "students": ["First", "May", "Pam", "Pond"],
#     "scores": [95, 90, 94, 95]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

print(grey_squirrels_count)
print(cinnamon_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur color": ["grey", "cinnamon", "black"],
    "Count": [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}
print(data_dict)
data = pandas.DataFrame(data_dict)
data.to_csv("squirrel_count.csv")
