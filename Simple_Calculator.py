#Python Practical Project Calculator


#Libraries to import
import math

#Standard Menu
def menu():
    print("---------Calculator Menu---------")
    print("1. Standard Arithmetic")
    print("2. Trigonometry")
    print("3. Exponents")
    print("4. Square Root")
    print("5. Percentage")
    print("6. Exit")
    print("---------------------------------")

#Standard Arithmetic - Jun Jie
def addCal():
    num1 = int(input("Please enter a number: "));
    num2 = int(input("Please enter the second number: "));
    results = num1 + num2;
    print("The answer of " + str(num1) + " + " + str(num2) + " is: " + str(results) + "\n");    

def subCal():
    num1 = int(input("Please enter a number: "));
    num2 = int(input("Please enter the second number: "));
    results = num1 - num2;
    print("The answer of " + str(num1) + " - " + str(num2) + " is: " + str(results) + "\n");    

def multiCal():
    num1 = int(input("Please enter a number: "));
    num2 = int(input("Please enter the second number: "));
    results = num1 * num2;
    print("The answer of " + str(num1) + " * " + str(num2) + " is: " + str(results) + "\n");    

def diviCal():
    num1 = int(input("Please enter a number: "));
    num2 = int(input("Please enter the second number: "));
    results = num1 / num2;
    print("The answer of " + str(num1) + " / " + str(num2) + " is: " + str(results) + "\n");    

#Trigonometry - Kevin
def sinCal():
    result = math.sin(math.radians(float(input("Please enter a number: "))))    
    print("The answer is: " + str(result) + " Rads")

def cosCal():
    result = math.cos(math.radians(float(input("Please enter a number: "))))    
    print("The answer is: " + str(result) + " Rads")
    
def tanCal():
    result = math.tan(math.radians(float(input("Please enter a number: "))))    
    print("The answer is: " + str(result) + " Rads")
    
def inverseSinCal():
    while(True):
        trigoValue = float(input("Please enter a number: "))
        if (trigoValue < -1 or trigoValue > 1):
            print("Please enter a value between -1 and 1.")
        break

    result = math.asin(trigoValue)
    print("The answer is: " + str(math.degrees(result)) + " Degrees")
    
def inverseCosCal():
    while(true):
        trigoValue = float(input("Please enter a number: "))
        if (trigoValue < -1 or trigoValue > 1):
            print("Please enter a value between -1 and 1.")
        break
            
    result = math.acos(trigoValue)
    print("The answer is: " + str(math.degrees(result)) + " Degrees")
    
def inverseTanCal():

    while(true):
        trigoValue = float(input("Please enter a number: "))
        if (trigoValue < -1 or trigoValue > 1):
            print("Please enter a value between -1 and 1.")
        break
            
    result = math.atan(trigoValue)
    print("The answer is: " + str(math.degrees(result)) + " Degrees")
    
#Exponents - Samuel
def power(number,exponent):
    initial = number
    for i in range(exponent-1):
        number *= initial
    return number

#Square Root - Tricia
def sqRoot(i):
    if (i < 0):
        print("Please enter a number >=0)")
    else:
        i = math.sqrt(i)
        print(i)

#Percentage - Elgin
def percentage():
    totalNumber = float(input("Please enter the number you want to get percentage of: "))
    percentageNumber = float(input("Please enter the % you want: "))
    decimalNumber = percentageNumber/100
    result = totalNumber * decimalNumber
    print (str(result) + " is your number")


#Code to run


item = True

while(item):
    menu()
    value = int(input("Please enter a number from 1-6: "))
    if (value == 6):
        item  = False
    elif (value == 1):
        print("\nPlease choose which Simple Arithmetic function do u want to calculate.");
        print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division");
        arithmeticSelect = input("Please choose a function: ");
        if(arithmeticSelect == "1"):
            addCal();
        elif(arithmeticSelect == "2"):
            subCal();
        elif(arithmeticSelect == "3"):
            multiCal();
        elif(arithmeticSelect == "4"):
            diviCal();
        else:
            print("PLease choose one of the functions!\n");
    elif (value == 2):
        print("Please choose which Trigometry function do you want to calculate. Values are in degrees")
        print("1. Sin\n2. Cos\n3. Tan\n4. Inverse Sin\n5. Inverse Cos\n6. Inverse Tan")
        trigoSelect = input("Please select a function: ")
        if (trigoSelect == "1"):
            sinCal()
        elif (trigoSelect == "2"):
            cosCal()
        elif (trigoSelect == "3"):
            tanCal()
        elif (trigoSelect == "4"):
            inverseSinCal()
        elif (trigoSelect == "5"):
            inverseCosCal()
        elif (trigoSelect == "6"):
            inverseTanCal()
        else:
            print("Please enter a value between 1-6!")
            print("")
    elif (value == 3):
        print("------------Exponents------------")
        power(int(input("Please enter a number: ")),int(input("Please enter exponent: ")))
    elif (value == 4):
        print ("Please put in your code Tricia")
    elif (value == 5):
        i = float(input("Please enter the number (>=0) you want to square root: "))
        sqRoot(i)
    elif (value == 5):
        percentage()
    elif ((value < 1) or (value > 6)):
        print("Please enter a value between 1-6!")
        print("")
    
