
# import csv
#
# with open("./weather-data.csv") as file:
#     data = csv.reader(file)
#     temp = []
#     for row in data:
#
#         if row[1] != "temp":
#             temp.append(row[1])
#     print(temp)

#import pandas
#
#
# panda_data_frame = pandas.read_csv("weather-data.csv")
# panda_series = panda_data_frame["temp"]
#
# # max = panda_series.max()
# # print(panda_data_frame[panda_data_frame.temp == max])
#
# monday = panda_data_frame[panda_data_frame.day == "Monday"]
#
# F = 9/5 * monday.temp + 32
#
# print(F)
import pandas

squirrel_data = pandas.read_csv("squirl_data.csv")

fur_colors = ["Gray", "Black", "Cinnamon", "White"]
counts = [len(squirrel_data[squirrel_data["Primary Fur Color"] == color]) for color in fur_colors]

summary = pandas.DataFrame({"Fur Color": fur_colors, "Count": counts})
print(summary)

summary.to_csv("./count.csv", index=False)