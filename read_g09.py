""" Read and extracts information from gaussian 09 log files
"""
from periodic import element
def get_xyz(g09_file):
    """
    Opens a g09 log file and returns the first geometry in Input orientation.
    Iterators are used so that the file is not all loaded into memory, which
    can be expensive.

    The function searches for the following text pattern in the log file:

                            Input orientation:
    ---------------------------------------------------------------------
    Center     Atomic      Atomic             Coordinates (Angstroms)
    Number     Number       Type             X           Y           Z
    ---------------------------------------------------------------------

    And will save the coordinates and the atomic symbols succeeding it
    Parameters
    ----------
    g09_file: Path to g09 log file
        File path

    Returns
    ----------
    List of lists: List of lists
        Outer list is whole xyz file, each inner list is a line of the file containing
        the symbol and x,y,z coordinates

    """
    with open(g09_file) as f:
        # Get the number of atoms so we can iterate without loading the file into memory
        for i,line in enumerate(f
            # Ensures line is not blank
            if line.strip():
                if line.split()[0]=="NAtoms=":
                    natoms=(int(line.split()[3]))
                    break
        # Will hold the coordinates and symbols
        coords=[]
        # Reset the iterator to the top of the file
        f.seek(0)
        for i,line in enumerate(f):
            if line.strip():
                if "Input orientation:" in line:
                    for i in range(5):
                        # Skip 5 lines to start of coordinates
                        line=f.next()
                    for i in range(natoms):
                        linesplit=line.split()
                        symb=str(element(linesplit[1]).symbol)
                        x=float(linesplit[3])
                        y=float(linesplit[4])
                        z=float(linesplit[5])
                        coords.append([symb,x,y,z])
                        line=f.next()
                    break
        return coords

    
