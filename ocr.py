import easyocr
import torch

reader = easyocr.Reader(['en']) # need to run only once to load model into memory

text = reader.readtext('IDCard.jpg')

print(text)