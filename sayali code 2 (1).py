# imports
import numpy as np
import matplotlib.pyplot as plt
# 1-D array
a = np.array([0, 0, 0, 0 ,0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],dtype='float32')
b = np.array([-1,1], dtype='float32')
# convolution is performed between a ,b 1-D arrays
c = np.convolve(a,b)

# plot of a
plt.subplot(211)
plt.plot(a, 'o-')
plt.show()

# plot of b
plt.subplot(212)
plt.plot(b, 'o-')
plt.show()

# plot of c
plt.subplot(212)
plt.plot(c, 'o-')
plt.show()
