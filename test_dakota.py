"""
Uncertainty Quantification
"""

from numpy import array

from dakota import DakotaBase


class TestDriver(DakotaBase):

    def __init__(self):
        super(TestDriver, self).__init__()
        self.force_exception = False

        self.input.environment = [
            "tabular_data",
            "  tabular_data_file = 'textbook_uq_sampling.dat'",
            "method_pointer = 'UQ'",
        ]
        self.input.model = [
            "single",
        ]
        self.input.method = [
            "id_method = 'UQ'",  #"optpp_newton",
            "sampling",
            "  sample_type lhs",
            "  samples = 10",
            "  seed = 98765 rng rnum2",
            "  response_levels = 0.1 0.2 0.6",
            "                    0.1 0.2 0.6",
            "                    0.1 0.2 0.6",
            "  distribution cumulative",
        ]
        self.input.variables = [
            "uniform_uncertain = 2",
            "  lower_bounds =  0.   0.",
            "  upper_bounds =  1.   1.",
            "  descriptors  = 'x1' 'x2'",
        ]
        self.input.interface = [
            "python",
            "  numpy",
            "  analysis_drivers = 'dakota:dakota_callback'",
        ]
        self.input.responses = [
            "response_functions = 3",
            "no_gradients",
            "no_hessians",
        ]

    def dakota_callback(self, **kwargs):
        """
        Return responses from parameters.  `kwargs` contains:

        =================== ==============================================
        Key                 Definition
        =================== ==============================================
        functions           number of functions (responses, constraints)
        ------------------- ----------------------------------------------
        variables           total number of variables
        ------------------- ----------------------------------------------
        cv                  list/array of continuous variable values
        ------------------- ----------------------------------------------
        div                 list/array of discrete integer variable values
        ------------------- ----------------------------------------------
        drv                 list/array of discrete real variable values
        ------------------- ----------------------------------------------
        av                  single list/array of all variable values
        ------------------- ----------------------------------------------
        cv_labels           continuous variable labels
        ------------------- ----------------------------------------------
        div_labels          discrete integer variable labels
        ------------------- ----------------------------------------------
        drv_labels          discrete real variable labels
        ------------------- ----------------------------------------------
        av_labels           all variable labels
        ------------------- ----------------------------------------------
        asv                 active set vector (bit1=f, bit2=df, bit3=d^2f)
        ------------------- ----------------------------------------------
        dvv                 derivative variables vector
        ------------------- ----------------------------------------------
        currEvalId          current evaluation ID number
        ------------------- ----------------------------------------------
        analysis_components str(id(self))
        =================== ==============================================

        """
        print 'dakota_callback:'
        cv = kwargs['cv']
        asv = kwargs['asv']
        print '    cv', cv
        print '    asv', asv

        # Rosenbrock function.
        x = cv
        f0 = x[1] - x[0] * x[0]
        f1 = 1 - x[0]

        retval = dict()

        f = array([100 * f0 * f0 + f1 * f1])
        retval['fns'] = asv

        #try:
        #    if asv[0] & 1:
        #        f = array([100 * f0 * f0 + f1 * f1])
        #        retval['fns'] = f

        #    if asv[0] & 2:
        #        g = array([[-400 * f0 * x[0] - 2 * f1, 200 * f0]])
        #        retval['fnGrads'] = g

        #    if asv[0] & 4:
        #        fx = x[1] - 3 * x[0] * x[0]
        #        h = array([[[-400 * fx + 2, -400 * x[0]],
        #                    [-400 * x[0], 200]]])
        #        retval['fnHessians'] = h

        #    if self.force_exception:
        #        raise RuntimeError('Forced exception')

        # except Exception, exc:
        #    print '    caught', exc
        #    raise

        print '    returning', retval
        return retval

    def run(self):
        self.run_dakota()
