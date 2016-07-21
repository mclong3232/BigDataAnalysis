"""@package docstring
Documentation for this module

More details.
"""
# !/usr/bin/env python
import Database
# import Statistics
# import Initializer
import dakota
import Graphics


# Initializes connection to MySQL database and application window.
username = raw_input("Username:  ")
password = raw_input("Password:  ")
dataB = Database.MyDatabase("localhost", username, password, "signal_intensity")


# Clear out a database.
# dataB.mysql.execute("DROP DATABASE `signal_intensity`;")
# dataB.mysql.execute("CREATE SCHEMA `signal_intensity` DEFAULT CHARACTER SET utf8 ;")
# dataB = Database.MyDatabase("localhost", username, password, "signal_intensity")


# Get a list of all files that could be added to database
files = dataB.get_files()

targetfile = raw_input("Which dataset to add:  ")

if targetfile in files:
    dataB.add_data(dataB, targetfile)
else:
    print "Dataset not found!"


# Run statistical process on data sets
# Statistics.anova()


# Run DAKOTA
dakota.run_dakota(infile="dakota.in", stdout="dakota_results.out", stderr="dakota_results.err")


# Graph the data sets
disp_graph = raw_input("Display graphs? (Y/n)  ")

if disp_graph == "Y":
    Graphics.graph_sets(dataB)


# Commit changes to database
dataB.comm_exit()
