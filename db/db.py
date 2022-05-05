from json import load
from psycopg2 import connect

class Database:
  # db/login.json instead of login.json, because it is imported by app.py
  jsonfile = open('db/login.json', 'r')
  login = load(jsonfile)

  user = login['user']
  password = login['password']
  dbname = login['database']
  port = login['port']

  def __init__(self):
    try:
      self.db = connect(f"user={self.user} password={self.password} dbname={self.dbname} port={self.port}")
      self.cursor = self.db.cursor()
    except:
      raise Exception("An error occurred.")
    