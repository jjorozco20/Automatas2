#Name: calc.py
#Objetive: Get a calculator that will get user variables, loops for menus 
#and comparational sentences.
#Author: José Juan Orozco
#Date: June 29th, 2019


#------------------------------------------------------------------------
#Function to add numbers
#------------------------------------------------------------------------
def add(var1, var2):
    return  var1+var2
#------------------------------------------------------------------------
#Function to subtract numbers
#------------------------------------------------------------------------
def rest(var1, var2):
    return var1-var2
#------------------------------------------------------------------------
#Function to multiply numbers
#------------------------------------------------------------------------
def mult(var1, var2):
    return var1*var2 
#------------------------------------------------------------------------   
#Function to divide 
#------------------------------------------------------------------------
def divide(var1, var2):
    return var1/var2
#------------------------------------------------------------------------
#Function to compare numbers
#------------------------------------------------------------------------
def compare(var1, var2):
    if (var1>var2):
        print("The higher number is: ", var1)

    elif (var2>var1):
        print("The higher number is: ", var2)

    else:
        print("Both numbers are equals", var1, ", ", var2)

#------------------------------------------------------------------------
    #Declare a loop (FOR) to enter into the calculator at least twice
#------------------------------------------------------------------------
def count(var1, var2):
    if(var2>=var1):
        for i in range(var1, var2+1):
            print("i's value: ", i)
    if (var1>var2):
        for i in range(var2, var1-1, -1):
            print("i's value: ", i)
#------------------------------------------------------------------------
#Main Method
#------------------------------------------------------------------------
def main():
    #------------------------------------------------------------------------
    #Declare a loop (WHILE) to enter into the calculator at least twice
    #------------------------------------------------------------------------
    loop = True
    while (loop == True):
    #------------------------------------------------------------------------   
        print("Basic calculator's functions")
        print("\n")
        var1 = int(input("Input the first number: "))
        var2 = int(input("Input the second number: "))
            
        #Call functions
        print("Result of sum: " + str(add(var1, var2)))
        print("Result of subtract: " + str(rest(var1, var2)))
        print("Result of multiplication: " + str(mult(var1, var2)))
        print("Result of divide: " + str(divide(var1, var2)))
        compare(var1, var2)
        count(var1, var2)
        cad = input ("Do you want to do another calculate? (Y/N)")
        if (cad == "Y" or cad== "y"):
            loop = True
        else: 
            loop = False
#------------------------------------------------------------------------
#Declare the main method's entrance
#------------------------------------------------------------------------
if __name__ == "__main__":
    main()