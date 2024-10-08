# Import file from your system
from google.colab import files
file = files.upload()

# Connect with sqlite database
# Import necessary libraries
import sqlite3

database = 'database.sqlite'

conn = sqlite3.connect(database)
print('Opened data successfully')

# Read SQL query for getting all the tables of database into a dataframe
import pandas as pd
tables = pd.read_sql("""SELECT * 
                    FROM sqlite_master
                    WHERE type='table';""", conn)
tables


# Read Table from the database into dataframe
matches = pd.read_sql("""SELECT *
                        FROM Match;""", conn)

# Print Table info
matches.info()