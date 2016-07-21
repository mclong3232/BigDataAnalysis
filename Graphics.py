from rpy2 import robjects
from rpy2.robjects import Formula
from rpy2.robjects.packages import importr


def display_graphics(dataset):

    # The R 'print' function
    rprint = robjects.globalenv.get("print")

    lattice = importr('lattice')

    formula = Formula('id ~ value')
    formula.getenvironment()['id'] = dataset['id'].tolist()
    formula.getenvironment()['value'] = dataset['value'].tolist()

    p = lattice.xyplot(formula)
    rprint(p)

    raw_input()


def graph_sets(datab):

    print "Liver_UF_Control_rep2"
    dataset = datab.get_set("GSM576077")
    display_graphics(dataset)

    print "Liver_A_Exposed_rep2"
    dataset = datab.get_set("GSM576083")
    display_graphics(dataset)

    print "Liver_B_Exposed_rep2"
    dataset = datab.get_set("GSM576086")
    display_graphics(dataset)

    print "Liver_D_Ref_rep2"
    dataset = datab.get_set("GSM576084")
    display_graphics(dataset)

    print "Liver_E_Exposed_rep2"
    dataset = datab.get_set("GSM576081")
    display_graphics(dataset)

    print "Testis_UF_Control_rep2"
    dataset = datab.get_set("GSM576102")
    display_graphics(dataset)

    print "Testis_A_Exposed_rep2"
    dataset = datab.get_set("GSM576103")
    display_graphics(dataset)

    print "Testis_B_Exposed_rep2"
    dataset = datab.get_set("GSM576106")
    display_graphics(dataset)

    print "Testis_D_Ref_rep3"
    dataset = datab.get_set("GSM576100")
    display_graphics(dataset)

    print "Testis_E_Exposed_rep2"
    dataset = datab.get_set("GSM576105")
    display_graphics(dataset)
