"""
This program is supposed to take a .csv file of poll votes and decide who gets eliminated in each round.
It works by taking in the csv file, reading each row and column, calculating how many votes in each round,
and thus determining who gets eliminated and who wins the vote. It outputs the order of which the candidates
are eliminated.

(DOESNT WORK)
"""
import csv #used to read csv files
from os.path import dirname, join #used to ensure the files input are correctly sourced from the correct directory
import random #used to assign random IDs to candidates
from collections import Counter, OrderedDict #used to count each occurrence of each number

#this function opens the directory of which the currrent file is in, so that if it is run using something like cmd, it works in that console
def openDir():
  currentDir = dirname(__file__) #finds the directory of the current file
  fileInput = input('Enter the name of the file: ') #getting input
  fileName = join(currentDir, "./", fileInput) #this makes it so that running the code in the client would run in the correct directory (this problem doesnt occur in cmd)
  file = open(fileName, encoding='utf-8-sig') #without the encoding part of this line, it would print 'ï»¿' before the first entry
  return file

#this function reads the csv file input into the program
def readInput():
  fileName = openDir() #calls the openDir function so that it works in other consoles
  csvreader = csv.reader(fileName) #reads the file using the csv library
  rowList = [] #creates empty list for each row in the csv file
  for row in csvreader:
    rowList.append(row) #appends each row as lists into rowList
  return rowList

#assigns ids to every candidate
def assignID(readInputReturn):
  candidateIDList = [] #creates empty list for each candidate's ID
  for row in readInputReturn: #initiates the variable row
    pass

  #assigns random ID's ranging from 1-200, and makes sure if a number is already assigned, it is not assigned again
  for candidateID in range(0, len(row)): 
    candidateID = random.randint(1,200)
    if candidateID in candidateIDList:
      candidateID = random.randint(1,200)
    candidateIDList.append(candidateID)
  return candidateIDList

#determines which candidate to eliminate for each round
def determineElim(readInputReturn,voteStarter):
  for row in readInputReturn: #initiates the variable row
    pass

  candidateIDList = assignID(readInputReturn) #calls the ID list into this function
  voteCountDict = Counter() #creates a dictionary with the counts of each candidate
  placeList = []
  #makes it so that this loops through every column
  for occur in range(voteStarter, len(row)):
    loopCounter = -1

    #removes empty spaces in the list of entries
    for row in readInputReturn:
      if row[occur].isdigit():
        placeList.append(row[occur])
    
    voteCount = OrderedDict(sorted(voteCountDict.items())) #turn the dict into a list
    lowestID = -1
    lowestVar = 99999

    #for every entry in the voteCount list
    for key in voteCount:
      voteCountDict.clear() #clears the list for each use
      loopCounter += 1
      currentVar = (voteCount[key] / len(placeList)) * 100 #find the percentage for the current row
      print(f"candidate {loopCounter+1} = {currentVar}%") #for debugging purposes, this was used to what percentage of votes each candidate has
      #if the current percentage is above 50, the candidate wins
      if currentVar >= 50:
        print("candidate number", loopCounter+1, "is the winner")

      #elif, if the current variable is lower than the lowest, make the current into lowest, and assign the current candidate into the lowest candidate
      elif currentVar < lowestVar:
        lowestVar = currentVar
        lowestID = key

      #if the current variable is already the lowest variable, return it
      elif currentVar == lowestVar:
        if candidateIDList[(int(key)-1)] < candidateIDList[(int(lowestID)-1)]:
          return lowestID
        elif candidateIDList[(int(key)-1)] > candidateIDList[(int(lowestID)-1)]:
          lowestID = key
          return lowestID

# update the votes
def updateVotes(readInputReturn, lowestID):
  #this function was going to go through the entire list, or csv file and remove the votes of the candidate that lost
  for row in readInputReturn:
    for entry in range(len(row)):
      #this was going to see if the current row entry was equal to the candidate, and delete it
      if row[entry] == lowestID:
        row[entry] = ''

#this function was going to print out the elimination order
def elimOrder():
  pass

#main function
def main():
  readInputReturn = readInput()
  assignID(readInputReturn)
  lowestID = determineElim(readInputReturn,0)
  updateVotes(readInputReturn, lowestID)


main()
