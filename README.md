# Exciton Coupling 

## Introduction

This program allows the user to calculate the exciton coupling between molecular dimers. Based on Kasha's theory,
there are various methods to calculate the exciton coupling, each with their own set of approximations. This package analyses
Gaussain 09 log files and allows the user to calculate the exciton coupling *J* between monomers *i* and *j*
using the following methods:

1. Energy splitting (dE) between the S<sub>1</sub> and S<sub>2</sub> states in a dimer:

    <a href="https://www.codecogs.com/eqnedit.php?latex=J_{ij}=\frac{1}{2}(E_{S_{2}}-E_{S_{1}})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?J_{ij}=\frac{1}{2}(E_{S_{2}}-E_{S_{1}})" title="J_{ij}=\frac{1}{2}(E_{S_{2}}-E_{S_{1}})" /></a>

2. Point dipole approximation (PDA) uses the interaction between transition dipole moments of the monomers:

    <a href="https://www.codecogs.com/eqnedit.php?latex=J_{ij}=\frac{\boldsymbol{\mu}_{i}\boldsymbol{\mu}_{j}}{R^{3}}-\frac{3(\boldsymbol{\mu}_{i}\cdot\boldsymbol{R}_{ij})(\boldsymbol{R}_{ij}\cdot\boldsymbol{\mu}_{j})}{R^{5}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?J_{ij}=\frac{\boldsymbol{\mu}_{i}\boldsymbol{\mu}_{j}}{R^{3}}-\frac{3(\boldsymbol{\mu}_{i}\cdot\boldsymbol{R}_{ij})(\boldsymbol{R}_{ij}\cdot\boldsymbol{\mu}_{j})}{R^{5}}" title="J_{ij}=\frac{\boldsymbol{\mu}_{i}\boldsymbol{\mu}_{j}}{R^{3}}-\frac{3(\boldsymbol{\mu}_{i}\cdot\boldsymbol{R}_{ij})(\boldsymbol{R}_{ij}\cdot\boldsymbol{\mu}_{j})}{R^{5}}" /></a>


3. Coulomb Atomic Transtion Charges (CATC) calculates the Coulomb interaction between the atomic transition charges between the 
ground and excited state of the monomers, where **R**<sup>*i*</sup><sub>*a*</sub> is the position of atom a of chromophore *i*, and N<sup>*i*</sup> <sub>*a*</sub> the number of atoms in chromophore *i*:

   <a href="https://www.codecogs.com/eqnedit.php?latex=J_{ij}=\sum^{N_{i}}_{a}\sum^{M_{j}}_{b}\frac{q_{a}q_{b}}{|\boldsymbol{R}^{i}_{a}-\boldsymbol{R}^{j}_{b}|}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?J_{ij}=\sum^{N_{i}}_{a}\sum^{M_{j}}_{b}\frac{q_{a}q_{b}}{|\boldsymbol{R}^{i}_{a}-\boldsymbol{R}^{j}_{b}|}" title="J_{ij}=\sum^{N_{i}}_{a}\sum^{M_{j}}_{b}\frac{q_{a}q_{b}}{|\boldsymbol{R}^{i}_{a}-\boldsymbol{R}^{j}_{b}|}" /></a>
 
4. The diabatization method of Troisi *et. al.* (*Phys. Rev. Lett.,* **114**, 026402, 2015), where matrix **C** transforms the adiabatic 2x2 Hamiltonian **H<sup>A</sup>**
containing the S<sub>1</sub> and S<sub>2</sub> states of the dimer in the basis of the monomers, yielding the coupling *J<sub>ij</sub>*
on the diagonal of the new, diabatic Hamiltonian **H<sup>A</sup>**:

   <a href="https://www.codecogs.com/eqnedit.php?latex=\boldsymbol{H}^D=\begin{bmatrix}E_{i}^D&space;&&space;J_{ij}\\J_{ij}&space;&&space;E_{j}^D\end{bmatrix}=\begin{bmatrix}C_{11}&space;&&space;C_{12}\\C_{21}&space;&&space;C_{22}\end{bmatrix}\begin{bmatrix}E_{i}^A&space;&&space;0\\0&space;&&space;E_{j}^A\end{bmatrix}\begin{bmatrix}C_{11}&space;&&space;C_{21}\\C_{12}&space;&&space;C_{22}\end{bmatrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\boldsymbol{H}^D=\begin{bmatrix}E_{i}^D&space;&&space;J_{ij}\\J_{ij}&space;&&space;E_{j}^D\end{bmatrix}=\begin{bmatrix}C_{11}&space;&&space;C_{12}\\C_{21}&space;&&space;C_{22}\end{bmatrix}\begin{bmatrix}E_{i}^A&space;&&space;0\\0&space;&&space;E_{j}^A\end{bmatrix}\begin{bmatrix}C_{11}&space;&&space;C_{21}\\C_{12}&space;&&space;C_{22}\end{bmatrix}" title="\boldsymbol{H}^D=\begin{bmatrix}E_{i}^D & J_{ij}\\J_{ij} & E_{j}^D\end{bmatrix}=\begin{bmatrix}C_{11} & C_{12}\\C_{21} & C_{22}\end{bmatrix}\begin{bmatrix}E_{i}^A & 0\\0 & E_{j}^A\end{bmatrix}\begin{bmatrix}C_{11} & C_{21}\\C_{12} & C_{22}\end{bmatrix}" /></a>

There are in theory an infinite number of ways that **C** can perform this transformation. Troisi *et. al.* use a chemical property 
to find the best **C**, through single value decomposition. See the Supporting Information of their [paper](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.114.026402) for more details. In this package,
two methods are implemented:

   4A) Transition dipole moments
   
   4B) Atomic transition charges
    

## Usage

All options of the program are set using the in-built flags and calling the main function, `exciton_coupling.py`. 

#### Flags

`-m`,`--method`

Accepted arguments:
    1. dE
    2. PDA
    3. CATC
    4. DIA


`-u`,`--units`

Accepted arguments:
    1. ev
    2. au

The units of the output coupling must be chosen using the `-u` flag, with `ev` (electron volts) or `au` (atomic units, Hartrees) accepted inputs. 

`-mf`,`--monomerfiles`

Accepted arguments:

The names of the log files containing output from monomer calculations. These only need to be set for methods 2-4. In each case, two files should be given. 

`-df`,`--dimerfiles`


Accepted arguments:

The names of the log files containing output from dimer calculations. These only need to be set for methods 1 and 4. 


`-ms`,`--monstate`

Accepted arguments:

The number of the electronic excitation (1,2,3 ...) used in the monomer calculation. Represents calculating the coupling for the S<sub>N</sub> state.


`-ds`,`--dstate`

Accepted arguments:

The number of the electronic excitation (1,2,3 ...) used in the dimer calculation. Represents calculating the coupling for the S<sub>N</sub> state. For the dE method, the input should be `-ds 1 2`. For the DIA method, the input should ususally be the same but you should check the character of the excitations to ensure that S<sub>1</sub> and S<sub>2</sub> in the dimer match the S<sub>1</sub> of the constituent monomers.

`-p`, `--property `

Accepted arguments:
1. TDM
2. ATC

When using the DIA method, the property chosen to calculate the **C** matrix can be either the transition dipole moment or the atomic transition charges.

## Examples
    
### dE

Requirements: A g09 logfile of a dimer system where the first two excited states are calculated, for example using TD=(Nstates=2) in the Gaussian input file. This will then produce the logfile, for instance dimer.log. The dE exciton coupling is then calculated using:

`exciton_coupling.py -m dE `

