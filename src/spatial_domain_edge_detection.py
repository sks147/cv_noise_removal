import numpy as np
import cv2
from scipy import signal

def convolution(img, kernel):
  img = cv2.imread(img, 0)
  row=img.shape[0]
  col=img.shape[1]
  kernel_row=kernel.shape[0]
  kernel_col=kernel.shape[1]

  nimg = np.zeros((row,col),np.float32)
  nkernel = np.zeros((kernel_row, kernel_col), np.float32)
  return signal.convolve2d(img, kernel)


def sobel_edge(img):
  x=np.zeros((3,3),np.float32)
  y=np.zeros((3,3),np.float32)
  x[0]=[2,0,-2]
  x[1]=[3,0,-3]
  x[2]=[2,0,-2]
  y[0]=[2,3,2]
  y[1]=[0,0,0]
  y[2]=[-2,-3,-2]
  Gx = convolution(img,x)
  Gy = convolution(img,y)
  G = np.power(np.add(np.multiply(Gx,Gx), np.multiply(Gy,Gy)), 0.5)
  return G