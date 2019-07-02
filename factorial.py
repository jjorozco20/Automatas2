#Name: factorial.py
#Objetive: Get a factorial's calculator that will get user variables, loops for menus 
#and comparational sentences.
#Author: José Juan Orozco
#Date: June 29th, 2019

#------------------------------------------------------------------------
#Importing the math library
#------------------------------------------------------------------------
import math as mat
#------------------------------------------------------------------------
#Function to calculate factorial
#------------------------------------------------------------------------
def fact(var1):
    print("Number's factorial: ", mat.factorial(var1))
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
        print("Number's factorial")
        print("\n")
        var1 = int(input("Input the number that you want to calculate: "))
        #Call Function
        fact(var1)
        cad = input ("Do you want to do another calculate? (Y/N) ")
        if (cad == "Y" or cad== "y"):
            loop = True
        else: 
            loop = False
#------------------------------------------------------------------------
#Declare the main method's entrance
#------------------------------------------------------------------------
if __name__ == "__main__":
    main()