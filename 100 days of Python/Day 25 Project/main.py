# Day 24 - Working with CSV files


import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# # print(data["temp"])

data_dict = data.to_dict()   
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

average = sum(temp_list) / len(temp_list)
print(average)

print(data["temp"].mean())
data["temp"] = data["temp"] * 9/5 + 32
print(data["temp"].max())
print(data[data.temp == data.temp.max()])
