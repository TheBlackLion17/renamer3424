import os, time

class Config(object):
  # database config
    DB_NAME = os.environ.get("DB_NAME","Agsmod")     
    DB_URL  = os.environ.get("DB_URL","")
