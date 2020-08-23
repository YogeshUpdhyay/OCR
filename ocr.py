import easyocr
import torch
import cv2
import PIL as pil
import matplotlib.pyplot as plt

#reader = easyocr.Reader(['en']) # need to run only once to load model into memory

#text = reader.readtext('Challan.jpeg',detail=0)

#print(text)

im = plt.imread('Challan.jpeg')

plt.imshow(im)
plt.show()