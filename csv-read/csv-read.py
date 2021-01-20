# Work with CSV
import csv


with open("weather_data.csv") as data_file:
  #data = data_file.readlines()
  # readlines returns ['day,temp,condition\n', 'Monday,12,Sunny\n', 'Tuesday,14,Rain\n', 'Wednesday,15,Rain\n', 'Thursday,14,Cloudy\n', 'Friday,21,Sunny\n', 'Saturday,22,Sunny\n', 'Sunday,24,Sunny']
  data = csv.reader(data_file)
  for row in data:
    print(row)


print(data)