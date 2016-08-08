"""
@package DakotaFileIO.py
Handles the Dakota file operations.
"""

import dakota


def make_file():
    """
    Creates a Dakota input file (e.g.: file_name.in)

    Args:
        N/A

    Returns:
        name    :string:  The name of the Dakota input file.
    """

    # Create a DAKOTA input file
    name = "uq.in"
    dak = dakota.DakotaInput(environment=["tabular_data",
                                          "  tabular_data_file = 'textbook_uq_sampling.dat'",
                                          "method_pointer = 'UQ'", ],
                             method=["id_method = 'UQ'",
                                     "sampling",
                                     "  sample_type lhs",
                                     "  samples = 20",
                                     "  seed = 98765 rng rnum2",
                                     "  response_levels = 0.1 0.2 0.6",
                                     "                    0.1 0.2 0.6",
                                     "                    0.1 0.2 0.6",
                                     "  distribution cumulative", ],
                             model=["single", ],
                             variables=["uniform_uncertain = 2",
                                        "  lower_bounds =  0.   0.",
                                        "  upper_bounds =  20.   20.",
                                        "  descriptors  = 'x1' 'x2'", ],
                             interface=["analysis_driver =    'text_book'",
                                        "  system",
                                        "  parameters_file = 'data.in'",
                                        "  results_file = 'results.out'",
                                        "  file_tag",
                                        "  file_save", ],
                             responses=["response_functions = 3",
                                        "no_gradients",
                                        "no_hessians", ]
                             )
    dakota.DakotaInput.write_input(dak, infile=name)
    return name


def read_file():
    """
    Parse the output file from Dakota for results.

    Args:
        N/A

    Returns:
        N/A
    """

    print "***WIP***"
