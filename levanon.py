#! /usr/bin/env python

# Author: Srinivasa Rao Zinka (srinivas . zinka [at] gmail . com)
# Copyright (c) 2015 Srinivasa Rao Zinka
# License: New BSD License.

from __future__ import division
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from mayavi import mlab

# adjusting "matplotlib" label fonts
from matplotlib import rc
rc('text', usetex=True)

w = 2*np.pi*150 # carrier freq = 150 Hz
wc = 2*np.pi*15 # square wave freq = 15 Hz
x = np.linspace(0, 1,2001) # Samplinf freq = 2 KHz

wd = 0.05*wc
s = (np.cos((w+wd)*x))*0.5*(signal.square(wc*x)+1)

plt.plot(x, s)

y = s*np.cos(w*x)

plt.xlabel('Angle [rad]')
plt.ylabel('s(t)')
plt.axis('tight')
plt.show()
#plt.plot(x, y)
#plt.show()

b, a = signal.butter(8,0.08, 'low')
w, h = signal.freqz(b, a)

fig = plt.figure()
plt.title('Digital filter frequency response')
ax1 = fig.add_subplot(111)


plt.plot(w*2e3/(2*np.pi), 20 * np.log10(abs(h)), 'b')
plt.ylabel('Amplitude [dB]', color='b')
plt.xlabel('Frequency [rad/sample]')


#ax2 = ax1.twinx()
#angles = np.unwrap(np.angle(h))
#plt.plot(w*2e3/(2*np.pi), angles, 'g')
#plt.ylabel('Angle (radians)', color='g')

plt.grid()
plt.axis('tight')
plt.show()


#filtered = signal.convolve(sig, win, mode='same')
output_signal = signal.filtfilt(b, a, y)

plt.plot(x, output_signal)
plt.show()
