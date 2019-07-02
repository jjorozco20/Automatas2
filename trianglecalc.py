#Name: trianglecalc.py
#Objetive: Get an operational condition's calculator that will get user variables 
#and import math library and making a clear screen each time that the 
#loop will enter using Operative System's library.
#Author: José Juan Orozco
#Date: June 29th, 2019


#------------------------------------------------------------------------
#Calculate triangle's type method
#------------------------------------------------------------------------
def calculateType(base, side1, side2):
    if (base == side1 and side2==base):
        print("It is an equilateral triangle.")
    elif (base != side1 and side2==side1):
        print("It is an isosceles triangle.")
    else:
        print("It is an scalene triangle.")

#------------------------------------------------------------------------
#Importing the clear screen function whit Operative System library
#------------------------------------------------------------------------
import os

def main():
    ciclo = True
    while ciclo == True:

        print("Script to calculate triangle's type of")
        base = float(input("Input the base's value: "))
        side1 = float(input("Input the side one's value: "))
        side2 = float(input("Input the side two's value: "))
        #Invoke a method
        calculateType(base, side1, side2)
        
        response= input("Do you want to do another calcule? (S/N)")
        if (response == "S" or response == "s"):
            ciclo= True
            #------------------------------------------------------------
            #Making the clear screen
            #------------------------------------------------------------
            os.system("cls")
        else: 
            ciclo= False
    else: 
        print("End of script.")

if __name__ == "__main__":
    main()