alldata = []


def creationofarr():
    """
    This function asks for creating 1D or 2D array and then takes elements input and stores array in global variable.
    It doesn't takes any argumments
    Return value:1D or 2D array based on user selected input
    """
    arr = input("enter 1D array or 2D array: ")
    if arr == "1":
        odinp = input("enter elements of 1D array with space: ")
        arrod = list(map(int, odinp.split()))
        alldata.extend(arrod)
        return arrod
    elif arr == "2":
        row = int(input("enter no of rows: "))
        cols = int(input("enter no of columns: "))
        tdarrlist = []
        for i in range(row):
            arrod = []
            for j in range(cols):
                odinp = int(input(f"enter element for row {i+1} col {j+1}: "))
                arrod.append(odinp)
            tdarrlist.append(arrod)
        for i in tdarrlist:
            for j in i:
                alldata.append(j)
        return tdarrlist


def disdata():
    """
    Shows stored data and gives option to display summary or clear data.
    Arguments: None
    Return value: None
    """
    global alldata
    print(alldata)
    if len(alldata) == 0:
        print("no data stored yet!")
        return
    print("""which array you stored?
        1. summary
        2. clear data """)
    arrstrd = int(input("enter choice: "))
    if arrstrd == 1:
        print(f"""summary:
                -total elements: {len(alldata)}
                -min value: {min(alldata)}
                -max value: {max(alldata)}
                -sum: {sum(alldata)}
                -average: {sum(alldata)/len(alldata)}""")
    elif arrstrd == 2:
        alldata.clear()
        print("all data cleared!")


def calcfact(n):
    """
    Calculates factorial of a number using recursion.
    Arguments: n (input number)
    Return value: Factorial of n
    """
    if n == 1:
        return 1
    return n * calcfact(n - 1)


def filterthresh():
    """
    Filters and prints numbers greater than the user's limit using lambda.
    Arguments: None
    Return value: None
    """
    if len(alldata) == 0:
        print("no data stored yet!")
        return
    thresh = int(input("enter threshold value: "))
    res = list(filter(lambda x: x > thresh, alldata))
    print(f"elements greater than {thresh}:", res)


def sortmydata(arr):
    """
    Sorts the array in ascending or descending order .
    Arguments: arr (list) 
    Return value: Sorted list
    """
    return sorted(arr)


def getstats(*args):
    """
    Calculates min, max, total sum, and average of all numbers using *args.
    Arguments: *args (multiple numbers)
    Return value: Tuple of 4 values (min, max, total, avg)
    """
    mn = min(args)
    mx = max(args)
    tot = sum(args)
    av = tot / len(args)
    return mn, mx, tot, av


while True:
    print("\nData Analyzer and Transformer Program")
    print("""Menu:
    1. Input Data
    2. Display Data Summary or clear data
    3. Calculate Factorial
    4. Filter Data by Threshold
    5. Sort Data
    6. Display Dataset Statistics
    7. Exit Program
    """)
    userinp = input("enter choice: ")

    if userinp == "1":
        print(creationofarr())
        print("data stored successfully!")

    elif userinp == "2":
        disdata()

    elif userinp == "3":
        num = int(input("enter number for factorial: "))
        if num <=0:
            print("factorial not possible for negative numbers!")
        else:
            print(f"factorial of {num} is:", calcfact(num))

    elif userinp == "4":
        filterthresh()

    elif userinp == "5":
        if len(alldata) == 0:
            print("no data stored yet!")
        else:
            print("1. Ascending")
            print("2. Descending")
            ch = input("enter choice (1 or 2): ")
            if ch == "1":
                print("sorted ascending:", sortmydata(alldata))
            elif ch == "2":
                z=sortmydata(alldata)
                print("sorted descending:", z[::-1])
            else:
                print("invalid choice!")

    elif userinp == "6":
        if len(alldata) == 0:
            print("no data stored yet!")
        else:
            mn, mx, tot, av = getstats(*alldata)
            print(f"""statistics:
                - min: {mn}
                - max: {mx}
                - total: {tot}
                - average: {av}""")

    elif userinp == "7":
        print("thank you! goodbye!")
        print("UDF 1: ", creationofarr.__doc__)
        print("UDF 2: ", disdata.__doc__)
        print("UDF 3: ", calcfact.__doc__)
        print("UDF 4: ", filterthresh.__doc__)
        print("UDF 5: ", sortmydata.__doc__)
        print("UDF 6: ", getstats.__doc__)
        break
        
    else:
        print("invalid choice")

