# Day 24 - Working with CSV files


import pandas
import csv

# data = pandas.read_csv("weather_data.csv")
# # # print(type(data))
# # print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)


# temp_list = data["temp"].to_list()
# print(len(temp_list))

# # average = sum(temp_list) / len(temp_list)
# # print(average)



# # print(data["temp"].mean())
# # print(data["temp"].max())

# # # Get data in columns

# # print(data["condition"])
# # print(data.condition)


# # Get data in rows 

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)


# create a dataframe from scratch

data_dict = {
    "students": ["Alex", "James", "Geni"],
    "scores": [80, 79, 93]

}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")






