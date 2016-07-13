# Module:  Statistics.py
import pickle

import pandas as pd
from scipy import stats


def anova():
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
