"""
This program takes name inputs and uses the Soundex algorithm to compare how the names sound.
It will compute through all the different names given, and output the names that have the same
Soundex value.
"""

#This function gets the inputs from the user.
def getInput():
  global wordList
  wordList = [] #create empty list for names
  wordNum = 1
  word = str(input("Enter names, one on each line. Type DONE to quit entering names. \n"))
  wordList.append(word) #adds names to list
  while word != "DONE": #While input is not 'DONE', keep asking for input 
    wordNum += 1
    word = str(input("Enter names, one on each line. Type DONE to quit entering names. \n"))
    if word != "DONE": #While input is not 'DONE', keep asking for input 
      wordList.append(word) #adds names to list
  return wordList


#This function is the third step of the soundex algorithm, which replaces letters with digits,
#as seen in the 'replacement_' variables below
def soundexStep3(word):
  posn = -1
  global newWords3
  #the Replacement Digit for each case
  replacement1 = "aeiouyhw"
  replacement2 = "bfpv"
  replacement3 = "cgjkqsxz"
  replacement4 = "dt"
  replacement5 = "l"
  replacement6 = "mn"
  replacement7 = "r"

  #makes the word into a list so it can iterate through each letter one by one
  wordListedForm = list(word)
  for char in wordListedForm:
    posn += 1
    if char in replacement1:
      wordListedForm[posn] = "0"
    elif char in replacement2:
      wordListedForm[posn] = "1"
    elif char in replacement3:
      wordListedForm[posn] = "2"
    elif char in replacement4:
      wordListedForm[posn] = "3"
    elif char in replacement5:
      wordListedForm[posn] = "4"
    elif char in replacement6:
      wordListedForm[posn] = "5"
    elif char in replacement7:
      wordListedForm[posn] = "6"
  newWords3 = "".join(wordListedForm) #joins the list back into a string
  return newWords3

#This function is step 4 of the soundex algorithm,
#this gets rid of consecutive repeating digits
def soundexStep4(newWords3):
  global se4res
  if len(newWords3)<2:
    return newWords3
  if newWords3[0]!=newWords3[1]:
    return newWords3[0]+soundexStep4(newWords3[1:])
  se4res = soundexStep4(newWords3[1:])
  return se4res

#This function removes 0 from the number
def soundexStep5(se4res): 
  global step5return
  wordRepList = list(str(se4res)) #turns the number from the prev step into a list
  tempList = []
  for num in wordRepList: #iterate through list
    if num != "0": #if the current num is not zero, add it to a list
      tempList.append(num)
  step5return = "".join(tempList) #join list into string
  return step5return


def soundexStep6(word): #This function converts F to a digit
  global se6return

  #the Replacement Digit for each case
  replacement1 = "aeiouyhw"
  replacement2 = "bfpv"
  replacement3 = "cgjkqsxz"
  replacement4 = "dt"
  replacement5 = "l"
  replacement6 = "mn"
  replacement7 = "r"

  firstLetter = word[0] #assigns the 0th index of the word into firstLetter

  #each case for which number it'll be
  if firstLetter in replacement1:
    firstLetterNum = "0"
  elif firstLetter in replacement2:
    firstLetterNum = "1"
  elif firstLetter in replacement3:
    firstLetterNum = "2"
  elif firstLetter in replacement4:
    firstLetterNum = "3"
  elif firstLetter in replacement5:
    firstLetterNum = "4"
  elif firstLetter in replacement6:
    firstLetterNum = "5"
  elif firstLetter in replacement7:
    firstLetterNum = "6"

  #if firstLetter is equal to the first digit of the soundex number, replace it
  if firstLetterNum == step5return[0]:
    se6return = (firstLetter + step5return[1:])
  
  #else, add it to the front
  else:
    se6return = (firstLetter + step5return)
  return se6return


def soundexStep7(): #This function makes the length of the soundex output into 4 digits  
  global se7return
  #if length is less than 4, add 0's then cut it to 4 digits.
  if len(se6return) < 4:
    se7return = ((se6return + "0000")[:4])
    return se7return
  #if length is more than 4, cut it to 4 digits
  elif len(se6return) > 4:
    se7return = se6return[:4]
    return se7return
  #if length is 4 digits, do nothing
  elif len(se6return) == 4:
    se7return = se6return
    return se7return

#This function is the main soundex function
def soundexMain():
  global listOfTuples
  listOfTuples = []
  #goes through each of the words in wordlist
  for word in newWordList:
    #goes through each of the steps that require functions
    soundexStep3(word)
    soundexStep4(newWords3)
    soundexStep5(soundexStep4(newWords3))
    soundexStep6(word)
    soundexStep7()
    #makes each case into a tuple
    tempTuple = tuple((se7return, word))
    #puts each tuple into a list
    listOfTuples.append(tempTuple)


def main():

  getInput() #gets input from user

  #makes another list and then appends lower case versions of the words into it
  global newWordList
  newWordList = []
  for word in wordList:
    word = word.lower()
    newWordList.append(word)

  soundexMain() #runs soundexMain func

  #goes through each tuple and find matching soundex cases, if one is found, take both names,
  #put it in a tuple, and then put that in a list of tuples for later use
  listOfResults = []
  for i in range(0, len(listOfTuples)):
    for j in range(i+1, len(listOfTuples)):
      if listOfTuples[i][0] == listOfTuples[j][0]:
        tempList = []
        tempList.append(wordList[i])
        tempList.append(wordList[j])
        tempList.sort() #make names alphabetical
        listOfResults.append(tempList)
  #make tuples alphabetical
  listOfResults.sort()
  #for each matching case, print names
  for i in range(0, len(listOfResults)):
    print(listOfResults[i][0], "and", listOfResults[i][1], "have the same Soundex encoding.")

#call main func
main()
