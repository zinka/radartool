#! /usr/bin/env python

# Author: Srinivasa Rao Zinka (srinivas . zinka [at] gmail . com)
# Copyright (c) 2016 Srinivasa Rao Zinka
# License: New BSD License.

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mayavi import mlab
from radartool import SNR, SNR_Pavg, Rmax

# ========================================================================================
# Fig. 1.18 and 1.19 in Radar Systems Analysis and Design Using Matlab (2nd ed) by Mahafza
# ========================================================================================

Pt = 1.5e6  # Peak transmit power in Watt
Nl = 1 # No. of pulses in one dwell
Gt = 45 # Gain of TX antenna in dB
Gr = 45 # Gain of RX antenna in dB

freq = 5.6e9 # Frequency of operation in Hz
lam = 3e8/freq # Wavelength in m

sig = 1 # RCS in m^2
CR = 1 # Compression ratio / gain
R = 40e3 # Range in m
B = 5e6 # Bandwidth in Hz
F = 3 # Noise figure of the receiver in dB

LS = 6 # System losses in dB
LI = 0 # Integration losses in dB
LA = 0 # Atmospheric losses in dB
LGP = 0 # Ground plane losses in dB
Lmisc = 0 # Any other miscellaneous losses in dB

Ta = 290 # Antenna temperature in Kelvin

lst_tmp = np.array([Gt, Gr, F, LS, LI, LA, LGP, Lmisc])
[Gt, Gr, F, LS, LI, LA, LGP, Lmisc] = 10**(lst_tmp/10) # Converting dB values to linear

# Figure 1.18a, p.27 , Radar Systems Analysis and Design Using Matlab (2nd ed) by Mahafza
R = np.linspace(20e3, 180e3, 100, endpoint=True)
SNR1 = SNR(Pt, Nl, Gt, Gr, lam, 1, CR, R, B, F, LS, LI, LA, LGP, Lmisc, Ta)
SNR2 = SNR(Pt, Nl, Gt, Gr, lam, 0.1, CR, R, B, F, LS, LI, LA, LGP, Lmisc, Ta)
SNR3 = SNR(Pt, Nl, Gt, Gr, lam, 0.01, CR, R, B, F, LS, LI, LA, LGP, Lmisc, Ta)
plt.figure(1)
plt.plot(R/1e3, 10*np.log10(SNR1), R/1e3, 10*np.log10(SNR2),R/1e3, 10*np.log10(SNR3))
plt.xlabel('Detection range - Km'); plt.ylabel('SNR - dB'); plt.grid(True); plt.show()

# Figure 1.18b, p.27 , Radar Systems Analysis and Design Using Matlab (2nd ed) by Mahafza
R = np.linspace(20e3, 180e3, 100, endpoint=True)
SNR1 = SNR(2.16e6, Nl, Gt, Gr, lam, .1, CR, R, B, F, LS, LI, LA, LGP, Lmisc, Ta)
SNR2 = SNR(1.5e6, Nl, Gt, Gr, lam, .1, CR, R, B, F, LS, LI, LA, LGP, Lmisc, Ta)
SNR3 = SNR(0.6e6, Nl, Gt, Gr, lam, .1, CR, R, B, F, LS, LI, LA, LGP, Lmisc, Ta)
plt.figure(2)
plt.plot(R/1e3, 10*np.log10(SNR1), R/1e3, 10*np.log10(SNR2),R/1e3, 10*np.log10(SNR3))
plt.xlabel('Detection range - Km'); plt.ylabel('SNR - dB'); plt.grid(True); plt.show()  

# Figure 1.19a, p.29 , Radar Systems Analysis and Design Using Matlab (2nd ed) by Mahafza
R = np.linspace(10e3, 250e3, 100, endpoint=True)
SNR1 = SNR(Pt, 10, Gt, Gr, lam, .1, CR, R, B, F, LS, LI, LA, LGP, Lmisc, Ta)
SNR2 = SNR(Pt, 5, Gt, Gr, lam, .1, CR, R, B, F, LS, LI, LA, LGP, Lmisc, Ta)
SNR3 = SNR(Pt, 1, Gt, Gr, lam, .1, CR, R, B, F, LS, LI, LA, LGP, Lmisc, Ta)
plt.figure(3)
plt.plot(R/1e3, 10*np.log10(SNR1), R/1e3, 10*np.log10(SNR2),R/1e3, 10*np.log10(SNR3))
plt.xlabel('Detection range - Km'); plt.ylabel('SNR - dB'); plt.grid(True); plt.show()

