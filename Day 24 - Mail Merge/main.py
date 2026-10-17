with open("Input/Letters/starting_letter.txt", "r") as file:
    k = file.read()


with open("Names/invited_names.txt", "r") as names:
    for name in names:
        name = name.strip()
        p = k.replace("[name]", name)

        with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w+") as final:
            final.write(p)


