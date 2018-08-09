"""Contains the tools required to calculate the exciton coupling based on PDA

The point dipole appromixation (PDA) calculates the exciton coupling based upon
the interaction between the transition dipoles of the two systems,

J = u1*u2/R12^5 - 3(u1*R12)(R12*u2) / R12^5

where u1 and u2 are the TD vectors of the two systems and R12 is the vector
between their centre of masses.
"""
import numpy as np
from periodic import element
def centre_of_mass(symbols,coordinates):
    """
    Calculates the centre of mass (COM) for a set of atomic positions, based on:

    COM_x = m1x1 + m2x2 + ... + mnxn / m1 + m2 + ... + mn
    COM_y = m1y1 + m2y2 + ... + mnyn / m1 + m2 + ... + mn
    COM_z = m1z1 + m2z2 + ... + mnzn / m1 + m2 + ... + mn

    Parameters
    ----------
    symbols: List of strings
        List of elemental symbols
    coordinates: Nx3 array of floats
        Array of x,y,z coordinates
    Returns
    ----------
    COM_x,COM_y,COM_z: Floats of centre of mass of x,y,z coordinate
    """
    if len(symbols)!=len(coordinates):
        exit("Inputs not of the same dimension!")

    masses = np.array([element(i).mass for i in symbols])
    mass_sum = np.sum(masses)

    x_coords=coordinates[:,0]
    y_coords=coordinates[:,1]
    z_coords=coordinates[:,2]
    x_numerator=np.sum(np.dot(masses,x_coords))
    y_numerator=np.sum(np.dot(masses,y_coords))
    z_numerator=np.sum(np.dot(masses,z_coords))

    COM_x = x_numerator/mass_sum
    COM_y = y_numerator/mass_sum
    COM_z = z_numerator/mass_sum
    return COM_x,COM_y,COM_z