# Figure 1.19b, p.30 , Radar Systems Analysis and Design Using Matlab (2nd ed) by Mahafza
Nl = np.linspace(0, 500, 100, endpoint=True)
SNR1 = SNR(Pt, Nl, Gt, Gr, lam, 1, CR, 150e3, B, F, LS, LI, LA, LGP, Lmisc, Ta)
SNR2 = SNR(Pt, Nl, Gt, Gr, lam, .1, CR, 150e3, B, F, LS, LI, LA, LGP, Lmisc, Ta)
plt.figure(4)
plt.plot(Nl, 10*np.log10(SNR1), Nl, 10*np.log10(SNR2))
plt.xlabel('No. of pulses');    plt.ylabel('SNR - dB'); plt.grid(True); plt.show()  

# ========================================================================================
# Fig. 1.20, p.32, in Radar Systems Analysis and Design Using Matlab (2nd ed) by Mahafza
# ========================================================================================

Pt = 10e3  # Peak transmit power in Watt
dt = 0.3 # Transmit duty cycle

Tint = 2 # Integration time (coherent/non-coherent)

Gt = 20 # Gain of TX antenna in dB
Gr = 20 # Gain of RX antenna in dB

freq = 5.6e9 # Frequency of operation in Hz
lam = 3e8/freq # Wavelength in m

sig = 0.01 # RCS in m^2
R = 50e3 # Range in m
F = 5 # Noise figure of the receiver in dB

LS = 8 # System losses in dB
LI = 0 # Integration losses in dB
LA = 0 # Atmospheric losses in dB
LGP = 0 # Ground plane losses in dB
Lmisc = 0 # Any other miscellaneous losses in dB

Ta = 290 # Antenna temperature in Kelvin

lst_tmp = np.array([Gt, Gr, F, LS, LI, LA, LGP, Lmisc])
[Gt, Gr, F, LS, LI, LA, LGP, Lmisc] = 10**(lst_tmp/10) # Converting dB values to linear 

# Figure 1.20, p.32, Radar Systems Analysis and Design Using Matlab (2nd ed) by Mahafza
R = np.linspace(10e3, 225e3, 1000, endpoint=True)
SNR1 = SNR_Pavg(Pt, 0.05, Tint, Gt, Gr, lam, sig, R, F, LS, LI, LA, LGP, Lmisc, Ta)
SNR2 = SNR_Pavg(Pt, 0.1, Tint, Gt, Gr, lam, sig, R, F, LS, LI, LA, LGP, Lmisc, Ta)
SNR3 = SNR_Pavg(Pt, 0.2, Tint, Gt, Gr, lam, sig, R, F, LS, LI, LA, LGP, Lmisc, Ta)
plt.figure('SNR_Pavg')
plt.plot(R/1e3, 10*np.log10(SNR1), R/1e3, 10*np.log10(SNR2),R/1e3, 10*np.log10(SNR3))
plt.xlabel('Detection range - Km'); plt.ylabel('SNR - dB'); plt.grid(True); plt.axis([0, 250, -30, 40]); plt.show()

# Example, p.32, Radar Systems Analysis and Design Using Matlab (2nd ed) by Mahafza
Pt = 100e3; dt = 0.3; R = 50e3
tmp = SNR_Pavg(Pt, dt, Tint, Gt, Gr, lam, sig, R, F, LS, LI, LA, LGP, Lmisc, Ta)
print 10*np.log10(tmp)

# ========================================================================================
# Example, p.24, in Radar Systems Analysis and Design Using Matlab (2nd ed) by Mahafza
# ========================================================================================

Pt = 1.5e6  # Peak transmit power in Watt
Nl = 1 # No. of pulses in one dwell
Gt = 45 # Gain of TX antenna in dB
Gr = 45 # Gain of RX antenna in dB

freq = 5.6e9 # Frequency of operation in Hz
lam = 3e8/freq # Wavelength in m

sig = 0.1 # RCS in m^2
CR = 1 # Compression ratio / gain
SNR = 20 # SNR in dB
B = 5e6 # Bandwidth in Hz
F = 3 # Noise figure of the receiver in dB

LS = 0 # System losses in dB
LI = 0 # Integration losses in dB
LA = 0 # Atmospheric losses in dB
LGP = 0 # Ground plane losses in dB
Lmisc = 0 # Any other miscellaneous losses in dB

Ta = 290 # Antenna temperature in Kelvin

lst_tmp = np.array([Gt, Gr, SNR, F, LS, LI, LA, LGP, Lmisc])
[Gt, Gr, SNR, F, LS, LI, LA, LGP, Lmisc] = 10**(lst_tmp/10) # Converting dB values to linear
    
print Rmax (Pt, Nl, Gt, Gr, lam, sig, CR, SNR, B, F, LS, LI, LA, LGP, Lmisc, Ta)
    

# Ambiguity fun using quad and inf boundaries for various waveforms

# TODO PD, Pfa,  ... for various types of echos and Swerling models

# TODO Blake chart 1
