#Name: cincumference.py
#Objetive: Get an area and diam's calculator that will get user variables 
#and import math library and making a clear screen each time that the 
#loop will enter using Operative System's library.
#Author: José Juan Orozco
#Date: June 29th, 2019

#------------------------------------------------------------------------
#Importing the math library
#------------------------------------------------------------------------
import math as mat
#------------------------------------------------------------------------
#Calculate area's method
#------------------------------------------------------------------------
def calculateArea(r):
    area = mat.pi*(mat.pow(r,2))
    return area
#------------------------------------------------------------------------
#Calculate diameter's method
#------------------------------------------------------------------------
def calculateDiameter(d):
    diameter = d*2
    return diameter
#------------------------------------------------------------------------
#Importing the clear screen function whit Operative System library
#------------------------------------------------------------------------
import os
def main():
    ciclo = True
    while ciclo == True:

        print("Script to calculate circle's area")
        radix = float(input("Input the radix value: "))

        #Invoke a method
        print("Circle's area: ",calculateArea(radix))
        print("Circle's diameter: ", calculateDiameter(radix))
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