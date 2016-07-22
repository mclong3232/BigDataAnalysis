# Module:  DakotaFileIO.py
import dakota


def make_file():
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
                                        "  upper_bounds =  1.   1.",
                                        "  descriptors  = 'x1' 'x2'", ],
                             interface=["direct",
                                        "analysis_driver =    'text_book'", ],
                             responses=["response_functions = 3",
                                        "no_gradients",
                                        "no_hessians", ]
                             )
    dakota.DakotaInput.write_input(dak, infile=name)
    return name


def read_file():
    # Stuff
    print "lol"
