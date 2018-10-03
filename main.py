import os
import cv2
import src.spatial_domain_noise_removal as sdnr 
import src.spatial_domain_edge_detection as sded
import src.frequency_domain_noise_removal as fdnr 
import src.frequency_domain_edge_detection as fded

from matplotlib import pyplot as plt

base_path = os.getcwd()

img = os.path.join(base_path, 'bruce.jpg')

# print img

#spatial domain
gaussian_blur = sdnr.gaussian_blur(img)
sobel_edge = sded.sobel_edge(img)

#frequency domain
frequency_smooth = fdnr.lowpass_filter(img)
frequency_edge = fded.highpass_filter(img)

image = cv2.imread(img, 0)

plt.subplot(231),plt.imshow(image, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(232),plt.imshow(gaussian_blur, cmap='gray')
plt.title('Gaussian Smoothing'), plt.xticks([]), plt.yticks([])

plt.subplot(233),plt.imshow(sobel_edge, cmap='gray')
plt.title('Sobel Edge Detection'), plt.xticks([]), plt.yticks([])

plt.subplot(234),plt.imshow(frequency_smooth, cmap='gray')
plt.title('Freq. Domain Smoothing'), plt.xticks([]), plt.yticks([])

plt.subplot(235),plt.imshow(frequency_edge, cmap='gray')
plt.title('Freq. Domain Edge Detection'), plt.xticks([]), plt.yticks([])


plt.show()
