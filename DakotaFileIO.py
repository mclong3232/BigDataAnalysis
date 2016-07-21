# Module:  DakotaFileIO.py
import dakota


def make_file():
    # Create a DAKOTA input file
    name = "uq.in"
    dak = dakota.DakotaInput()
    dakota.DakotaInput.write_input(dak, infile=name)
    return name


def read_file():
    # Stuff
    print "lol"
