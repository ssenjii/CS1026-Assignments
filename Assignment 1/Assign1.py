import sys, time, os
from typing import final

#Clears the previous code output if any.
os.system('cls' if os.name == 'nt' else 'clear')

#Peak Hour Prices
OFFPEAK = 0.085
ONPEAK = 0.176
MIDPEAK = 0.119

#Discounts
TotalUsageDiscount = 0.96
OnPeakDiscount = 0.95
SeniorDiscount = 0.89

TAX = 1.13

def inputRestriction():
  while True:
    try:
      a = int(input())
    except ValueError:
      print("Sorry, I didn't understand that. ")
      time.sleep(0.1)
      print("Please enter a number.\n")
      continue

    if a < 0:
      print("Please enter a positive number\n")
    else:
      break
  return a

def seniorCheck():
  print("Is owner senior? (Y,y,N,n): ")
  r = input()
  if r == "y" or r == "Y":
    y = r.lower()
    seniorCheck.areYouSenior = y

  elif r == "n" or r == "N":
    z = r.lower()
    seniorCheck.areYouSenior = z

  else:
    print("Please try again.")
    seniorCheck()
  
def main():
  offPeakInput = -1
  onPeakInput = -1
  midPeakInput = -1
  while (offPeakInput != 0):
    #print("Enter kwh during Off Peak period: ")
    offPeakInput = float(input("Enter kwh during Off Peak period: "))
    if (offPeakInput == 0):
      print("Process finished with exit code 0")
      break

    #print("Enter kwh during On Peak period: ")
    onPeakInput = float(input("Enter kwh during On Peak period: "))

    #print("Enter kwh during Mid Peak period: ")
    midPeakInput = float(input("Enter kwh during Mid Peak period: "))

    seniorCheck()
    break
  
  onPeakPrice = onPeakInput * ONPEAK
  offPeakPrice = offPeakInput * OFFPEAK
  midPeakPrice = midPeakInput * MIDPEAK
  preFinalPrice = onPeakPrice + offPeakPrice + midPeakPrice

  totalUsage = offPeakInput + onPeakInput + midPeakInput
  if (totalUsage < 400) and (onPeakInput > 150):
    preFinalPrice = preFinalPrice * TotalUsageDiscount
    
  elif (onPeakInput < 150):
    onPeakPrice *= OnPeakDiscount

  if (seniorCheck.areYouSenior == "y"):
    preFinalPrice *= SeniorDiscount

  print("Electricity cost: ${}".format(finalPrice))

  #print(offPeakInput,  onPeakInput, midPeakInput)#, seniorCheck.areYouSenior)


main()
