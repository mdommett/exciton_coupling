"""Contains the tools required to calculate the exciton coupling based on PDA

The point dipole appromixation (PDA) calculates the exciton coupling based upon
the interaction between the transition dipoles of the two systems,

J = u1*u2/R12^5 - 3(u1*R12)(R12*u2) / R12^5

where u1 and u2 are the TD vectors of the two systems and R12 is the vector
between their centre of masses.
"""

def centre_of_mass(symbols,x_coords,y_coords,z_coords):
    """
    Calculates the centre of mass for a set of atomic positions

    Parameters
    ----------
    symbols: List of strings
        List of elemental symbols
    x_coords: List of floats
        List of x-coordinate positions
    y_coords: List of floats
        List of y-coordinate positions
    z_coords: List of floats
        List of z-coordinate positions

    Returns
    ----------
    Xcm,Ycm,Zcm: Floats of centre of mass of x,y,z coordinate
    """
    params=[symbols,x_coords,y_coords,z_coords]
    n = len(params[0])
    if all(len(x) != n for x in params):
        raise ValueError("Inputs not of the same dimension!")
    Xnumerator,Ynumerator,Znumerator,Xdenominator,Ydenominator,Zdenominator=0,0,0,0,0,0

    for i in range(natoms):
        Xnumerator += element(symbols[i]).mass*x_coords[i]
        Ynumerator += element(symbols[i]).mass*y_coords[i]
        Znumerator += element(symbols[i]).mass*z_coords[i]
        Xdenominator += element(list_of_symbols[i]).mass
        Ydenominator += element(list_of_symbols[i]).mass
        Zdenominator += element(list_of_symbols[i]).mass

    Xcm = Xnumerator/Xdenominator
    Ycm = Ynumerator/Ydenominator
    Zcm = Znumerator/Zdenominator

    return Xcm,Ycm,Zcm
