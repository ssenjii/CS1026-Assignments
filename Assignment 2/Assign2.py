def BasicCode(r):
  #This is the number without the last digit
  numModded = r // 10
  
  #This is the last digit of the input number
  numLastDigit = r % 10

  #Initializing the variable for the sum of the input number
  bcSumNum = 0

  #Seperates 'numModded' into seperate entries in a list and assigns the list to a variable
  res = [int(x) for x in str(numModded)]

  #'For' loop that loops through the above list and adds each digit into the sum variable
  for digit in res:
    bcSumNum += digit

  #takes the last digit of the sum of the numbers
  bcSumLastDigit = bcSumNum % 10

  #If the last digit of the input number matches the last digit of the sum variable, print out that it is valid, otherwise, end this function.
  if bcSumLastDigit == numLastDigit:
    print(r, "valid Basic Code.")

def PositionalCode(r):
  #Initializes a loop counter variable
  loop = 0

  #This is the number without the last digit
  numModded = r // 10
  
  #This is the last digit of the input number
  numLastDigit = r % 10

  #Initializing the variable for the sum of the input number
  pcSumNum = 0

  #Seperates 'numModded' into seperate entries in a list and assigns the list to a variable
  res = [int(x) for x in str(numModded)]

  #'For' loop that loops through the above list and calculates the sum
  for digit in res:
    #Adds 1 to the loop
    loop += 1

    #Multiplies the digit to the its respective position in the number, and adds that to the sum variable
    pcSumNum += (digit * loop)

  #takes the last digit of the sum of the numbers
  pcSumLastDigit = pcSumNum % 10
  
  #If the last digit of the input number matches the last digit of the sum variable, print out that it is valid, otherwise, end this function.
  if pcSumLastDigit == numLastDigit:
    print(r, "valid Positional Code.")


def main():
  #Gets input from user
  r = int(input("Please enter code (digits only) (enter 0 to quit) "))
  #If the input is 0, the program quits immediately
  if (r == 0):
    quit()
  
  #Calls each of the functions to determine whether or not it is that type of code.
  BasicCode(r)
  PositionalCode(r)

#Calls the main function
main()
