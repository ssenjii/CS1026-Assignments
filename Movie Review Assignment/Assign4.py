"""
Date: April 5, 2022
This file takes movie entries and reviews to create a database of movies and reviews.
This is done by taking commands by a text file and calling respective classes and functions
to do so. Upon command, it will print a long review or print all reviews in the form of short reviews
"""

from os.path import dirname, join #used to ensure the files input are correctly sourced from the correct directory
from movie import Movie #imports movie class from movie file
from moviedb import MovieDB #imports movie db class from movie db file

################### GLOBAL VARIABLES ###################
COMMAND=0
TITLE=1
YEAR=2
REVIEW=3

NEW_COMMAND = 'NEW'
REVIEW_COMMAND = 'REV'
SHOW_COMMAND = 'SHO'
PRINT_COMMAND = 'PRI'
################### GLOBAL VARIABLES ###################

"""
Name: readFile

Description: reads the file that the user inputs

Parameters:
  input: the name of the file, must be string

Returns: does not return anything
"""
def readFile(input):
  moviedbClass = MovieDB() #sets variable for moviedb class
  currentDir = dirname(__file__) #finds the directory of the current file
  fileName = join(currentDir, "./", input) #this makes it so that running the code in the client would run in the correct directory (this problem doesnt occur in cmd)

  #opens the file
  with open(fileName,'r') as fh:
    for line in fh:
      #strips each line of '-'
      data = line.strip().split('-')

      command = data[COMMAND]

      #If NEW_COMMAND, add it to the database
      if command == NEW_COMMAND:
        title = data[TITLE]
        year = int(data[YEAR])
        #If the entry is not already in the database, add it
        if not Movie(title, year) in moviedbClass.database:
          moviedbClass.addMovie(title, year)
        #Otherwise, pass
        else:
          pass
      
      #If REVIEW_COMMAND, enter a review for the respective movie
      elif command == REVIEW_COMMAND:
        title = data[TITLE]
        year = int(data[YEAR])
        review = int(data[REVIEW])

        #Determine the correct movie by looping through all the movies in the database
        #and matching a movie name and year, then adding that review to its list of reviews
        for entry in moviedbClass.database:
          if entry.title == title and entry.year == year:
            entry.addReview(review)
          #If no movie is found, pass
          else:
            pass

      #If SHOW_COMMAND, show all the reviews in the form of short reviews
      elif command == SHOW_COMMAND:
        moviedbClass.showAll()

      #If PRINT_COMMAND, print the current movie in long review form
      elif command == PRINT_COMMAND:
        title = data[TITLE]
        year = int(data[YEAR])

        #Determine the correct movie by looping through all the movies in the database
        #and matching a movie name and year, then printing its long review
        for entry in moviedbClass.database:
          if entry.title == title and entry.year == year:
            entry.longReview()
          #If no movie is found, pass
          else:
            pass

def main():
  fileInput = str(input('Enter the name of the file: ')) #getting input
  readFile(fileInput)

main()