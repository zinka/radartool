#! /usr/bin/env python

# Author: Srinivasa Rao Zinka (srinivas . zinka [at] gmail . com)
# Copyright (c) 2016 Srinivasa Rao Zinka
# License: New BSD License.

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mayavi import mlab

def SNR(Pt, Nl, Gt, Gr, lam, sig, CR, R, B, F, LS=1, LI=1, LA=1, LGP=1, Lmisc=1, Ta=290):
	""" Function to calculate SNR using Radar Range Equation """
	
	k = 1.38e-23 # Boltzmann's constant
	TS = Ta + (F-1)*290
	SNR = (Pt*Nl*Gt*Gr*lam**2*sig*CR) / (64*np.pi**3*R**4*k*TS*B*LA*LGP*LS*LI*Lmisc)

	return SNR
	
def SNR_Pavg(Pt, dt, Tint, Gt, Gr, lam, sig, R, F, LS=1, LI=1, LA=1, LGP=1, Lmisc=1, Ta=290):
	""" Function to calculate SNR using Radar Range Equation """
	
	k = 1.38e-23 # Boltzmann's constant
	TS = Ta + (F-1)*290
	SNR = (Pt*dt*Tint*Gt*Gr*lam**2*sig) / (64*np.pi**3*R**4*k*TS*LA*LGP*LS*LI*Lmisc)

	return SNR	
	
def Rmax (Pt, Nl, Gt, Gr, lam, sig, CR, SNR, B, F, LS=1, LI=1, LA=1, LGP=1, Lmisc=1, Ta=290):
	""" Function doc """
	
	k = 1.38e-23 # Boltzmann's constant
	TS = Ta + (F-1)*290
	Rmax = ((Pt*Nl*Gt*Gr*lam**2*sig*CR) / (64*np.pi**3*SNR*k*TS*B*LA*LGP*LS*LI*Lmisc))**0.25
		
	return Rmax
	
def ambig():
	""" Function doc """
	return
	
if __name__ == '__main__':
	
	print 'nothing'
