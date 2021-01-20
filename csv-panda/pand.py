import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])

# Two types of data in Pandas:
#  DataFrame: 2D data - Tables
#  Series: 1D data - Columns of data(as lists)
print(type(data))

data_dict = data.to_dict()
print(data_dict)

temp_list= data["temp"].to_list()
print(temp_list)

# Get data in Rows
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

# create datafram from some lists
data_dict2 = {
  "students": ["Amy", "James", "Angels"],
  "scores": [74,89,34]
}
data2 = pandas.DataFrame(data_dict2)
data.to_csv("new_data.csv")