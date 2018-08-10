#!/usr/bin/env python
import PDA
import xyz
import read_g09
import CATC
from sys import exit,argv
import argparse

if __name__=='__main__':
    au2ev=27.211396132
    parser = argparse.ArgumentParser()
    parser.add_argument("-m","--method",help="[PDA] Point Dipole Approximation or \
    [CATC] Coulomb Atomic Transition Charges",required="True")
    parser.add_argument("-u","--units",help="Output unit [ev] electronvolts or [au] Hartrees",type=str,required="True")
    parser.add_argument("input",help="Input files",type=str,nargs='*')
    user_input = argv[1:]
    args = parser.parse_args(user_input)

    ############################
    # Point Dipole Approximation
    ############################
    if args.method.upper()=="PDA":
        if len(args.input)==2:
            g09_1=args.input[0]
            g09_2=args.input[1]
            mol_1=read_g09.get_xyz(g09_1)
            mol_2=read_g09.get_xyz(g09_2)

            coords_1=xyz.xyz_to_matrix(mol_1)
            symbols_1=xyz.symbols_from_xyz(mol_1)
            coords_2=xyz.xyz_to_matrix(mol_2)
            symbols_2=xyz.symbols_from_xyz(mol_2)
            COM_1=PDA.centre_of_mass(symbols_1,coords_1)
            COM_2=PDA.centre_of_mass(symbols_2,coords_2)

            TD_1=read_g09.read_TD(g09_1,1)
            TD_2=read_g09.read_TD(g09_2,1)

            PDA_coupling=PDA.PDA_coupling(TD_1,TD_2,COM_1,COM_2)
            if args.units=="au":
                print("PDA coupling: {:.3f} H".format(PDA_coupling))
            elif args.units=="ev":
                print("PDA coupling: {:.3f} eV".format(PDA_coupling*au2ev))
        else:
            exit("Error! Two G09 output files are needed!\nExiting")
    ############################

    ############################
    # Coulomb ATC method:
    ############################
    elif args.method.upper()=="CATC":
        if len(args.input)==2:
            g09_1=args.input[0]
            g09_2=args.input[1]
            mol_1=read_g09.get_xyz(g09_1)
            mol_2=read_g09.get_xyz(g09_2)
            coords_1=xyz.xyz_to_matrix(mol_1)
            coords_2=xyz.xyz_to_matrix(mol_2)
            NTO_1=read_g09.read_NTO(g09_1,len(mol_1))
            NTO_2=read_g09.read_NTO(g09_2,len(mol_2))

            CATC_coupling=CATC.CATC_coupling(NTO_1,NTO_2,coords_1,coords_2)

            if args.units=="au":
                print("CATC coupling: {:.3f} H".format(CATC_coupling))
            elif args.units=="ev":
                print("CATC coupling: {:.3f} eV".format(CATC_coupling*au2ev))
        else:
            exit("Error! Two G09 output files are needed!\nExiting")
