"""
@package Database.py
Handles all database functionality of the program.
"""

import Node
import MySQLdb
import os
import glob
import csv
import pandas as pd


class MyDatabase:
    """
    Definitions and methods for a database connection
    """

    def __init__(self, host, user, password, db):
        """
            Initialize a MySQL database connection.

            Args:
                host        :string:  hostname to login to MySQL database
                user        :string:  username to login to MySQL database
                password    :string:  password to login to MySQL database
                db          :string:  schema to connect to in MySQL database

            Returns:
                N/A
        """

        self.dtb = MySQLdb
        self.dtb_obj = self.dtb.connect(host=host,  # your host, usually localhost
                                        user=user,  # your username
                                        passwd=password,  # your password
                                        db=db)  # name of the data base
        self.mysql = self.dtb_obj.cursor(MySQLdb.cursors.DictCursor)

    @staticmethod
    def get_files():
        """
            Collects all of the file names that end in .csv into a list
            that are in the current working directory

            Args:
                N/A

            Returns:
                name_list   :List:  list of .csv file names
        """

        name_list = []

        # Choose the path to pull files from
        path = os.getcwd()

        files = glob.glob(path + "/*.csv")

        for f in files:
            # Extract the base name of the dataset
            csvname = os.path.basename(f)
            name = os.path.splitext(os.path.split(csvname)[1])[0]
            name_list.append(name)

        return name_list

    def add_table(self, db, table):
        """
            Adds a table into the specified schema of a MySQL database.

            Args:
                db      :string:    schema to be accessed
                table   :string:    name of the new table

            Returns:
                N/A
        """

        comm = """CREATE TABLE `{db}`.`{table}` (
               `id` INT NOT NULL,
               `value` FLOAT NOT NULL,
               PRIMARY KEY (`id`, `value`));"""

        comm = comm.format(db=db, table=table)
        self.mysql.execute(comm)

    def add_data(self, db, name):
        """
            Adds a .csv dataset into specified schema

            Accepts the name of the dataset and searches for it in
            a list of .csv datasets

            Args:
                db      :string:    name of schema to be accessed
                name    :string:    name of dataset to be added

            Returns:
                N/A
        """

        idlist = []
        vallist = []

        with open(name + '.csv', 'rb') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                idlist.append(float(row[0]))
                vallist.append(float(row[1]))

        dataset = Node.Node(name=name, id_=idlist, val=vallist)

        self.add_table(db, dataset.name)

        i = 0
        while i < len(dataset.idList):
            self.add_row(dataset.name, dataset.idList[i], dataset.valList[i])
            i += 1

    def add_row(self, table, id_, value):
        """
            Adds a row into the specified table.

            Args:
                table   :string:    name of the table to be accessed
                id_     :int:       value of the id_ to be added
                value   :int:       value of the value to be added

            Returns:
                N/A
        """

        comm = "INSERT INTO `{table}` () " \
               "VALUES ({id}, {value});"
        comm = comm.format(table=table, id=id_, value=value)
        self.mysql.execute(comm)

    def del_row(self, table, name, limit):
        """
            Deletes a row from the specified table.

            Args:
                table   :string:    identifies which table will be accessed
                name    :string:    identifies which row to be deleted
                limit   :string:    limit the amount of deletions

            Returns:
                N/A
        """

        comm = "DELETE FROM {table} WHERE name = '{name}' LIMIT {limit}"
        comm = comm.format(table=table, name=name, limit=limit)

        self.mysql.execute(comm)

    def get_row(self, table, name):
        """
            Gets the values of a row from the specified table and name.

            Args:
                table   :string:    identifies which table will be accessed
                name    :string:    identifies which row will be accessed

            Returns:
                row     :string:    value of the row requested by function
        """

        comm = "SELECT id FROM {table} WHERE name = {name}"
        comm = comm.format(table=table, name=name)

        self.mysql.execute(comm)
        row = self.mysql.fetchone()

        return row

    def get_set(self, table):
        """
            Gets the values of a table from the specified table name.

            Args:
                table   :string:    identifies which table will be accessed

            Returns:
                pd.DataFrame(dictionary):   returns a whole table
        """

        comm = "SELECT id, value FROM {table}"
        comm = comm.format(table=table)

        self.mysql.execute(comm)
        result_set = self.mysql.fetchall()

        id_list = []
        val_list = []

        for row in result_set:
            id_list.append(row["id"])
            val_list.append(row["value"])

        names = ["id", "value"]
        values = [id_list, val_list]

        dictionary = dict(zip(names, values))

        return pd.DataFrame(dictionary)

    def get_path(self):
        """
        Gets the goods, a.k.a. the absolute file path of a dataset.
        """

        comm = "SELECT id FROM {table} WHERE name = {name}"

        self.mysql.execute(comm)

    def comm_exit(self):
        """
        Commits the changes to the database and exits.
        """

        self.dtb_obj.commit()
        self.dtb_obj.close()

    def no_comm_exit(self):
        """
        Doesn't commit the changes to the database and exits.
        """

        self.dtb_obj.rollback()
        self.dtb_obj.close()
