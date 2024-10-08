# Import Dataset
from google.colab import files
uplaoded = files.upload()

# Import necessary libraries
import pandas as pd
import numpy as np
from datetime import datetime

# Setup a connection with database
# and print all the tables inside it
import sqlite3

database = 'database.sqlite'

conn = sqlite3.connect(database)

tables = pd.read_sql("""SELECT * 
                    FROM sqlite_master
                    WHERE type='table';""", conn)
tables

# Aliasing 
match_details = pd.read_sql('''SELECT Season_Id, Match_Id,  
                              v.Venue_Name, c.City_Name, t.Team_Name AS Winner 
                              FROM Match
                              INNER JOIN Venue AS v ON match.Venue_Id == v.Venue_Id
                              INNER JOIN City AS c ON v.City_Id == c.City_Id
                              INNER JOIN Team AS t ON match.Match_Winner == t.Team_Id;''', conn)

match_details