#! /usr/bin/env python
# Authors: Amandeep Gupta & Srinivasa Rao Zinka (srinivas . zinka [at] gmail . com)
# License: New BSD License.

from __future__ import division
import numpy as np
import scipy as sp
from scipy.sparse import spdiags
from pylab import *
from mayavi import mlab

tb = 1  # bit period (original sample period)

# Single pulse
m_basic = 12
u_basic = r_[[1] * int(m_basic)]

# # A pulse train
# u_basic = r_[[1]*int(m_basic), [0]*int(4*m_basic)]
# u_basic = r_[u_basic,u_basic,u_basic,u_basic,u_basic,u_basic]

m_basic = u_basic.size  # gives the total number of elements

f_basic = r_[[0] * m_basic]  # Frequency coding of the basic pulse
# f_basic = np.array([1,2,3,4,5,6]) # DELETE THIS LATER

F = 4  # Maximal Doppler shift in units of 1/Mtb
K = 101  # Number of Doppler grid points on each side
df = F / (K - 1) / (m_basic * tb)  # Doppler grid size in Hz

T = 1  # Maximal delay in units of Mtb
N = 101  # Number of delay grid points on each side
dtau = T * m_basic * tb / (N - 1)  # Delay grid size in sec

# ==============================================================================
# Over sampling
# ==============================================================================

sr = 10  # over-sampling ratio
r = int(ceil(sr * tb / dtau))

dt = tb / r  # sample period after oversampling
m = m_basic * r  # No. of samples after over sampling

ao = np.ones((m_basic, r))
ud = np.diag(u_basic)
u_new = np.dot(ud, ao).reshape(m,)  # u_new is the over-sampled version
uamp = np.absolute(u_new)
phas = np.angle(u_new)

fdiag = diag(f_basic)
f_new = np.dot(fdiag, ao).reshape(m,)  # f_new is the over-sampled version

phas = phas + 2 * pi * np.cumsum(f_new) * dt
uexp = exp(1j * phas)
u = uamp * uexp  # u is the final over-sampled version

# ==============================================================================
# Plotting the signal's amplitude and phase
# ==============================================================================

t = np.arange(0, tb * m_basic, dt)  # time after oversampling

plt.figure(1)
plt.subplot(211)
plt.plot(t, np.abs(uamp))
plt.ylabel(' Amplitude ')
plt.ylim([0, 1.2 * max(np.abs(uamp))])

plt.subplot(212)
plt.plot(t, phas)
plt.ylabel('Phase [rad]')

# dphas = r_[[np.nan], np.diff(phas)]*r/2/np.pi # CHECK LATER
# plt.subplot(313) # CHECK LATER
#plt.plot(t , dphas*ceil(max(t)) )
#plt.ylabel(' Amplitude ')
#plt.xlabel(' t_b ')
#plt.ylabel('  Mt_b ')

# plt.show()

# ==============================================================================
# Generating delay and doppler grids
# ==============================================================================

tau = np.round(np.arange(N) * dtau / dt) * dt  # Delay grid
f = np.arange(K) * df  # Doppler grid (one sided)
f = r_[-1 * f[:0:-1], f]  # '0' copied once

# ==============================================================================
# Creation of various matrices
# ==============================================================================

tau_max = int(tau.max() / dt)  # maximum index along the delay grid
ud = np.reshape(u, (1, -1))
mat1 = spdiags(np.conj(ud), 0, m + tau_max, m)

u_padded = r_[u, np.zeros(tau_max)]
u_padded = np.reshape(u_padded, (1, -1))

cidx = np.arange(m + tau_max)
ridx = np.round(tau / dt).reshape(-1, 1)
ridx = ridx.astype(int)

index = np.tile(cidx, (N, 1)) - np.tile(ridx, (1, m + tau_max))
mat2 = u_padded[0, index]

uu_pos = mat1.transpose().dot(mat2.T)
uu_pos = uu_pos.T

ft = np.dot(np.array(f, ndmin=2).T, np.array(t, ndmin=2))
e = np.exp(-2j * np.pi * ft)

a = np.dot(e, uu_pos.T)
a_pos = a / abs(a).max()
a_pos = abs(a_pos)

# ==============================================================================
# Plotting partial ambiguity function
# ==============================================================================

[tau, f] = np.meshgrid(tau, f)
norm1 = m_basic * tb
tau = tau / norm1
f = f * norm1  # Normalizing delay and Doppler axes
mlab.surf(f, tau, abs(a_pos), warp_scale='auto')
ranges1 = [f.min(), f.max(), tau.min(), tau.max(),
           abs(a_pos).min(), abs(a_pos).max()]
mlab.axes(xlabel='f', ylabel='tau', zlabel='ambig', ranges=ranges1)
mlab.show()

# ==============================================================================
# Plotting total ambiguity function
# ==============================================================================

tau = np.hstack((-np.fliplr(tau), tau))
print(tau.shape)
f = np.hstack((np.fliplr(f), f))

a_top = a_pos[0:K, :]
a_top = a_top[::-1, ::-1]
a_bot = a_pos[K:2 * K + 1, :]
a_bot = a_bot[::-1, ::-1]
tm = np.vstack((a_bot, a_top))
a_pos = np.hstack((tm, a_pos))

mlab.surf(f, tau, abs(a_pos), warp_scale='auto')
ranges1 = [f.min(), f.max(), tau.min(), tau.max(),
           abs(a_pos).min(), abs(a_pos).max()]
mlab.axes(xlabel='f', ylabel='tau', zlabel='ambig', ranges=ranges1)
mlab.show()

# mlab.surf(f, tau, abs(a_pos), warp_scale='auto')
# ranges1=[f.min(),f.max(),tau.min(),tau.max(),abs(a_pos).min(),abs(a_pos).max()]
# mlab.axes(xlabel='f', ylabel='tau',zlabel='ambig', ranges=ranges1)
# mlab.show()

# TODO Now, let's check this code by plotting figures given in Levanon
