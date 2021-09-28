import sys, time, os

#Clears the previous code output if any.
os.system('cls' if os.name == 'nt' else 'clear')

#Peak Hour Prices
OFFPEAK = 0.085
PEAK = 0.176
MIDPEAK = 0.119

#Discounts
TotalUsageDiscount = 0.04
OnPeakDiscount = 0.05
SeniorDiscount = 0.11

TAX = 0.13

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
      print(f"Please enter a positive number\n")
    else:
      break
  return a

def seniorCheck():
  print("Is owner senior? (Y,y,N,n): ")
  r = input()
  if r == "y":
    seniorCheck.areYouSenior = 1

  elif r == "n":
    seniorCheck.areYouSenior = 0

  else:
    print("Please try again.")
    seniorCheck()

  

def main():
  offPeakInput = -1
  onPeakInput = -1
  midPeakInput = -1
  while (offPeakInput != 0):
    print("Enter kwh during Off Peak period: ")
    offPeakInput = inputRestriction()
    if (offPeakInput == 0):
      print("Process finished with exit code 0")
      break

    print("Enter kwh during On Peak period: ")
    onPeakInput = inputRestriction()

    print("Enter kwh during Mid Peak period: ")
    midPeakInput = inputRestriction()

    seniorCheck()
    break

  print(offPeakInput,  onPeakInput, midPeakInput, seniorCheck.areYouSenior)

main()
