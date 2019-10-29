'''
This script detects if an input is integer or float or string.

Pros:
It can also detect if a given input has only float/integer despite of it being in form of a string.
For example, if the input is '258'. It will detect it as an integer and not string.
Same for the float.

Limitations:
The logic breaks if anything other than int/str/float is input.
This limitation may be removed in later iterations of the script.
'''

def takeInput():  #takes input
    inp = input("Enter Integer/Float/String: \n")
    makeStringCheckDot(inp)

def floatVsString(stringEntered): #Checks for float or string (FN3)
    #print("InFN3")
    try:
        floatInput = float(stringEntered)
        print("Input is a float.")
    except:
        if type(stringEntered) == type('abc'):
            print("Input is a string.")
        else:
            somethingElse()

def intVsSomethingElse(stringEntered): #checks for integer or string (FN2)
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
    
def makeStringCheckDot(x):   #Makes input a string and checks for demical (FN1)
    stringEntered = str(x).strip()
    if '.' in stringEntered:
        floatVsString(stringEntered)
    else:
        intVsSomethingElse(stringEntered)

takeInput() #calls for input
