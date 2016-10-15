#! /usr/bin/env python

# Author: Srinivasa Rao Zinka (srinivas . zinka [at] gmail . com)
# Copyright (c) 2016 Srinivasa Rao Zinka
# License: New BSD License.

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mayavi import mlab
import waveforms as wf
from scipy import integrate

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
	
def Rmax_Pavg():
	""" Function doc """
	return
	
def ambig_gen(tau, wd, pulse_shape='rect', no_of_pulses=1, plot_type='3D'):
	""" This is function is damn slow ... so, never use this for ambiguity plots unless really required """
	
	# te = 1.5 # Expanded pulse width ... not required for Gaussian pulse
	# [tau,wd] = np.mgrid[0:0:1j, -20:20:100j]
    g1r = 'Gaussian(eta, te)[0]'
    g2r = 'Gaussian(eta+tau[i,j]], te)[0]' 
    g1i = 'Gaussian(eta, te)[1]'
    g2i = 'Gaussian(eta+tau[i,j], te)[1]'    
    
    g1r = 'rect(eta, te)[0]'
    g2r = 'rect(eta+tau[i,j], te)[0]' 
    g1i = 'rect(eta, te)[1]'
    g2i = 'rect(eta+tau[i,j], te)[1]'     
    
    mu = 1
    g1r = 'LFM(eta, mu, te)[0]'
    g2r = 'LFM(eta+tau[i,j], mu, te)[0]' 
    g1i = 'LFM(eta, mu, te)[1]'
    g2i = 'LFM(eta+tau[i,j], mu, te)[1]'     
        
    ambig = np.zeros(wd.shape, dtype='complex')
        
    for i in range(wd.shape[0]):
        
        for j in range(wd.shape[1]):
        
            gg_real = lambda eta: (eval(g1r)*eval(g2r)+eval(g1i)*eval(g2i))*np.cos(wd[i,j]*eta)- (eval(g1r)*eval(g2i)-eval(g1i)*eval(g2r))*np.sin(wd[i,j]*eta)        
            tmp_real = integrate.quad(gg_real, -np.inf, np.inf)[0]
            
            gg_imag = lambda eta: (eval(g1r)*eval(g2r)+eval(g1i)*eval(g2i))*np.sin(wd[i,j]*eta)+ (eval(g1r)*eval(g2i)-eval(g1i)*eval(g2r))*np.cos(wd[i,j]*eta)        
            tmp_imag = integrate.quad(gg_imag, -np.inf, np.inf)[0]
            
            ambig[i, j] = tmp_real+1j*tmp_imag	
		
	return	
	
def ambig_gen_tau(tau, wd, pulse_shape='rect', no_of_pulses=1, plot_type='3D'):
	""" Function doc """	
	return
	
def ambig_gen_wd(tau, wd, pulse_shape='rect', no_of_pulses=1, plot_type='3D'):
""" Function doc """	
return

def ambig(tau, wd, pulse_shape='rect', no_of_pulses=1, plot_type='3D'):
	""" Function doc """	
	return
	
if __name__ == '__main__':
	
	print 'nothing'
