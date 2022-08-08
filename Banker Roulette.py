#day4(banker Roulette)
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
num_items = len(names)
random_choice = random.randint(0, num_items  - 1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is going to buy the meal today !")

#day4(treasure map)
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizonal = int(position[0])
vertical = int(position[1])
map[vertical - 1][horizonal - 1] ="X"

print(f"{row1}\n{row2}\n{row3}")
