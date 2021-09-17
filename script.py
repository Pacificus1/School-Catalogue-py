class School:
  def __init__(self, name, level, numberOfStudents):
    self._name = name
    self._level = level
    self._numberOfStudents = numberOfStudents
    
  @property
  def name(self):
    return self._name
  @property
  def level(self):
    return self._level
  @property
  def numberOfStudents(self):
    return self._numberOfStudents
  @numberOfStudents.setter
  def numberOfStudents(self, num):
    self._numberOfStudents = num

  def __repr__(self):
    return(f"A {self.level} school name {self.name} with {self.numberOfStudents} students")

class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, "primary", numberOfStudents)
    self._pickupPolicy = pickupPolicy

  @property
  def pickupPolicy(self):
    return self._pickupPolicy
  @pickupPolicy.setter
  def pickupPolicy(self, pickup):
    self._pickupPolicy = pickup

  def __repr__(self):
    return(f"A {self.level} school name {self.name} Pickup is {self.pickupPolicy} for students.")

class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, 'high', numberOfStudents)
    self._sportsTeams = sportsTeams

  @property
  def sportsTeams(self):
    return self._sportsTeams
  @sportsTeams.setter
  def sportsTeams(self, teams):
    self._sportsTeams = teams

  def __repr__(self):
    return(f"A {self.level} school named {self.name} number one sports are {self.sportsTeams} and also has {self.numberOfStudents} students.")

e1 = School("TVHS", "high school", 50)
print(e1)

e2 = PrimarySchool("codecademy", 60, "Not Allowed")
print(e2)

e3 = HighSchool("Golden Bears", 1200, ["Wrestling, Football"])
print(e3)








