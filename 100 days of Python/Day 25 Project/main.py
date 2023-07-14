# Day 24 - Working with CSV files

with open("weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)

    