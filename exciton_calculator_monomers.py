#!/usr/bin/env python2
#
#
# Calculate the exciton coupling between constituent monomers in a chromophores,
# based on charges from NTO population analysis
#
#
# Usage:
#
# $ NTO_monomer1.out NTO_monomer2.out
#
# Atom order in the .xyz must match Atom order in the NTO output file


import numpy as np
from itertools import chain
from sys import argv
import sys
from periodic import element

#coords_i = open(argv[1],"r").read().splitlines()
#coords_j = open(argv[2],"r").read().splitlines()
#natoms_i = int(coords_i[0])
#print "Monomer 1 contains {} atoms".format(natoms_i)
#natoms_j = int(coords_j[0])
#print "Monomer 2 contains {} atoms".format(natoms_j)
NTO_i = open(argv[1],"r").read().splitlines()
NTO_j = open(argv[2],"r").read().splitlines()
ang2bohr = 1.8897259885789

def get_coordinates(NTO_file):
    x,y,z = [],[],[]
    for i,j in enumerate(NTO_file):
        if j == " Number     Number       Type             X           Y           Z":
            count = int(i)

    for i,j in enumerate(NTO_file[count+2:]):
        if j == " ---------------------------------------------------------------------":
            natoms = int(i)
            break

    for i in NTO_file[count+2:count+natoms+2]:
        cols = i.split()
        x.append(float(cols[3])*ang2bohr)
        y.append(float(cols[4])*ang2bohr)
        z.append(float(cols[5])*ang2bohr)
    
    return natoms,x,y,z

def get_charges(NTO_file,natoms):

    q = []

    for i,j in enumerate(NTO_file):
        if j == " Mulliken charges:":
            count = int(i)
            break
    charges = NTO_file[(count+2):(count+2+natoms)]
    summed = NTO_file[count+natoms+2].split()
    for line in charges:
        line_charge= line.split()
        atomic_symbol = line_charge[1]
        q.append(element(atomic_symbol).atomic-float(line_charge[2]))
    sumd=0
    for i in q:
        sumd +=float(i)
    print sumd
    return q

natoms_i,x_i,y_i,z_i = get_coordinates(NTO_i)
natoms_j,x_j,y_j,z_j = get_coordinates(NTO_j)
q_i = get_charges(NTO_i,natoms_i)
q_j = get_charges(NTO_j,natoms_j)


J12 = 0
for a in range(0,natoms_i):
    for b in range(0,natoms_j):
        J12 += (q_i[a]*q_j[b])/(np.sqrt((x_i[a]-x_j[b])**2 + (y_i[a]-y_j[b])**2 + (z_i[a]-z_j[b])**2))

output_format=raw_input("Would you like the output in atomic unites [au] or eV [ev]: ")
if output_format == "au":
    print J12
elif output_format == "ev":
    print J12*27.2114
else:
    print "I did not understand how you want the output to be printed. Please enter ev or au"
