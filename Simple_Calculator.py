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

#Percentage - Elgin


#Code to run


item = True

while(item):
    menu()
    value = int(input("Please enter a number from 1-6: "))
    if (value == 6):
        item  = False
    elif (value == 1):
        print ("Please put in your code Jun Jie")
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
        print ("Please put in your code Elgin")
    elif ((value < 1) or (value > 6)):
        print("Please enter a value between 1-6!")
        print("")
    
