class Country:
  def __init__(self, name, pop, area, continent):
    self._name = name
    self._pop = pop
    self._area = area
    self._continent = continent

  #getName getter method
  def getName(self):
    return self._name

  #getPopulation getter method
  def getPopulation(self):
    return self._pop

  #setPopulation setter method
  def setPopulation(self, sPop):
    self._pop = sPop

  #getArea getter method
  def getArea(self):
    return self._area

  #setArea setter method
  def setArea(self, sArea):
    self._area = sArea

  #getContinent getter method
  def getContinent(self):
    return self._continent

  #setContinent setter method
  def setContinent(self, sContinent):
    self._continent = sContinent

