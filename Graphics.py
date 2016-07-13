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
