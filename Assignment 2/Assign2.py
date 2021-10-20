#Importing the functions from the other file
from code_check import BasicCode, PositionalCode, UPC

#Initializing lists for the codes
bcList = []
pcList = []
upcList = []
noneList = []

#Main Function
def main():
  #Gets input from user
  userinput = input("Please enter code (digits only) (enter 0 to quit) ")
  #Infinite loop until user enters 0
  while (userinput != "0"):
    #Calls each of the functions to determine whether or not it is that type of code.
    BasicCode(userinput)
    PositionalCode(userinput)
    UPC(userinput)

    #'If' loop to put the input into its respective list
    if BasicCode.boolean == True and userinput != "0":
      bcList.append(userinput)
    if PositionalCode.boolean == True and userinput != "0":
      pcList.append(userinput)
    if UPC.boolean == True and userinput != "0":
      upcList.append(userinput)
    
    #If the code returns False in all cases (meaning its none of the 3 types of code), and if the input isn't 0, add it to the 'none' list
    if BasicCode.boolean == False and PositionalCode.boolean == False and UPC.boolean == False and userinput != "0":
      print("--code:", userinput, "not Basic, Position, or UPC Code.")
      noneList.append(userinput)
    #calls the main function again to loop
    main()

  #If a list is empty, append the string "None" to it.
  if not bcList:
    bcList.append("None")
  if not pcList:
    pcList.append("None")
  if not upcList:
    upcList.append("None")
  if not noneList:
    noneList.append("None")

  #The next 4 lines makes it so that when the lists are printed, it's not printed with the brackets
  bc = ', '.join(bcList)
  pc = ', '.join(pcList)
  upc = ', '.join(upcList)
  none = ', '.join(noneList)

  #The print statement
  print("Summary\nBasic : {}\nPosition : {}\nUPC : {}\nNone : {}".format(bc, pc, upc, none))
  
  #Exits the program
  quit()

#Calls the main function
main()
