#day2(Life in weeks)
age = input("What is your current age?")

year_remaining = 90-int(age)
day_remaining = year_remaining * 365
week_remaining = year_remaining * 52
month_remaining = year_remaining * 12
message= f"You have {day_remaining} days, {week_remaining} weeks, and {month_remaining} months left."
print(message)
