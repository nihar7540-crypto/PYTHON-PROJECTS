import datetime
import time
import math
import random
import uuid
import filemodule

def showtime():
    """
    This function prints the current time.
    Arguments: None
    Returns: None
    """
    now = datetime.datetime.now()
    print(now)

def datediff():
    """
    This function calculates difference between dates.
    Arguments: None
    Returns: None
    """
    print("Enter first date YYYY-MM-DD")
    dateone = input()
    print("Enter second date YYYY-MM-DD")
    datetwo = input()
    done = datetime.datetime.strptime(dateone, "%Y-%m-%d")
    dtwo = datetime.datetime.strptime(datetwo, "%Y-%m-%d")
    diff = dtwo - done
    print("Days difference is")
    print(diff.days)

def customformat():
    """
    This function formats the current date.
    Arguments: None
    Returns: None
    """
    now = datetime.datetime.now()
    result = now.strftime("%d %B %Y")
    print(result)

def runstopwatch():
    """
    This function runs a simple stopwatch.
    Arguments: None
    Returns: None
    """
    print("Press enter to start")
    input()
    start = time.time()
    print("Press enter to stop")
    input()
    end = time.time()
    diff = end - start
    print("Seconds passed")
    print(diff)

def runcountdown():
    """
    This function runs a countdown timer.
    Arguments: None
    Returns: None
    """
    print("Enter seconds")
    secs = int(input())
    while secs > 0:
        print(secs)
        time.sleep(1)
        secs = secs - 1
    print("Done")

def calcfactorial():
    """
    This function calculates the factorial.
    Arguments: None
    Returns: None
    """
    print("Enter number")
    number = int(input())
    result = math.factorial(number)
    print(result)

def calctrig():
    """
    This function calculates sine value.
    Arguments: None
    Returns: None
    """
    print("Enter angle")
    angle = float(input())
    result = math.sin(angle)
    print(result)

def calcinterest():
    """
    This function calculates compound interest.
    Arguments: None
    Returns: None
    """
    print("Enter principal")
    prin = float(input())
    print("Enter rate")
    rate = float(input())
    print("Enter years")
    year = float(input())
    amount = prin * (math.pow((1 + rate / 100), year))
    print(amount)

def calcarea():
    """
    This function calculates circle area.
    Arguments: None
    Returns: None
    """
    print("Enter radius")
    radius = float(input())
    area = math.pi * radius * radius
    print(area)

def randnum():
    """
    This function generates a random number.
    Arguments: None
    Returns: None
    """
    result = random.randint(1, 100)
    print(result)

def randlist():
    """
    This function samples from a list.
    Arguments: None
    Returns: None
    """
    things = ["cricket", "minecraft", "burger", "watch", "laptop"]
    result = random.sample(things, 2)
    print(result)

def randpass():
    """
    This function generates a random password.
    Arguments: None
    Returns: None
    """
    print("Enter length")
    size = int(input())
    letters = "qwertyuiop1234567890asdfghjkl"
    word = ""
    for index in range(size):
        word = word + random.choice(letters)
    print(word)

def randotp():
    """
    This function generates a random otp.
    Arguments: None
    Returns: None
    """
    result = random.randint(1000, 9999)
    print(result)

def genuuid():
    """
    This function generates a unique identifier.
    Arguments: None
    Returns: None
    """
    unique = uuid.uuid4()
    print(unique)

def exploremod():
    """
    This function explores module attributes.
    Arguments: None
    Returns: None
    """
    print("Enter module name like math or random")
    name = input()
    if name == "math":
        print(dir(math))
    if name == "random":
        print(dir(random))
    if name == "time":
        print(dir(time))

def printdocs():
    """
    This function prints all docstrings.
    Arguments: None
    Returns: None
    """
    print(showtime.__doc__)
    print(datediff.__doc__)
    print(customformat.__doc__)
    print(runstopwatch.__doc__)
    print(runcountdown.__doc__)
    print(calcfactorial.__doc__)
    print(calctrig.__doc__)
    print(calcinterest.__doc__)
    print(calcarea.__doc__)
    print(randnum.__doc__)
    print(randlist.__doc__)
    print(randpass.__doc__)
    print(randotp.__doc__)
    print(genuuid.__doc__)
    print(exploremod.__doc__)
    print(filemodule.makefile.__doc__)
    print(filemodule.writefile.__doc__)
    print(filemodule.readfile.__doc__)
    print(printdocs.__doc__)
    print(main.__doc__)

def main():
    """
    This function runs the main menu.
    Arguments: None
    Returns: None
    """
    loop = True
    while loop:
        print("Menu")
        print("1 Datetime")
        print("2 Math")
        print("3 Random")
        print("4 UUID")
        print("5 File")
        print("6 Explore")
        print("7 Exit")
        print("Enter choice")
        choice = input()
        
        if choice == "1":
            print("1 Time")
            print("2 Diff")
            print("3 Format")
            print("4 Stopwatch")
            print("5 Countdown")
            print("Enter option")
            option = input()
            if option == "1":
                showtime()
            if option == "2":
                datediff()
            if option == "3":
                customformat()
            if option == "4":
                runstopwatch()
            if option == "5":
                runcountdown()
                
        if choice == "2":
            print("1 Factorial")
            print("2 Interest")
            print("3 Area")
            print("4 Trig")
            print("Enter option")
            option = input()
            if option == "1":
                calcfactorial()
            if option == "2":
                calcinterest()
            if option == "3":
                calcarea()
            if option == "4":
                calctrig()
                
        if choice == "3":
            print("1 Number")
            print("2 Password")
            print("3 OTP")
            print("4 List")
            print("Enter option")
            option = input()
            if option == "1":
                randnum()
            if option == "2":
                randpass()
            if option == "3":
                randotp()
            if option == "4":
                randlist()
                
        if choice == "4":
            genuuid()
            
        if choice == "5":
            print("1 Make")
            print("2 Write")
            print("3 Read")
            print("Enter option")
            option = input()
            if option == "1":
                filemodule.makefile()
            if option == "2":
                filemodule.writefile()
            if option == "3":
                filemodule.readfile()
                
        if choice == "6":
            exploremod()
            
        if choice == "7":
            print("Goodbye")
            printdocs()
            loop = False

if __name__ == "__main__":
    main()
