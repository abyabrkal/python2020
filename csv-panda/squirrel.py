import pandas


data = pandas.read_csv("2018_Central_Park_Squirrel_Census.csv")
gray_sq = len(data[data["Primary Fur Color"] == "Gray"])
red_sq = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_sq = len(data[data["Primary Fur Color"] == "Black"])

data_dic = {
  "Fur Color": ["Gray", "Cinnamon", "Black"],
  "count": [gray_sq, red_sq, black_sq]
}
print(data_dic)

df = pandas.DataFrame(data_dic)
df.to_csv("squirrel_count.csv")
print(df)