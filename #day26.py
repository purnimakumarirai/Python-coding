#day26(squaring number)
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [num**2 for num in numbers]
print(squared_numbers)

#day26(data overlap)
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

result = [num for num in numbers if num %2 ==0 ]
print(result)

#day26(dictionary compregension1)
with open("file1.txt") as file1:
  file_1_data = file1.readlines()
with open("file2.txt")  as file2:
  file_2_data = file2.readlines()

  result = [int(num) for num in file_1_data if num in file_2_data]

print(result)

#day26(dictionary compregension2)
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
sentence_c = {
    "What": 4,
    "is": 2,
    "the": 3,
    "Airspeed": 8,
    "Velocity": 8,
    "of": 2,
    "an": 2,
    "Unladen": 7,
    "Swallow": 8
}
result =  {sentence for sentence in sentence_c}

print(result)
