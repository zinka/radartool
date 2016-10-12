#! /usr/bin/env python

# Author: Srinivasa Rao Zinka (srinivas . zinka [at] gmail . com)
# Copyright (c) 2016 Srinivasa Rao Zinka
# License: New BSD License.

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mayavi import mlab

def N_scan():
	""" Function doc """
	return	
	
def N_track():
	""" Function doc """
	return

def SNR():
	""" Function doc """
	
	return
	
def SNR_CW():
	""" Function doc """
	SNR(Pt=P_avg, Nl=Tdwell, B=1)
	return
	
def Rmax ():
	""" Function doc """
	return
	
def ambig():
	""" Function doc """
	return
	
if __name__ == '__main__':
	
	Pt = 40  # Peak transmit power in Watt
	Nl = 10 # No. of pulses in one dwell
	Gt = 30 # Gain of TX antenna in dB
	Gr = 30 # Gain of RX antenna in dB
	freq = 10e9 # Frequency of operation in Hz
	lam = 3e8/freq # Wavelength in m
	sig = 0.1 # RCS in m^2
	CR = 10 # Compression ratio / gain
	R = 10e3 # Range in m
	k = 1.38e-23 # Boltzman's constant
	B = 10e6 # Bandwidth in Hz
	Ta = 290 # Antenna temperature in Kelvin
	F = 3 # Noise figure of the reciver in dB
	LA = 0 # Atmospheric losses in dB
	LGP = 0 # Ground plane losses in dB
	LS = 0 # System losses in dB
	LI = 0 # Integration losses in dB
	Lmisc = 0 # Any other miscellenous losses in dB
	
	
	
	SNR()
	
# Ambiguity fun using quad and inf boundaries for various waveforms

# TODO PD, Pfa,  ... for various types of echos and Swerling models

# TODO Blake chart


