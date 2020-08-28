'''
Created on Sep 23, 2017

@author: Ben Rose
'''

from Stoicheometry import *

C8 = Element('C',8,12.011)
H18 = Element('H',18,1.008)

Octane = C8 + H18

O2 = Element('O',2,15.999)

H2 = Element('H',2,1.008)
O1 = Element('O',1,15.999)
Water = H2 + O1

H8 = Element('H',8,1.008)
C4 = Element('C',4,12.011)
O2 = Element('O',2,15.999)

H12 = Element('H',12,1.008)
C6 = Element('C',6,12.011)

N1 = Element('N',1,14.007)
H3 = Element('H',3,1.008)
ammonia = (N1 + H3)

C1 = Element('C',1,12.011)
O2 = Element('O',2,15.999)
carbonDioxide = (C1+O2)

C1 = Element('C',1,12.011)
H4 = Element('H',4,1.008)
N2 = Element('N',2,14.007)
O1 = Element('O',1,15.999)
urea = (C1 + H4) + (N2 + O1)

H2 = Element('H',2,1.008)
O1 = Element('O',1,15.999)
water = H2 + O1

C6 = Element('C',6,12.011)
H12 = Element('H',12,1.008)
O6 = Element('O',6,15.999)
glucose = C6 + (H12 + O6)

K1 = Element('K',1,39.098)
Br1 = Element('Br',1,79.904)
H1 = Element('H',1,1.008)
Mg1 = Element('Mg',1,24.305)
Cl2 = Element('Cl',2,35.45)

Ca1 = Element('Ca',1,40.078)
hydroxide = O1 + H1
calciumOxide = Ca1 + O1
Na1 = Element('Na',1,22.99)
Na3 = Element('Na',3,22.99)
Br2 = Element('Br',2,79.904)
O3 = Element('O',3,15.999)

P1 = Element('P',1,30.974)
O4 = Element('O',4,15.999)
Cu1 = Element('Cu',1,63.546)
Cl1 = Element('Cl',1,35.45)
salt = Na1 + Cl1

I1 = Element('I',1,126.9)
print((H1+Cl1)*.8/0.0174)
