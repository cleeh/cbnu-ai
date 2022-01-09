import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('Identification_Photo_Edit.jpg')

plt.imshow(img)
plt.show()