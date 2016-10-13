#! /usr/bin/env python

# Author: Srinivasa Rao Zinka (srinivas . zinka [at] gmail . com)
# Copyright (c) 2016 Srinivasa Rao Zinka
# License: New BSD License.

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

def rect(T):
    """create a centered rectangular pulse of width $T"""
    return lambda t: (t>=-T/2) & (t <= T/2)

def pulse_train(t, at, shape):
    """create a train of pulses over $t at times $at and shape $shape"""
    return np.sum(shape(t - at[:,np.newaxis]), axis=0)

t = np.linspace(-50, 50, 1000, endpoint=True)
sig = pulse_train(t, at=np.array([0, 20, 40]), shape=rect(10))

plt.plot(t, sig)
plt.grid(True)
plt.show()


    
    
