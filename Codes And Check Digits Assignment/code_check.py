
def BasicCode(userinput):
  num = int(userinput)

  #Initialize boolean variable
  BasicCode.boolean = False
  
  #This is the number without the last digit
  numModded = num // 10
  
  #This is the last digit of the input number
  numLastDigit = num % 10

  #Initializing the variable for the sum of the input number
  bcSumNum = 0

  #Seperates 'numModded' into seperate entries in a list and assigns the list to a variable
  basicList = [int(x) for x in str(numModded)]

  #'For' loop that loops through the above list and adds each digit into the sum variable
  for digit in basicList:
    bcSumNum += digit

  #takes the last digit of the sum of the numbers
  bcSumLastDigit = bcSumNum % 10

  #If the last digit of the input number matches the last digit of the sum variable, state valid, and return boolean true, otherwise, end this function.
  if bcSumLastDigit == numLastDigit:
    BasicCode.boolean = True
    print("--code:", userinput, "valid Basic code.")
  return BasicCode.boolean

def PositionalCode(userinput):
  num = int(userinput)

  #Initialize boolean variable
  PositionalCode.boolean = False

  #Initializes a loop counter variable
  loop = 0

  #This is the number without the last digit
  numModded = num // 10
  
  #This is the last digit of the input number
  numLastDigit = num % 10

  #Initializing the variable for the sum of the input number
  pcSumNum = 0

  #Seperates 'numModded' into seperate entries in a list and assigns the list to a variable
  positionalList = [int(x) for x in str(numModded)]

  #'For' loop that loops through the above list and calculates the sum
  for digit in positionalList:
    #Adds 1 to the loop
    loop += 1

    #Multiplies the digit to the its respective position in the number, and adds that to the sum variable
    pcSumNum += (digit * loop)

  #takes the last digit of the sum of the numbers
  pcSumLastDigit = pcSumNum % 10
  
  #If the last digit of the input number matches the last digit of the sum variable, state valid, and return boolean true, otherwise, end this function.
  if pcSumLastDigit == numLastDigit:
    PositionalCode.boolean = True
    print("--code:", userinput, "valid Positional code.")
  return PositionalCode.boolean

def UPC(userinput):
  num = int(userinput)

  #Initialize boolean variable
  UPC.boolean = False

  #Initializes a loop counter variable
  loop = 0

  #This is the number without the last digit
  numModded = num // 10
  
  #This is the last digit of the input number
  numLastDigit = num % 10

  #Initializing the variable for the sum of the input number
  upcSumNum = 0

  #Seperates the input number into seperate entries in a list and assigns the list to a variable
  universalList = [int(x) for x in str(numModded)]

  #'For' loop that loops through the above list and calculates the sum
  for digit in universalList:
    #Adds 1 to the loop
    loop += 1

    #Multiplies the digit to the its respective position in the number, and adds that to the sum variable
    if loop % 2 == 1:
      upcSumNum += (digit * 3)
    else:
      upcSumNum += (digit * 1)
      

  #takes the last digit of the sum of thse numbers
  pcSumLastDigit = 10 - (upcSumNum % 10)
  
  #If the last digit of the input number matches the last digit of the sum variable, state valid, and return boolean true, otherwise, end this function.
  if pcSumLastDigit == numLastDigit:
    UPC.boolean = True
    print("--code:", userinput, "valid UPC Code.")
  return UPC.boolean
