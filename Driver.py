"""
@package Driver.py
The driver module for the entire program.
"""

# !/usr/bin/env python
import Database
# import Graphics
# import Analysis
# import Initializer


# Initializes connection to MySQL database
print "Logging into database..."
username = raw_input("Username:  ")
password = raw_input("Password:  ")
dataB = Database.MyDatabase("localhost", username, password, "signal_intensity")


# Clear out a database.
# dataB.mysql.execute("DROP DATABASE `signal_intensity`;")
# dataB.mysql.execute("CREATE SCHEMA `signal_intensity` DEFAULT CHARACTER SET utf8 ;")
# dataB = Database.MyDatabase("localhost", username, password, "signal_intensity")


# Get a list of all files that could be added to database
# Searches within the current working directory
files = dataB.get_files()

targetfile = raw_input("Which dataset to add:  ")

if targetfile in files:
    dataB.add_data(dataB, targetfile)
else:
    print "Dataset not found!"


# Run statistical process on data sets
# Statistics.anova()


# Run DAKOTA
# Analysis.uq()


# Commit changes to database
dataB.comm_exit()
