from core.constants import *

class ctx:
  def __init__(self):
    self.date = DATE
    self.title = "FlaskPostgreSQL Blog"
    # self.login = True
    self.user = 'Clark'

class postdata:
  def __init__(self):
    self.id = 0
    self.title = 1
    self.content = 2
    self.createdAt = 3