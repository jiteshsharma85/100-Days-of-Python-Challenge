#numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

#squared_numbers = [i * i for i in numbers]

# result = [i for i in numbers if i % 2 == 0]



# with open("file1.txt") as file1:
#     a = file1.readlines()
#
#
# with open("file2.txt") as file2:
#     b = file2.readlines()
#
# list_3 = [int(num.strip()) for num in a if num in b]
#
#
# print(list_3)


# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"


# list = sentence.split()
#
# result = {word: len(word) for word in list}
#
# print(result)


weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday":15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24
}

weather_f = {key: (c*9/5) + 32 for (key, c) in weather_c.items()}


print(weather_f)








