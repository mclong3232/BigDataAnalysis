"""
@package Analysis.py
Handles the analysis functions of the program.
"""

import DakotaFileIO
import pickle
import dakota
import pandas as pd
from scipy import stats


def anova():
    """
        Performs an analysis of variance of a dataset

        Args:
            N/A

        Returns:
            N/A
    """

    infile = open("dataSets.pkl", 'r')
    datasets = pickle.load(infile)

    node = datasets.head
    targets = ["GSM576073", "GSM576077", "GSM576082", "GSM576090"]
    df_list = []

    while node is not None:
        if node.name in targets:
            print node.name
            df = pd.DataFrame({'value': node.valList})
            df_list.append(df)
        node = node.get_next()

    f_val, p_val = stats.f_oneway(*df_list)

    print "One-way ANOVA p-value = ", p_val[0]


def uq():
    """
        Performs an uncertainty quantification analysis on the data using Dakota

        Args:
            N/A

        Returns:
            N/A (WIP:  function not finished)
    """

    name = DakotaFileIO.make_file()
    dakota.run_dakota(infile=name, stdout="dakota_results.out", stderr="dakota_results.err")
    return DakotaFileIO.read_file()
