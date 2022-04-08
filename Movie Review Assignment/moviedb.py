#imports the movie function from the movie file
from movie import *

class MovieDB:

  def __init__(self):
    self.database = []

  """
  Name: addMovie

  Description: adds movie to the database list

  Parameters:
    title: the title of the movie
    year: the year of the movie

  Returns: N/A
  """
  def addMovie(self, title, year):
    self.title = title
    self.year = year

    #tries adding entry to list
    try:

      #if the movie is not in the database, add it
      if not Movie(self.title, self.year) in self.database:
        self.database.append( Movie(self.title, self.year))

      #if it already exists, raises KeyError
      else:
        raise KeyError

    except KeyError:
      print('Entry already in list')

  """
  Name: findMovie

  Description: finds a movie in the database list

  Parameters:
    title: the title of the movie
    year: the year of the movie

  Returns:
    entry = returns the Movie object
    None = returns 'None'
  """
  def findMovie(self, title, year):
    #loops through movies in the database
    for entry in self.database:

      #if a match is found, return the entry
      if entry.title == title and entry.year == year:
        return entry

      #otherwise, return None
      else:
        return None

  """
  Name: showAll

  Description: shows all reviews in a long review format

  Parameters: N/A

  Returns: N/A
  """
  def showAll(self):
    movieList = []

    #appends every movie and year to a list
    for entry in self.database:
      movieList.append((entry.getTitle(), entry.getYear()))

    #sorts the list
    movieList.sort()

    #loops through every pair in the list
    for (t, y) in movieList:

      #loops through every movie in the database
      for entry in self.database:

        #if a match is found, carry on
        if entry.title == t and entry.year == y:

          #if the number of reviews is 0, print the following
          if len(entry.reviews) == 0:
            print("{} ({}): 0.0/5".format(t, y))

          #if more than 0 reviews, calculate the average and print the following
          else:
            avgRating = round(sum(entry.reviews) / len(entry.reviews), 1)
            print("{} ({}): {}/5".format(t, y, avgRating))

        #otherwise, pass
        else:
          pass