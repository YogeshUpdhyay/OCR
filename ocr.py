import easyocr
import torch


reader = easyocr.Reader(['en']) # need to run only once to load model into memory

text = reader.readtext('Challan.jpeg',detail=0)

print(text)