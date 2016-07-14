"""@package docstring
Documentation for this module

More details.
"""
# !/usr/bin/env python
import Database
# import Statistics
# import Initializer
# import test_dakota
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

# Statistics.anova()

# x = test_dakota.TestDriver()
# x.run()

# dakota_driver.driver.run_dakota(infile="test.in")

disp_graph = raw_input("Display graphs? (Y/n)  ")

if disp_graph == "Y":
    print "Liver_UF_Control_rep2"
    dataset = dataB.get_set("GSM576077")
    Graphics.display_graphics(dataset)

    print "Liver_A_Exposed_rep2"
    dataset = dataB.get_set("GSM576083")
    Graphics.display_graphics(dataset)

    print "Liver_B_Exposed_rep2"
    dataset = dataB.get_set("GSM576086")
    Graphics.display_graphics(dataset)

    print "Liver_D_Ref_rep2"
    dataset = dataB.get_set("GSM576084")
    Graphics.display_graphics(dataset)

    print "Liver_E_Exposed_rep2"
    dataset = dataB.get_set("GSM576081")
    Graphics.display_graphics(dataset)

    print "Testis_UF_Control_rep2"
    dataset = dataB.get_set("GSM576102")
    Graphics.display_graphics(dataset)

    print "Testis_A_Exposed_rep2"
    dataset = dataB.get_set("GSM576103")
    Graphics.display_graphics(dataset)

    print "Testis_B_Exposed_rep2"
    dataset = dataB.get_set("GSM576106")
    Graphics.display_graphics(dataset)

    print "Testis_D_Ref_rep3"
    dataset = dataB.get_set("GSM576100")
    Graphics.display_graphics(dataset)

    print "Testis_E_Exposed_rep2"
    dataset = dataB.get_set("GSM576105")
    Graphics.display_graphics(dataset)

# Commit changes to database
dataB.comm_exit()
