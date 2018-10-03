import os
from scipy import signal
import numpy as np
from math import *
import cv2

# def get_image(filename):
#   img = cv2.imread(filename, 0)
#   cv2.imwrite('sdnr.jpg', img)

def convolution(img, kernel):
  img = cv2.imread(img, 0)
  row=img.shape[0]
  col=img.shape[1]
  kernel_row=kernel.shape[0]
  kernel_col=kernel.shape[1]

  nimg = np.zeros((row,col),np.float32)
  nkernel = np.zeros((kernel_row, kernel_col), np.float32)
  return signal.convolve2d(img, kernel)

def gaussian_blur(img):
  n=5
  sigma=float(n)/5
  kernel=np.zeros((n,n),np.float32)
  mid=n/2
  for i in range(-mid,mid+1):
    for j in range(-mid,mid+1):
      kernel[i][j]=exp(-(i*i+j*j)/(2*sigma*sigma))

  return convolution(img, kernel)


