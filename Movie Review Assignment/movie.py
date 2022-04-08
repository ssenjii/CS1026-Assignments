class Movie:
  
  def __init__(self, title = '<title>', year = 0000):
    self.title = title
    self.year = year
    self.reviews = []

  """
  Name: __calcAverage

  Description: calculates the average of the reviews in the list "self.reviews"

  Parameters: N/A

  Returns:
    avgRating: the calculated average
  """
  def __calcAverage(self):
    avgRating = round(sum(self.reviews) / len(self.reviews), 1)
    return avgRating

  """
  Name: addReview

  Description: adds a review to the specified movie

  Parameters:
    review: the review that is paired with the command, must be an integer

  Returns: N/A
  """
  def addReview(self, review):
    #if review is less than 1 or more than 5, do nothing
    if review < 1 or review > 5:
      pass
    #otherwise, add it to the list
    else:
      self.reviews.append(review)

  """
  Name: shortReview

  Description: prints a short review with the average review score, if no reviews, prints 0.0/5

  Parameters: N/A

  Returns: N/A
  """
  def shortReview(self):
    #if there are no reviews, print the following
    if len(self.reviews) == 0:
      print("{} ({}): {}/5".format(self.title, self.year, 0))
    #otherwise calculate the average and print the following
    else:
      avgRating = self.__calcAverage()
      print("{} ({}): {}/5".format(self.title, self.year, avgRating))

  """
  Name: longReview

  Description: prints a long review with the average review score, if no reviews, prints 0.0/5 with 0 on all the stars

  Parameters: N/A

  Returns: N/A
  """
  def longReview(self):
    #if there are no reviews, print the following
    if len(self.reviews) == 0:
      print("{} ({})\nAverage review: {}/5\n*****: {}\n**** : {}\n***  : {}\n**   : {}\n*    : {}"
      .format(self.title, self.year, 0.0, 0 ,0 ,0 ,0 ,0))
    else:
      #lists for each star rating
      starRating1 = []
      starRating2 = []
      starRating3 = []
      starRating4 = []
      starRating5 = []

      #calculates the avg
      avgRating = self.__calcAverage()

      #puts each star rating in its respective list
      for num in self.reviews:
        if num == 1:
          starRating1.append(num)
        elif num == 2:
          starRating2.append(num)
        elif num == 3:
          starRating3.append(num)
        elif num == 4:
          starRating4.append(num)
        elif num == 5:
          starRating5.append(num)
      
      print("{} ({})\nAverage review: {}/5\n*****: {}\n**** : {}\n***  : {}\n**   : {}\n*    : {}"
      .format(self.title, self.year, avgRating, len(starRating5) ,len(starRating4) ,len(starRating3) ,len(starRating2) ,len(starRating1)))

  """
  Name: getTitle

  Description: accessor function to get the title of a specified movie

  Parameters: N/A

  Returns:
    self.title: returns the title of the specified movie
  """
  def getTitle(self):
    return self.title

  """
  Name: getYear

  Description: accessor function to get the year of a specified movie

  Parameters: N/A

  Returns:
    self.year: returns the year of the specified movie
  """
  def getYear(self):
    return self.year

  """
  Name: __eq__

  Description: correctly compares objects

  Parameters:
    other: the other object you're comparing this object to

  Returns:
    NotImplemented = basically tries the comparison both ways. e.g. it tries a == b, then tries b == a
    self.title == other.title = returns boolean to see if titles match
    self.year == other.year = returns boolean to see if years match
  """
  def __eq__(self, other):
    if not isinstance(other, Movie):
      return NotImplemented
    return self.title == other.title and self.year == other.year