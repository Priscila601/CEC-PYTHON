# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 12:31:14 2019

@author: CEC
"""

import numpy as np
import matplotlib.pyplot as plt

plt.ioff()
for i in range(3):
    plt.plot(np.random.rand(10))
    plt.show()