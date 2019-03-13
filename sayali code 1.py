import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage.filters import convolve
from scipy.signal import convolve2d
from scipy import misc
img = misc.ascent()
# shape of the image is accessed and it returns a tuple of no of rows and columns
plt.imshow(img, cmap='gray')
# 3-D array
h_kernel = np.array([[1, 2, 1],[0, 0, 0],[-1, -2, -1]])
plt.imshow(h_kernel)
# convolution is performed
s=convolve2d(img, h_kernel)

# plot grayscale image
plt.imshow(s, cmap='gray')
plt.show()