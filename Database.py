# Module:  Database.py
import MySQLdb
import os
import glob
import pandas as pd


class MyDatabase:
    """Definitions and methods for a database connection"""

    def __init__(self, host, user, password, db):
        """Initialize a MySQL database connection.

        Receives host, user, password, and name of database to connect to.
        """

        self.dtb = MySQLdb
        self.dtb_obj = self.dtb.connect(host=host,  # your host, usually localhost
                                        user=user,  # your username
                                        passwd=password,  # your password
                                        db=db)  # name of the data base
        self.mysql = self.dtb_obj.cursor(MySQLdb.cursors.DictCursor)

    @staticmethod
    def get_files():
        # Choose the path to pull files from
        path = os.getcwd()

        return glob.glob(path + "/*.csv")

    def add_table(self, db, table):
        """Adds a table into the specified schema of a MySQL database.

        Receives the name of the schema and the name of the table.
        """

        comm = """CREATE TABLE `{db}`.`{table}` (
               `id` INT NOT NULL,
               `value` FLOAT NOT NULL,
               PRIMARY KEY (`id`, `value`));"""
        comm = comm.format(db=db, table=table)
        self.mysql.execute(comm)

    def add_row(self, table, id_, value):
        """Adds a row into the specified table.

        Receives the name of the table, and the values to be added.
        """

        comm = "INSERT INTO `{table}` () " \
               "VALUES ({id}, {value});"
        comm = comm.format(table=table, id=id_, value=value)
        self.mysql.execute(comm)

    def del_row(self, table, name, limit):
        """Deletes a row from the specified table.

        Receives the name of the table and the name and limit of the deletion.
        """

        comm = "DELETE FROM {table} WHERE name = '{name}' LIMIT {limit}"
        comm = comm.format(table=table, name=name, limit=limit)

        self.mysql.execute(comm)

    def get_row(self, table, name):
        """Gets the values of a row from the specified table and name.

        Receives the name of the table and the named to search for.
        """

        comm = "SELECT id FROM {table} WHERE name = {name}"
        comm = comm.format(table=table, name=name)

        self.mysql.execute(comm)
        row = self.mysql.fetchone()

        return row

    def get_set(self, table):
        """Gets the values of a row from the specified table and name.

        Receives the name of the table and the named to search for.
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
        """Gets the goods, a.k.a. the absolute file path of a dataset."""

        comm = "SELECT id FROM {table} WHERE name = {name}"

        self.mysql.execute(comm)

    def comm_exit(self):
        """Commits the changes to the database and exits."""

        self.dtb_obj.commit()
        self.dtb_obj.close()

    def no_comm_exit(self):
        """Doesn't commit the changes to the database and exits."""

        self.dtb_obj.rollback()
        self.dtb_obj.close()
