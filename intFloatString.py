def takeInput():
    inp = input("Enter Integer/Float/String: \n")
    makeStringCheckDot(inp)

def floatVsString(stringEntered): #FN3
    #print("InFN3")
    try:
        floatInput = float(stringEntered)
        print("Input is a float.")
    except:
        if type(stringEntered) == type('abc'):
            print("Input is a string.")
        else:
            somethingElse()

def intVsSomethingElse(stringEntered): #FN2
    #print("InFN2")
    try:
        intInput = int(stringEntered)
        print("Input is an integer.")
    except:
        if type(stringEntered) == type('abc'):
            print("Input is a string.")
        else:
            somethingElse()
    
def somethingElse(): #FN4
    #can be coded further to check for other data types
    print("Input is something else.")
    
def makeStringCheckDot(x):   #FN1
    stringEntered = str(x).strip()
    if '.' in stringEntered:
        floatVsString(stringEntered)
    else:
        intVsSomethingElse(stringEntered)

takeInput()
