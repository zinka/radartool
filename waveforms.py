#! /usr/bin/env python

# Author: Srinivasa Rao Zinka (srinivas . zinka [at] gmail . com)
# Copyright (c) 2016 Srinivasa Rao Zinka
# License: New BSD License.

from __future__ import division
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
from mayavi import mlab

def rect(t, T=1):
    """create a centered rectangular pulse of width $T"""
    return (t>=-T/2) & (t <= T/2), 0
    
def rect_xi(t, T=1):
    """create a centered rectangular pulse of width $T"""
    return (t>=-T/2) & (t <= T/2), 0    
    
def Gaussian(t, sig=1):
    """ Function doc """
    return np.exp(-0.5*t**2/sig**2), 0  
    
def Gaussian_xi(t, sig=1):
    """ Function doc """
    return np.exp(-0.5*t**2/sig**2), 0       
    
def LFM(t, mu=1, T=1):
    """ Function doc """
    return rect(t,T)[0]*np.cos(mu*t**2*0.5), rect(t,T)[0]*np.sin(mu*t**2*0.5)
    
def LFM_xi(t, mu=1, T=1):
    """ Function doc """
    return rect(t,T)[0]*np.cos(mu*t**2*0.5), rect(t,T)[0]*np.sin(mu*t**2*0.5)
    
if __name__ == '__main__':
        
    te = 1.5 # Expanded pulse width ... not required for Gaussian pulse
    
    wd = np.linspace(-20, 20, 100) # Doppler angular shift
    tau = 0 # Delay in time with respect to t0
    [tau,wd] = np.mgrid[0:0:1j, -20:20:100j]
    
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
            
    mlab.mesh(tau, wd, abs(ambig))
    mlab.show()


    
    
