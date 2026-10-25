import pandas


file = pandas.read_csv("nato_phonetic_alphabet.csv")

dictionary = {rows.letter: rows.code for (index, rows) in file.iterrows()}

#print(dictionary)

user_input =  input("Enter your name: ").upper()

#print(user_input)


#result = [dictionary.get(letter) for letter in user_input]

result = [dictionary[letter] for letter in user_input]

print(result)