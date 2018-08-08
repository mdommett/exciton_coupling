#!/usr/bin/env python2

import numpy as np
from itertools import chain
from sys import argv
import sys
from periodic import element
import math
import operator

#########################################################################################
#
# $ PDA_calculator.py monomer_1.xyz monomer_2.xyz monomer_1_TDM.out monomer_2_TDM.out
#
#########################################################################################

ang2bohr = 1.8897259885789

coords_i = open(argv[1],"r").read().splitlines()
natoms_i = int(coords_i[0])
coords_j = open(argv[2],"r").read().splitlines()
natoms_j = int(coords_j[0])
symbol,x,y,z,q,atomic_no = [],[],[],[],[],[]
G09_i = open(argv[3],"r").read().splitlines()
G09_j = open(argv[4],"r").read().splitlines()

# Get atomic coordinates from the .xyz file of the dimer

def read_coords(natoms,coords,symbol,x,y,z):
    
 
    for line in coords[2:natoms+2]:
        coord = line.split()
        symbol.append(coord[0])
        x.append(float(coord[1])*ang2bohr)
        y.append(float(coord[2])*ang2bohr)
        z.append(float(coord[3])*ang2bohr)
    
    return symbol,x,y,z 
    
# Calculate the Centre of Mass (CoM) for each of the monomers in the dimer .xyz file

def centre_of_mass(natoms,list_of_symbols,x_coords,y_coords,z_coords):
    Xnumerator,Ynumerator,Znumerator,Xdenominator,Ydenominator,Zdenominator=0,0,0,0,0,0
    for i in range(natoms):
        Xnumerator += element(list_of_symbols[i]).mass*x_coords[i]
        Ynumerator += element(list_of_symbols[i]).mass*y_coords[i]
        Znumerator += element(list_of_symbols[i]).mass*z_coords[i]
        Xdenominator += element(list_of_symbols[i]).mass
        Ydenominator += element(list_of_symbols[i]).mass
        Zdenominator += element(list_of_symbols[i]).mass

    Xcm = Xnumerator/Xdenominator
    Ycm = Ynumerator/Ydenominator
    Zcm = Znumerator/Zdenominator
    
    return Xcm,Ycm,Zcm


def vector_distance(x1,y1,z1,x2,y2,z2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2-z1)**2)
    return dist


symbols_i,X_i,Y_i,Z_i = [],[],[],[] # monomer 1 coordinates
read_coords(natoms_i,coords_i,symbols_i,X_i,Y_i,Z_i)
symbols_j,X_j,Y_j,Z_j = [],[],[],[] # monomer 2 coordinates
read_coords(natoms_j,coords_j,symbols_j,X_j,Y_j,Z_j)

Xicm,Yicm,Zicm = centre_of_mass(natoms_i,symbols_i,X_i,Y_i,Z_i)
Xjcm,Yjcm,Zjcm = centre_of_mass(natoms_j,symbols_j,X_j,Y_j,Z_j)


CMi = (Xicm,Yicm,Zicm)
CMj = (Xjcm,Yjcm,Zjcm)
CMij = (Xjcm-Xicm,Yjcm-Yicm,Zjcm-Zicm)
print CMi
print CMj
print CMij

# Get the line number where the transition electric dipole moment is stored in each monomer calculation output file    

for i,j in enumerate(G09_i):
    if j == ' Ground to excited state transition electric dipole moments (Au):':
        count_i = int(i)
        break
for i,j in enumerate(G09_j):
    if j == ' Ground to excited state transition electric dipole moments (Au):':
        count_j = int(i)
        break
# Get the right excitation TDM, assign x,y,z components for each monomer of the dimer

state=int(raw_input("Use the transition dipole moment of excited state: "))

tdmvector_i = G09_i[count_i+state+1].split()
TDMix = float(tdmvector_i[1])
TDMiy = float(tdmvector_i[2])
TDMiz = float(tdmvector_i[3])
TDMi = (TDMix,TDMiy,TDMiz)

tdmvector_j = G09_j[count_j+state+1].split()
TDMjx = float(tdmvector_j[1])
TDMjy = float(tdmvector_j[2])
TDMjz = float(tdmvector_j[3])
TDMj = (TDMjx,TDMjy,TDMjz)

print TDMi,TDMj
A = np.dot(TDMi,TDMj)/((vector_distance(Xicm,Yicm,Zicm,Xjcm,Yjcm,Zjcm))**3)
B = (3*(np.dot(TDMi,CMij)*(np.dot(CMij,TDMj))))/((vector_distance(Xicm,Yicm,Zicm,Xjcm,Yjcm,Zjcm))**5)
print "A: {}".format(A)
print "B: {}".format(B)

output_format=raw_input("Would you like the output in atomic unites [au] or eV [ev]: ")
if output_format == "au":
    print A-B
elif output_format == "ev":
    print (A-B)*27.2114
else:
    print "I did not understand how you want the output to be printed. Please enter ev or au"


