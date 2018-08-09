""" Opens xyz files and returns the atoms and cooridnates in various forms
"""
def open_xyz(xyz_file):
    """
    Opens an xyz file and returns a list of lists

    Parameters
    ----------
    xyz_file: String containing file location

    Returns
    ----------
    List of lists: List of lists, where each inner list contains symbol,x,y,z
    """
    file=open(xyz_file,'r').read().splitlines()
    # Check if first line contains number of atoms
    if len(file[0])!= 1:
        raise ValueError("Not a proper xyz file!")
        exit()
    natoms = int(file[0])
    if natoms != len(file[2:]):
        raise ValueError("Number of atoms not equal to file header!")
