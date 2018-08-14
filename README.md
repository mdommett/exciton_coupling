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
    
## Requirements

The `exciton_coupling` is written in python3 are requires the following packages to be installed and in the python path:

`numpy`

`periodic`

`sys`

`argparse`

## Installation

1. Git clone this repository to the desired location on your local computer:

`git clone https://github.com/mdommett/exciton_coupling.git`

2. Change into `exciton_coupling` parent directory:

`cd exciton_coupling`

3. Ensure you have the required packages installed:

`pip3 install -r requirements.txt`

4. Add the location of the parent directory to your $PATH and $PYTHONPATH in your bashrc or bash_profile:

`export exciton_coupling=/path/to/parent/directory`

`export PYTHONPATH=$exciton_coupling:$PYTHONPATH`

`export PATH=$exciton_coupling:$PATH`
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

A g09 logfile of a dimer system is required, where the first two excited states are calculated, for example using TD=(Nstates=2) in the Gaussian input file. This will then produce the logfile, for instance dimer.log. The dE exciton coupling is then calculated using:

`exciton_coupling.py -m dE -df dimer.log -ds 1 2 -u ev `

where the output will be in eV and the  S<sub>1</sub> and  S<sub>2</sub> states are used. 

### PDA

Two g09 logfiles are required; one for each monomer. The nosymm option should be used:

`exciton_coupling.py -m PDA -mf mon_1.log mon_2.log -u ev `

### CATC

Two g09 logfiles are required; one for each monomer. The nosymm option should be used. The ATC charges are caclulated in the Gaussian by requesting Population=(NTO,Transition=1) for the first excited state. 

`exciton_coupling.py -m CATC -mf mon_1.log mon_2.log -u ev `

### DIA

#### TDM (Recommended)

The DIA method using the transition dipole vectors (TDM) requires three log files; one dimer calculation and two monomer files. The atomic positions of the monomers in the monomer calculations should exactly match those in the dimer file. The nosymm option should be used in all three calculations. To calculate the coupling using the S<sub>1</sub> and S<sub>2</sub> states, using the DIA-TDM method, the following input should be used:

`exciton_coupling.py -m DIA -p TDM -df dimer.log -mf mon_1.log mon_2.log -ds 1 2 -ms 1 -u ev.`

#### ATC 

The DIA method using the atomic transition charges (ATC) requires *five* log files; three dimer files, and two monomer files. 

The dimer files:
1. An initial dimer calculation to calculate the energy and the *densities*. For example:

`%chk=dimer
  #P WB97XD/def2-SVP TD=(nstates=2) density=all `
  
Upon completion of this calculation, two further calculations should be performed on the dimer, one for each electronic state, where the input should be:

`%chk=dimer
  #P WB97XD/def2-SVP density=(Read,Transition=1) `

This will read the density of the first electronic transition and save the charges in the population analysis. The same should be done for the second state:

`%chk=dimer
  #P WB97XD/def2-SVP density=(Read,Transition=2) `
  
The output files should be saved as separate names, for instance as `dimer.log`, `dimer_s1.log` and `dimer_s2.log`. In the progam, the energy is read from `dimer.log` while the charges are read from the `dimer_s1.log` and `dimer_s2.log` files. For the monomer files, the following input can be used:

`%chk=mon_1
  #P WB97XD/def2-SVP TD=(nstates=1) density=(Transition=1)`
  
  and
  
  
`%chk=mon_2
  #P WB97XD/def2-SVP TD=(nstates=1) density=(Transition=1)`
  
Once all five files are created, the exciton coupling can be calculated using:

`exciton_coupling.py -m DIA -p ATC -df dimer.log dimer_s1.log dimer_s2.log -mf mon_1.log mon_2.log -ds 1 2 -ms 1 -u ev.` 

Examples of each usage are given in the `examples/` directory.




