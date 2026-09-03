# 1. datetime module
import datetime
"""
Gets the exact date and time right now
arguments: none
returns: current date and time object
"""
now = datetime.datetime.now()
print("exact time right now:", now)

"""
Gets only today date without time
arguments: none
returns: today date object
"""
today = datetime.date.today()
print("today date is:", today)

"""
Makes your own custom date
arguments: year, month, day
returns: custom date object
"""
custom = datetime.date(2026, 12, 25)
print("custom date is:", custom)

"""
Changes date object into simple text format
arguments: text format code like %Y-%m-%d
returns: formatted text string
"""
text = now.strftime("%Y-%m-%d")
print("formatted date is:", text)

"""
Creates a time gap like days or hours
arguments: number of days or hours
returns: time gap object
"""
gap = datetime.timedelta(days=5)
future = today + gap
print("date after 5 days is:", future)


# 2. time module
import time
"""
Gets computer clock ticks since year 1970
arguments: none
returns: decimal number of seconds
"""
tick = time.time()
print("total ticks till now:", tick)

"""
Pauses the code for some seconds
arguments: number of seconds to wait
returns: nothing
"""
print("waiting for 2 seconds")
time.sleep(2)
print("done waiting")


# 3. math module
import math
"""
Finds the square root of a number
arguments: any number
returns: decimal square root number
"""
root = math.sqrt(64)
print("square root of 64 is:", root)

"""
Multiplies a number by itself many times
arguments: base number, power number
returns: decimal power result
"""
power = math.pow(3, 2)
print("3 power 2 is:", power)

"""
Forces a decimal number up to next whole number
arguments: decimal number
returns: bigger whole number
"""
up = math.ceil(5.2)
print("round up 5.2 is:", up)

"""
Forces a decimal number down to lower whole number
arguments: decimal number
returns: smaller whole number
"""
down = math.floor(5.8)
print("round down 5.8 is:", down)

"""
Multiplies all whole numbers down to 1
arguments: positive whole number
returns: multiplied whole number
"""
fact = math.factorial(5)
print("factorial of 5 is:", fact)


# 4. random module
import random
"""
Picks a random whole number in your range
arguments: start number, end number
returns: random whole number
"""
num = random.randint(1, 100)
print("random no. between 1 and 100 is:", num)

"""
Picks a random decimal between 0 and 1
arguments: none
returns: random decimal number
"""
dec = random.random()
print("random no. is:", dec)

"""
Picks one random item from a list
arguments: a list of items
returns: one single item
"""
colors = ["red", "blue", "green"]
pick = random.choice(colors)
print("random pick is:", pick)

"""
Mixes up the order of a list randomly
arguments: a list
returns: nothing
"""
numbers = [1, 2, 3, 4]
random.shuffle(numbers)
print("suffled numbers are:", numbers)

"""
Picks many unique random items from a list
arguments: a list, how many items to pick
returns: new list of picked items
"""
lots = [10, 20, 30, 40]
some = random.sample(lots, 2)
print("two random picks are:", some)


# 5. uuid module
import uuid
"""
Creates a long random unique token id
arguments: none
returns: unique id object
"""
uid = uuid.uuid4()
print("new uuid is:", uid)


# 6. higher order functions
"""
Arranges list items from small to big
arguments: a list
returns: new sorted list
"""
marks = [50, 10, 80]
sort = sorted(marks)
print("arranged small to big:", sort)

"""
Runs a function on every item in a list
arguments: a function name, a list
returns: map object
"""
def double(x):
    return x * 2

prices = [10, 20, 30]
maps = list(map(double, prices))
print("doubled prices using map:", maps)

"""
Checks all items and keeps only passing ones
arguments: a test function name, a list
returns: filter object
"""
def passmark(x):
    return x > 50

scores = [40, 90, 30, 70]
evens = list(filter(passmark, scores))
print("passed scores using filter:", evens)


import functools

"""
Squashes a list into one final answer using math
arguments: a math function name, a list
returns: one single final answer
"""
def add(x, y):
    return x + y

bills = [10, 20, 30]
total = functools.reduce(add, bills)
print("total bill amount using reduce:", total)