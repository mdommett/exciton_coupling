# Exciton Coupling 

This program allows the user to calculate the exciton coupling between molecular dimers. Based on Kasha's theory,
there are various methods to calculate the exciton coupling, each with their own set of approximations. This package analyses
Gaussain 09 log files and allows the user to calculate the exciton coupling *J* between monomers *i* and *j*
using the following methods:

1. Energy splitting (dE) between the S<sub>1</sub> and S<sub>2</sub> states in a dimer:

    <img src="http://www.sciweavers.org/tex2img.php?eq=J_%7Bij%7D%3D%5Cfrac%7B1%7D%7B2%7D%28E_%7BS_%7B2%7D%7D-E_%7BS_%7B1%7D%7D%29&bc=White&fc=Black&im=gif&fs=12&ff=modern&edit=0" align="center" border="0" alt="J_{ij}=\frac{1}{2}(E_{S_{2}}-E_{S_{1}})" width="139" height="36" />
2. Point dipole approximation (PDA) uses the interaction between transition dipole moments of the monomers:

    <img src="http://www.sciweavers.org/tex2img.php?eq=J_%7Bij%7D%3D%5Cfrac%7B%5Cboldsymbol%7B%5Cmu%7D_%7Bi%7D%5Cboldsymbol%7B%5Cmu%7D_%7Bj%7D%7D%7BR%5E%7B3%7D%7D-%5Cfrac%7B3%28%5Cboldsymbol%7B%5Cmu%7D_%7Bi%7D%5Ccdot%5Cboldsymbol%7BR%7D_%7Bij%7D%29%28%5Cboldsymbol%7BR%7D_%7Bij%7D%5Ccdot%5Cboldsymbol%7B%5Cmu%7D_%7Bj%7D%29%7D%7BR%5E%7B5%7D%7D&bc=White&fc=Black&im=gif&fs=12&ff=modern&edit=0" align="center" border="0" alt="J_{ij}=\frac{\boldsymbol{\mu}_{i}\boldsymbol{\mu}_{j}}{R^{3}}-\frac{3(\boldsymbol{\mu}_{i}\cdot\boldsymbol{R}_{ij})(\boldsymbol{R}_{ij}\cdot\boldsymbol{\mu}_{j})}{R^{5}}" width="244" height="39" />

3. Coulomb Atomic Transtion Charges (CATC) calculates the Coulomb interaction between the atomic transition charges between the 
ground and excited state of the monomers, where **R**<sup>*i*</sup><sub>*a*</sub> is the position of atom a of chromophore *i*, and N<sup>*i*</sup> <sub>*a*</sub> the number of atoms in chromophore *i*:

    <img src="http://www.sciweavers.org/tex2img.php?eq=J_%7Bij%7D%3D%5Csum%5E%7BN_%7Bi%7D%7D_%7Ba%7D%5Csum%5E%7BM_%7Bj%7D%7D_%7Bb%7D%5Cfrac%7Bq_%7Ba%7Dq_%7Bb%7D%7D%7B%7C%5Cboldsymbol%7BR%7D%5E%7Bi%7D_%7Ba%7D-%5Cboldsymbol%7BR%7D%5E%7Bj%7D_%7Bb%7D%7C%7D&bc=White&fc=Black&im=gif&fs=12&ff=modern&edit=0" align="center" border="0" alt="J_{ij}=\sum^{N_{i}}_{a}\sum^{M_{j}}_{b}\frac{q_{a}q_{b}}{|\boldsymbol{R}^{i}_{a}-\boldsymbol{R}^{j}_{b}|}" width="174" height="53" />
 
4. The diabatization method of Troisi *et. al.* (*Phys. Rev. Lett.,* **114**, 026402, 2015), where matrix **C** transforms the adiabatic 2x2 Hamiltonian **H<sup>A</sup>**
containing the S<sub>1</sub> and S<sub>2</sub> states of the dimer in the basis of the monomers, yielding the coupling *J<sub>ij</sub>*
on the diagonal of the new, diabatic Hamiltonian **H<sup>A</sup>**:

    
    <img src="http://www.sciweavers.org/tex2img.php?eq=%5Cboldsymbol%7BH%7D%5ED%3D%0A%5Cbegin%7Bbmatrix%7D%0AE_%7Bi%7D%5ED%20%26%20J_%7Bij%7D%5C%5C%0AJ_%7Bij%7D%20%26%20E_%7Bj%7D%5ED%0A%5Cend%7Bbmatrix%7D%0A%3D%0A%5Cbegin%7Bbmatrix%7D%0AC_%7B11%7D%20%26%20C_%7B12%7D%5C%5C%0AC_%7B21%7D%20%26%20C_%7B22%7D%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0AE_%7Bi%7D%5EA%20%26%200%5C%5C%0A0%20%26%20E_%7Bj%7D%5EA%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0AC_%7B11%7D%20%26%20C_%7B21%7D%5C%5C%0AC_%7B12%7D%20%26%20C_%7B22%7D%0A%5Cend%7Bbmatrix%7D&bc=White&fc=Black&im=gif&fs=12&ff=modern&edit=0" align="center" border="0" alt="\boldsymbol{H}^D=\begin{bmatrix}E_{i}^D & J_{ij}\\J_{ij} & E_{j}^D\end{bmatrix}=\begin{bmatrix}C_{11} & C_{12}\\C_{21} & C_{22}\end{bmatrix}\begin{bmatrix}E_{i}^A & 0\\0 & E_{j}^A\end{bmatrix}\begin{bmatrix}C_{11} & C_{21}\\C_{12} & C_{22}\end{bmatrix}" width="394" height="43" />

There are in theory an infinite number of ways that **C** can perform this transformation. Troisi *et. al.* use a chemical property 
to find the best **C**, through single value decomposition. See the Supporting Information of their [paper](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.114.026402) for more details. In this package,
two methods are implemented:

4A) Transition dipole moments
   
4B) Atomic transition charges
    
 Please see the documentation and tutorials for examples of how to use each of these 4 methods to calculate the exciton coupling of your systems.
