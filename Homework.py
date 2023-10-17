# List Sorter: Accept a list of numbers from the user and print the sorted list. 

numberofnumbers = (input("How many numbers?"))

list = []
i=1
while i <= int(numberofnumbers):
  i+=1
  nextnumber = input("Please give number")
  list.append(nextnumber)

list.sort()
print (list)

#Age Calculator: Ask the user for their birth year and calculate their age.

thisyear = 2023

birthyear = int(input("Which year were you born?"))

age = thisyear - birthyear

print(f"You are {age} years old.")

#Temperature Converter: Convert temperatures from Celsius to Fahrenheit and vice versa. 

degree = input ("What would you like to convert? Celsius or Fahrenheit?")

while degree.lower() != "celsius" and degree.lower() != "fahrenheit":
  degree = input ("What would you like to convert? Celsius or Fahrenheit?")

temp = int(input("What is the degree to convert?"))

if degree.lower() == "celsius":
  tempnew = temp * 9/5 + 32
  print (f"{temp} {degree} is equal to {tempnew} Fahrenheit.")

else:
  tempnew = temp / 9/5 + 32
  print (f"{temp} {degree} is equal to {tempnew} Celsius.")


#Simple Calculator: Create a program that can add, subtract, multiply, and divide two numbers based on user input. 

def add (x,y):
  return x+y

def subs (x,y):
  return x-y

def mult (x,y):
  return x*y

def div (x,y):
  return x/y

whattodo = input ("Please define what you would like to do: add/substract/multiply/divide")

while whattodo.lower() != "add" and whattodo.lower() != "substract" and whattodo.lower() != "multiply" and whattodo.lower() != "divide":
  whattodo = input ("Invalid input.\nPlease define what you would like to do: add/substract/multiply/divide")

first = float(input("Please give 1st number:"))
second= float(input("Please give 2nd number:"))

if whattodo == "add":
  result = add (first, second)
  print (f"The result is {result}.")

elif whattodo == "substract":
  result = subs (first, second)
  print (f"The result is {result}.")

elif whattodo == "multiply":
  result = mult (first, second)
  print (f"The result is {result}.")

elif whattodo == "divide":
  result = div (first, second)
  print (f"The result is {result}.")

#Word Counter: Accept a sentence from the user and count how many words it contains.

sentence = input("Please provide the sentence")
wordcounter = sentence.split( )
print("This sentence is", len(wordcounter), "words long.")


#Days Until Birthday: Using the datetime library, ask the user for their birthday and calculate how many days are left until their next birthday. 

import datetime

yourbday = input("When were you born? \nPlease provide YYYYMMDD format: ")

bdayyear = int(yourbday[0:4])
bdaymonth = int(yourbday[4:6])
bdayday = int(yourbday[6:8])

birthday = datetime.datetime(year=bdayyear, month=bdaymonth, day=bdayday)

current_date = datetime.datetime.now()

next_birthday = birthday.replace(year=current_date.year)

if current_date > next_birthday:
    next_birthday = next_birthday.replace(year=current_date.year + 1)

days_until_birthday = (next_birthday - current_date).days

print(f"You have {days_until_birthday} days left until your next birthday.")

#Random Number Guesser: Using the random library, generate a random number between 1 and 100 and let the user guess it. Provide feedback on whether the guess is too high, too low, or correct.

import random

selected = random.randint(0,101)

guess = int(input("Guess a number!"))

while selected != guess:
  if selected > guess:
    print ("The guessed number is smaller than the random number.")
    guess = int(input("Guess a number!"))
    print (selected)
  else:
    print ("The guessed number is larger than the random number.")
    guess = int(input("Guess a number!"))
    print (selected)

print ("Congratulations, you found the number!")


#Simple Alarm Clock: Ask the user to set a time, and when that time is reached, display a message.

import datetime
import time

alarm = input("For when do you want to set the alarm? Please provide hour:minute in 24-hour format - e.g. 14:24: ")

alarmhour = int(alarm[0:2])
alarmminute = int(alarm[3:])

currenttime = datetime.datetime.now()

alarmtime = currenttime.replace(hour=alarmhour, minute=alarmminute, second=0, microsecond=0)

if currenttime > alarmtime:
    alarmtime = alarmtime + datetime.timedelta(days=1)

time_difference = alarmtime - currenttime

time.sleep(time_difference.total_seconds())

print("Your alarm is set for now:", alarmtime)

#Currency Converter: Using a third-party library like forex-python, create a program that can convert one currency to another based on current exchange rates. 

from forex_python.converter import CurrencyRates

currency_converter = CurrencyRates()

amount = float(input("How much to convert? "))
from_currency = input("What is the currency you want to convert from (e.g., USD)?").upper()
to_currency = input("What is the currency you want to convert to (e.g., EUR)? ").upper()

converted_amount = currency_converter.convert(from_currency, to_currency, amount)

print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
