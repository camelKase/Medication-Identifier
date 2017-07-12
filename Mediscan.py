import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import pytesseract

def medscan():
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\camelkase\\Documents\\program\\Tesseract-OCR\\tesseract'
    print("=====output======")
    imprint = print(pytesseract.image_to_string(Image.open('pill.png')))

#thresholding
x = input('Enter image file name (include file extension): ')
image = cv2.imread(x)
first_value, image = cv2.threshold(image,105,255, cv2.THRESH_BINARY) #two inputs
#grayscale
plt.imshow(image,'gray')
plt.xticks([]),plt.yticks([])
#save new image after threshold:
width, height = 300,300
img= Image.fromarray(image,'RGB')
img.save('pill.png')

def database():
    imprint = str(pytesseract.image_to_string(Image.open('pill.png')))
    Medication = {"A 510" : "Generic-Divalproex, Brand-Depakote, Strength: 250 mg, *Seizure medication", 
    "227" : "Generic-Metformin, Brand-Glucophage, Strength 500mg, *Diabetes medication", 
    "103" : "Generic-Gabapentin, Brand-Neurotin, Strength 100mg, *Nerve pain",
    "R33" : "Genreric-Pantoprazole, Brand-Protonix, Strength 40mg, *Antacid",
    "CPC 835" : "Generic-Banophen, Brand-Benadryl, Strength 25mg, *Antihistamine",
    }
    for key in Medication:
        if key == imprint:
            print(Medication[imprint])
            break
        else:
            print("Not found")
            break
medscan()
database()
