#!/usr/bin/env python2

import numpy as np
from itertools import chain
from sys import argv
import sys
from periodic import element

def group_to_range(group):
  group = ''.join(group.split())
  sign, g = ('-', group[1:]) if group.startswith('-') else ('', group)
  r = g.split('-', 1)
  r[0] = sign + r[0]
  r = sorted(int(__) for __ in r)
  return range(r[0], 1 + r[-1])

def rangeexpand(txt):
  ranges = chain.from_iterable(group_to_range(__) for __ in txt.split(','))
  return sorted(set(ranges))

def read_coordinates(txtfile,atomic_no,x,y,z):
    for i,j in enumerate(txtfile):
        if j == " Number     Number       Type             X           Y           Z":
                count = int(i)
                break

    
    xyz = infile_lines[(count+2):(count+2+natoms)]
    for row in xyz:
        coords = row.split()
        atomic_no.append(float(coords[1]))
        x.append(float(coords[3]))
        y.append(float(coords[4]))
        z.append(float(coords[5]))
        
        
    return atomic_no,x,y,z

def get_charges(txtfile,q):
    for i,j in enumerate(txtfile):
        if j == "          Condensed to atoms (all electrons):":
            count = int(i)
            break
    
    charges = txtfile[(count+3):(count+3+natoms)]
    summed = txtfile[count+natoms+3].split()

    for i,line in enumerate(charges):
        line_charge= line.split()
        q.append(int(element(line_charge[1]).atomic)-float(line_charge[2])) 
    return q

molecule = open("molecule","r")
molecule_lines = molecule.read().splitlines()
natoms = int(molecule_lines[0])
chrom1 = rangeexpand(molecule_lines[1])
chrom2 = rangeexpand(molecule_lines[2])
print "Unit 1: {0} atoms".format(len(np.unique(chrom1)))
print "Unit 2: {0} atoms".format(len(np.unique(chrom2)))
if len(np.unique(chrom1+chrom2)) != natoms:
    print "You have made a mistake in the molecule input!\nThe number of atoms specified is not equal to the total.\nPlease fix the molecule input and retry."
    missing = sorted(set(range(1, natoms)).difference(np.unique(chrom1+chrom2)))
    print "The missing atom number(s) is: {0}".format(missing) 
    sys.exit()
if len(chrom1)+len(chrom2) != natoms:
    print "The total number of atoms is {0}, but there are {1} atoms in the two units!\nPlease fix the molecule input and retry.".format(natoms,len(chrom1)+len(chrom2))
    sys.exit()
    
infile = open(argv[1],"r")
infile_lines = infile.read().splitlines()
atomic_no,x,y,z = [],[],[],[]
read_coordinates(infile_lines,atomic_no,x,y,z)
q = []
get_charges(infile_lines,q)

    
J12 = 0
for i in chrom1:
    for j in chrom2:
        atomi = int(i)-1
        atomj = int(j)-1

        J12 += ((q[atomi]*q[atomj])/(np.sqrt((x[atomi]-x[atomj])**2 + (y[atomi]-y[atomj])**2 + (z[atomi]-z[atomj])**2)))
print "Total charge: {0:.3f} au".format(abs(np.sum(q)))
print "J Coupling: {0:.6f} au".format(J12)


