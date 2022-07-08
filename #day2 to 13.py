#day1 (2) fixing code
print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

#day1 (3)input  function
print(len(input("what is your name?")))

#day1 (4) variable
a = input("a: ")
b = input("b: ")
c=a
a=b
b=c
print("a: " + a)
print("b: " + b)

#day2(data types)
two_digit_number = input("Type a two digit number: ")

first_digit=two_digit_number[0]
second_digit=two_digit_number[1]
result=int(first_digit)+int(second_digit)
print(result)

#day2(BMI calculator)

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

weight_as_int=int(weight)
height_as_float=float(height)
bmi = weight_as_int/ height_as_float **2
bmi_as_int = int(bmi)
print(bmi_as_int)

#day2(Life in weeks)
age = input("What is your current age?")

year_remaining = 90-int(age)
day_remaining = year_remaining * 365
week_remaining = year_remaining * 52
month_remaining = year_remaining * 12
message= f"You have {day_remaining} days, {week_remaining} weeks, and {month_remaining} months left."
print(message)

#day3(Odd or Even)

number = int(input("Which number do you want to check? "))
if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")

#day3(BMI 2.0)
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round (weight / height ** 2)
if bmi < 18.5:
    print(f"Your mi is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you have a mormal weight.")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are  slightly overweight.")  
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are obese.")  
else:
    print(f"Your bmi is {bmi}, you are clinicaly obese.")      

#day3(Leap Year)
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year%400 == 0:
         print("Leap year.")
        else:
         print("Not leap year.")
    else:
        print("Leap year.") 
else:
    print("Not leap year.")     

#day3 (Pizza Order Practice)    
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0
if size == "S":
  bill += 15
elif size == "M":
  bill += 20   
else:
  bill += 25

if add_pepperoni =="Y":
    if size == "S":
       bill += 2  
    else:   
       bill += 3
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is ${bill}.")   

#days(love calculate)
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_string = name1 + name2
lower_case_string = combined_string.lower()
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e 

love_score = int(str(true) + str(love))
if(love_score < 10) or (love_score > 90):

 print(f"Your love score is {love_score},   you go together like cake and mentos.")
elif ( love_score >= 40) and (love_score<=50):
 print(f"Your love score is {love_score}, you are alright together.")

else:
     print(f"Your score is {love_score}.")

#day4 (Heads or Tails)
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
import random 
random_side = random.randint(0, 1)
if random_side == 1:
 print("Heads")
else:
 print("Tails") 

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

#day5(average height)
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
total_height = 0
for height in student_heights:
    total_height += height

number_of_students = 0
for student in student_heights:
    number_of_students +=1

average_height = round(total_height/number_of_students) 

print(average_height)

#day5(high score)
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
highest_score = 0
for score in student_scores:
 if score>highest_score:
  highest_score = score
print(f"The highest score in the class is :{highest_score}")        

#day5(average even number)

total = 0
for number in range(2, 101, 2):
 total += number
print(total)

#day5(fizzbuzz)
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz") 
    else:
        print(number) 

#day8(paint area calculator)
import math

def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"You'll need {num_of_cans} cans of paint." )
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

#day8(prime numbers)
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
      if number % i == 0:
        is_prime = False
    if is_prime:
      print("It's a prime number.")
    else:
      print("It's not a prime number.")        
n = int(input("Check this number: "))
prime_checker(number=n)

#day9(grading program)
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
 
for student in student_scores:
    score = student_scores[student]
    if score > 90:
      student_grades[student] = "Outstanding"
    elif score > 80:
      student_grades[student] = "Exceeds Expectations"
    elif score > 70:
      student_grades[student] = "Acceptable"
    else:
      student_grades[student] = "Fail"
print(student_grades)

#day9(dictionary in list)
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

#day10(days in month)
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
        return True
  else:
    return False
    
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if month > 12 or month < 1:
    return "Invalid month entered."
  if month == 2 and is_leap(year):
    return 29
  return month_days[month - 1]

#day13(debugging odd or even)
number = int(input("Which number do you want to check?"))

if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
  
#day13(debugging leap year)
year = int(input("Which year do you want to check?"))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")

#day13(debugging fizzbuzz)  
  for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number) 







         






