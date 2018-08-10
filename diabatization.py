#!/usr/bin/env python2

"""
----------------
This script diabatizes two non-adiabatic states to produce a diabatic Hamiltonion,
the off-diagonal elements of which are the couplings J between the two electronic
states.

The diabatization scheme used herein is proposed by Troisi et. al PRL 114, 026402 (2015)
 (https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.114.026402).
 The major detail can be found in the supplementary information,
 where they argue that the exciton coupling J can be
 computed by diabatization of the adiabatic s1 and s2 states of a dimer.
 The best 'diabatic' transformation is yielded by the matrix which minimizes
 the difference between the transition dipole moments of the s1 and s2 states
 of the dimer and the s1 states of the constituent monomers.

 Current implemented properties for diabatization:
    1. Transition diople moments (TDM)
    2. Atomic transtion charges (ATC)

If no option is selected, the TDM scheme is used by default

Usage:

For TDM scheme:

./diabatization.py -p TDM dimer_file.out monomer-1.out monomer-2.out

The three G09 output files must be calculated with the "nosymm" option

For the dimer, the first two excited states must be calculated
For the two constituent monomers, in the dimer config, the first excited states
must be calculated

For the ATC scheme:

./diabatization.py -p ATC dimer_s1.out dimer_s1.out monomer-1.out monomer-2.out dimer.out

dimer_s1 and dimer_s2 contains the Mulliken analysis for the s1 and s2 transitions in the dimer, achieved with:

density=(checkpoint,transition=1) pop=saveNTO

in the G09 input file. This can be done for each state 1 and 2, post the full calculation, which is given in dimer.out.
Monomer-1 and monomer-2 files contain the excited state calculation for the monomer, again stating pop=saveNTO and
density=(transition=1).

The atom numbers must all match for the monomers and dimers.

Enjoy

Michael Dommett
Septmber 2017
m.dommett@qmul.ac.uk
----------------
"""
import numpy as np
from sys import exit,argv
import argparse


def get_TDM(file,state):
    """
    Parses the passed file and gets the transition dipole moment of the specified state

    Accepts G09 output file and excited state number as input

    Parameters
    ----------
    file: list of str
    state: int
    Returns
    ----------
    1x3 matrix of the transition dipole moment
    """

    for linenumber,line in enumerate(file):
        if line==" Ground to excited state transition electric dipole moments (Au):":
            stateline=1+int(state)+linenumber
            break
    TDM=np.matrix(file[stateline].split()[1:4],dtype=float)
    return TDM

def get_ATC(file):
    """
    Parses the passed file and extracts the Mulliken transition densities, using the periodic library to convert these to charges

    Accepts G09 output file as input

    Parameters
    ----------
    file: list of str
    Returns
    ----------
    1xn matrix of the atomic transition charges, where n=number of atoms
    """
    for linenumber,line in enumerate(file):
        if line==" Mulliken charges:":
            start=linenumber+2
        if " Sum of Mulliken charges =" in line:
            stop=linenumber
            break
    ATC=np.matrix([element(str(i.split()[1])).atomic-float(i.split()[2]) for i in file[start:stop]],dtype=float)
    return ATC

def get_energy(file,state):
    """
    Parses the passed file and excited state energy in eV for the specified state

    Accepts G09 output file as input

    Parameters
    ----------
    file: list of str
    state: int
    Returns
    ----------
    float of energy (eV)
    """
    for line in file:
        if " Excited State   {}".format(state) in line:
            energy=float(line.split()[4])
            break
    return energy


def diabatize(dims1,dims2,monA,monB,E1,E2):
    """
    Uses the either the TDMs or ATCs of the s1 and s2 states of the dimer and the s1 state of the two monomers, to
    diabatize the adiabatic Hamiltonian of first two excited states (E1 and E1) to the diabatic
    Hamiltonian, where the off diagonal terms are the couplings J

    Accepts 1xn matrices and state energies as inputs

    Parameters
    ----------
    ATCs1,ATCs2,ATCA,ATCB: 1x3 matrices
    E1,E2: floats
    Returns
    ----------
    2x2 matrix
    """

    dim=np.concatenate((dims1,dims2))
    mon=np.concatenate((monA,monB))

    M=np.dot(dim,mon.T)

    U,s,Vt= np.linalg.svd(M)

    C=(np.dot(U,Vt)).transpose()

    E=np.matrix(([E1,0],[0,E2]))

    H=np.dot(np.dot(C,E),C.transpose())

    return H

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p","--property",help="[TDM] Transition Dipole Moments [TDM] or [ATC] Atomic Transition Charges",default="TDM")
    parser.add_argument("-ms","--monstate",help="Excited state to use for the monomer", default=1)
    parser.add_argument("-ds","--dimstates",help="Excited states to use for the dimer ", nargs=2, default=[1,2])
    parser.add_argument("input", help="Input files",type=str,nargs='*')
    user_input = argv[1:]
    args = parser.parse_args(user_input)

    if args.property.upper()=="TDM":
        if len(args.input)==3:
            dimer=open(args.input[0],"r").read().splitlines()
            monA=open(args.input[1],"r").read().splitlines()
            monB=open(args.input[2],"r").read().splitlines()

            # Dimer data (s1 and s2)
            TDMs1=get_TDM(dimer,args.dimstates[0])
            TDMs2=get_TDM(dimer,args.dimstates[1])
            Es1=get_energy(dimer,args.dimstates[0])
            Es2=get_energy(dimer,args.dimstates[1])

            # Monomer data (s1)
            TDMA=get_TDM(monA,args.monstate)
            TDMB=get_TDM(monB,args.monstate)
            H=diabatize(TDMs1,TDMs2,TDMA,TDMB,Es1,Es2)
            J=H[0,1]
            print("Diabatic Hamiltonian H:\n{}\n".format(H))
            print("J = {:.3f} eV".format(J))
        else:
            exit("Three input files must be specified for the TDM diabatization")

    elif args.property.upper()=="ATC":
        import periodic as pd
        if len(args.input)==5:
            dimer_s1=open(args.input[0],"r").read().splitlines()
            dimer_s2=open(args.input[1],"r").read().splitlines()
            monA=open(args.input[2],"r").read().splitlines()
            monB=open(args.input[3],"r").read().splitlines()
            dimer=open(args.input[4],"r").read().splitlines()

            E1=get_energy(dimer,args.dimstates[0])
            E2=get_energy(dimer,args.dimstates[1])

            ATC_s1=get_ATC(dimer_s1)
            ATC_s2=get_ATC(dimer_s2)

            # Monomer data (s1)
            ATC_A=get_ATC(monA)
            ATC_B=get_ATC(monB)
            ATC_AA=np.concatenate((ATC_A,ATC_A),axis=1)
            ATC_BB=np.concatenate((ATC_B,ATC_B),axis=1)

            H=diabatize(ATC_s1,ATC_s2,ATC_AA,ATC_BB,E1,E2)
            J=H[0,1]
            print("Diabatic Hamiltonian H:\n{}\n".format(H))
            print("J = {:.3f} eV".format(J))
        else:
            exit("Five input files must be specified for the TDM diabatization")

    else:
        exit("I did not understand your property input. Use -p TDM or -p ATC")
