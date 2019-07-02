#Name: arrays.py
#Objetive: It will show how a list works in python.
#Author: José Juan Orozco
#Date: July 2nd, 2019

#------------------------------------------------------------------------
#Create list
#------------------------------------------------------------------------
miLista = []
#------------------------------------------------------------------------
#Add item to list's method
#------------------------------------------------------------------------
def addItem(dato):
    miLista.append(dato)
#------------------------------------------------------------------------
#Print each element of the list's method
#------------------------------------------------------------------------
def printList():
    j=0
    for i in miLista:
        print("Item: ", j, ", ",i)
        j = j+1
#------------------------------------------------------------------------
#Main method
#------------------------------------------------------------------------
def main():    
    ciclo = True
    while ciclo == True:
        print("--- Script to work with lists ---")
        print("1.- Add item to list")
        print("2.- Search a item in the list")
        print("3.- Modify item in the list")
        print("4.- Delete item in the list")
        print("5.- Print the item of the list")
        print("6.- Exit")

        opc = int(input("Input the number of the option that you want to use: "))
        if (opc == 1):
            item = input("Input a value to add: ")
            addItem(item)
        elif(opc == 2):
            print("Opción dos")
        elif(opc == 3):
            print("Opción tres")
        elif(opc == 4):
            print("Opción cuatro")
        elif(opc == 2):
            print("Opción cinco")
        elif(opc == 6):
            print("Salió")
            ciclo = False
        else:
            print("Ingrese un valor del 1-6")
if __name__ == "__main__":
    main()