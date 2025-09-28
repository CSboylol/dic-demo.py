#This print is the golbal scope of the file
print("Hello World")
print(3+4*5)
print("Here I am before my function")

def printMe(myName):
    #Scope of execution of the print fuction is under the printMe fuction
    myName = myName + " King"
    return myName


print("Here I am after my function")
printMe("David")
print("End of the file ")