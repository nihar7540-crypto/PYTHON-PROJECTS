def makefile():
    """
    This function makes a new empty file.
    Arguments: None
    Returns: None
    """
    print("Enter filename")
    name = input()
    file = open(name, "w")
    file.close()
    print("Created")

def writefile():
    """
    This function writes text to a file.
    Arguments: None
    Returns: None
    """
    print("Enter filename")
    name = input()
    print("Enter text")
    text = input()
    file = open(name, "a")
    file.write(text)
    file.close()
    print("Written")

def readfile():
    """
    This function reads text from a file.
    Arguments: None
    Returns: None
    """
    print("Enter filename")
    name = input()
    file = open(name, "r")
    text = file.read()
    print(text)
    file.close()
