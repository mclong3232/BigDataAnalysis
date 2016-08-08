"""
@package Initializer.py
Initializes a database and the extraction of data from the .soft biological dataset.
"""
import Node
import LinkedList

import sys
import math
import GEOparse
import time
import pickle
import csv
from itertools import izip


def init(datab):
    """
        Initializes a database and loads all the datasets into it.

        Args:
            datab   :Database:  a database object, as defined in "Database.py"

        Returns:
            N/A
    """

    try:
        # Try to open the pickle first
        infile = open("dataSets.pkl", 'r')

    except IOError:

        # Pickle didn't exist, going the long way
        gse = GEOparse.get_GEO(filepath="./GSE23521_family.soft")
        outfile = open("dataSets.pkl", 'w')
        datasets = LinkedList.LinkedList()

        # Load the data sets into a list
        sys.stdout.write('\nLoading data sets .')

        # Log the time it takes to complete.
        start_time = time.time()

        for gsm_name, gsm in gse.gsms.iteritems():
            dataset = Node.Node(gsm_name)

            # Add data into the lists for the current node
            for key, i_d in gsm.table.iterrows():
                if math.isnan(i_d.values.item(0)) is False:
                    dataset.idList.append(i_d.values.item(0))
                    if math.isnan(i_d.values.item(1)) is False:
                        dataset.valList.append(i_d.values.item(1))
                    else:
                        dataset.valList.append(0)

            # Output individual datasets to .csv files
            with open(gsm_name + ".csv", 'wb') as f:
                writer = csv.writer(f)
                writer.writerows(izip(dataset.idList, dataset.valList))

            datasets.insert(dataset)
            sys.stdout.write('.')

        print("\n\n--- %.2f seconds for reading files and loading into linked list ---" % (time.time() - start_time))

        print "\n\n-------------------------------"
        print "Loaded", datasets.size(), "data sets into a list."
        print "-------------------------------\n\n"

        pickle.dump(datasets, outfile)

    else:

        # Pickle found, so load it.
        print "Loading datasets from pickle...\n"
        datasets = pickle.load(infile)

    # Adds the data sets into the database sequentially.
    node = datasets.head

    # Log the time it takes to complete.
    start_time = time.time()

    while node is not None:
        print "Adding dataset '" + node.name + "' to the database 'signal_intensity'"
        datab.add_table("signal_intensity", node.name)

        i = 0
        while i < len(node.idList):
            datab.add_row(node.name, node.idList[i], node.valList[i])
            i += 1
        node = node.get_next()

    print("\n--- %.2f seconds for loading linked list into database ---" % (time.time() - start_time))
