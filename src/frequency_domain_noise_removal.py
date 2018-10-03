import cv2
import numpy as np

def lowpass_filter(img):
  img = cv2.imread(img, 0)
  dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
  # Shift the zero-frequency component to the center of the spectrum.
  dft_shift = np.fft.fftshift(dft)
  row = img.shape[0]
  col = img.shape[1]
  mid_row = row/2
  mid_col = col/2

  mask = np.zeros((row, col, 2),np.uint8)
  cutoff = 50
  mask[mid_row-cutoff:mid_row+cutoff, mid_col-cutoff:mid_col+cutoff] = 1
  
  fshift = dft_shift*mask
  f_ishift = np.fft.ifftshift(fshift)
  #inverse transform
  new_img = cv2.idft(f_ishift)
  new_img = cv2.magnitude(new_img[:,:,0],new_img[:,:,1])
  return new_img