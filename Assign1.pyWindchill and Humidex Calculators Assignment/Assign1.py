"""
Date: Feb 15, 2022
Function prompts user for airtemperature in the form of a float. Then proceeds to calculate
humidex or windchill accordingly, and returns a comfort rating/exposure risk rating respectively,
prompting for additional inputs as needed.
"""

#importing math library to use the formulas
from math import *

#function that prompts the user to restart the program
def retryPrompt():
  reply = input("Check another weather condition (Y/N)? ").lower()

  if reply == 'y':
    main()

  elif reply == 'n':
    exit()
  
  else:
    print('That input is invalid.')
    retryPrompt()

#function to calculate humidex
def humidex(airTemp):
  print('Calculating humidex.')
  #global makes it so that i can use this variable elsewhere
  global crOutput

  #humidex comfort ratings to print out
  hdRange1 = 'Little or no discomfort.'
  hdRange2 = 'Some discomfort.'
  hdRange3 = 'Great discomfort. Avoid exertion.'
  hdRange4 = 'Dangerous. Heat stroke possible.'

  #calculations
  dewpointInput = float(input('Enter the dewpoint between -50 and 50: '))
  while not (1 <= dewpointInput <= 99):
    print('That dew point is invalid.')
    dewpointInput = float(input('Enter the dewpoint between -50 and 50: '))
  varF = 6.11 * exp(5417.7530 * ( 1/273.16 - (1/(273.16 + dewpointInput))))
  varG = 5/9 * (varF - 10)
  varH = airTemp + varG

  #rounded humidex result
  hdResult = round(varH)

  #humidex comfort ratings if statements
  if (20 <= hdResult <= 29):
    crOutput = hdRange1
  elif (30 <= hdResult <= 39):
    crOutput = hdRange2
  elif (40 <= hdResult <= 44):
    crOutput = hdRange3
  elif (45 <= hdResult):
    crOutput = hdRange4

  #return result
  return hdResult

#function to calculate windchill
def windchill(airTemp):
  print('Calculating windchill.')
  #global makes it so that i can use this variable elsewhere
  global erOutput

  #windchill exposure ratings to print out
  wcRange1 = 'Low risk.'
  wcRange2 = 'Moderate risk.'
  wcRange3 = 'High Risk. Skin can freeze in 10-30 minutes.'
  wcRange4 = 'Very High Risk. Skin can freeze in under 10 minutes.'
  #get velocity input from user
  velocityInput = float(input('Enter a wind speed between 1 and 99 km/h: '))
  while not (1 <= velocityInput <= 99):
    print('That wind speed is invalid.')
    velocityInput = float(input('Enter a wind speed between 1 and 99 km/h: '))

  #calculations
  varV = velocityInput ** 0.16
  varW = 13.12 + 0.6125 * airTemp - 11.37 * varV + 0.3965 * airTemp * varV

  #rounded windchill result
  wcResult = round(varW)

  #windchill exposure ratings if statements
  if (-9 <= wcResult <= 0):
    erOutput = wcRange1
  elif (-27 <= wcResult <= -10):
    erOutput = wcRange2
  elif (-39 <= wcResult <= -28):
    erOutput = wcRange3
  elif (wcResult <= -40):
    erOutput = wcRange4

  #return result
  return wcResult

def main():
  #gets air temperature from user
  airTemp = float(input('Enter a temperature between -50 and 50: '))
  while not (-50 <= airTemp <= 50):
    print('That temperature is invalid.')
    airTemp = float(input('Enter a temperature between -50 and 50: '))

  #if airtemp is 0 or below, runs the windchill function
  if airTemp <= 0:
    print('The windchill is {}. {}'.format(windchill(airTemp), erOutput))

  #if airtemp is 20 or higher, runs the humidex function
  elif airTemp >= 20:
    print('The humidex is {}. {}'.format(humidex(airTemp),crOutput))

  #if neither are true, prints the text below and continues
  else:
    print("Windchill and humidex are not a factor at this temperature.")

  #prompts the user to retry program
  retryPrompt()  

#calls main function
main()
