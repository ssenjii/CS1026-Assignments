"""
This script computes the cost of electricity for individual residences.
It will account for several discounts based on usage and whether the
residence belongs to a senior or not. An electricity cost will be output
after the respectful discounts have been applied.
"""

#Peak Hour Prices
OFFPEAK = 0.085
ONPEAK = 0.176
MIDPEAK = 0.119

#Discounts (100 - <discount>)
TotalUsageDiscount = 0.96
OnPeakDiscount = 0.95
SeniorDiscount = 0.89

#TAX
TAX = 1.13

#This function is a separate block of code specifically asking for senior status
#It also limits your input to "y" and "n", regardless of the capitalization.

def seniorCheck():
  r = input("Is owner senior? (Y,y,N,n): ")
  #.lower() turns all input lower case.
  if r == "y" or r == "Y":
    seniorCheck.areYouSenior = r.lower()

  elif r == "n" or r == "N":
    seniorCheck.areYouSenior = r.lower()

  else:
    print("Please try again.")
    seniorCheck()

#Main function
def main():
  #Initializing variables
  offPeakInput = -1
  onPeakInput = -1
  midPeakInput = -1

  #Setting condition to end script if user enters "0" for the kwh during off peak.
  #Also asks for inputs for kwh during different periods.
  while (offPeakInput != 0):
    offPeakInput = float(input("Enter kwh during Off Peak period: "))
    if (offPeakInput == 0):
      quit()

    onPeakInput = float(input("Enter kwh during On Peak period: "))

    midPeakInput = float(input("Enter kwh during Mid Peak period: "))

    seniorCheck()
    break

  #Applying the peak hour prices to the inputs
  onPeakPrice = onPeakInput * ONPEAK
  offPeakPrice = offPeakInput * OFFPEAK
  midPeakPrice = midPeakInput * MIDPEAK

  #Creating variable of all the prices added together
  preFinalPrice = onPeakPrice + offPeakPrice + midPeakPrice

  #Creating variable of all the kwh inputs added together
  totalUsage = offPeakInput + onPeakInput + midPeakInput

  #Sets conditions for each discount
  #If the total kwh usage is less than 400 but the on peak kwh is not less than 150,
  #it'll apply only the Total Usage Discount
  if (totalUsage < 400) and (onPeakInput > 150):
    preFinalPrice *= TotalUsageDiscount
    
  #We use an "else if" condition here instead of a regular "if" since it's a "one or the other"
  #type deal, where if the discount above is applied, this one cannot be applied. Likewise, 
  #if the discount above was not applied, it'll come to this one, and granted the conditions are
  #met, the discount will be applied to the On Peak price, and then added to the total price.
  elif (onPeakInput < 150):
    onPeakPrice *= OnPeakDiscount
    preFinalPrice = onPeakPrice + offPeakPrice + midPeakPrice

  #This one is just a simple "if condition is met, apply discount"
  if (seniorCheck.areYouSenior == "y"):
    preFinalPrice *= SeniorDiscount

  #Applying tax
  finalPrice = round(preFinalPrice * TAX, 2)

  #Prints output statement.
  print("Electricity cost: ${}\n".format(finalPrice))

  #Runs the function again, creating an endless loop until 0 is entered as off peak input.
  main()

#This just runs the function the first time.
main()
