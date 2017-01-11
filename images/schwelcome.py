# -*- coding: utf-8 -*-
'''
JDoe_JSmith_1_4_3: Change pixels in an image.
'''
import matplotlib.pyplot as plt
import os.path
import numpy as np # “as” lets us use standard abbreviations
import PIL


def mask(original_image):
    width, height = original_image.size
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__))
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'MonaLisa.png')
filename1 = os.path.join(directory, 'MonaLisa2.png')
# Read the image data into an array
img = PIL.Image.open(filename)
img2= PIL.Image.open(filename1)
img2_convert = img2.convert("RGBA")
img2 = np.array(img2_convert)

height = len(img2)
width = len(img2[0])
for r in range(height):
    for c in range(width):
        if img2[r][c][3] > 150:
            img2[r][c][3] = 150

img_convert = img.convert("RGBA")
img = np.array(img_convert)


height = len(img)
width = len(img[0])
for r in range(0,146):#height
    for c in range(0,687):#width
        img2[r][c]=[255,0,0,255] # Red


#height = len(img)
#width = len(img[0])
for r in range(146,292):#height
    for c in range(0,687):#width
        img2[r][c]=[255,165,0,255] # orange
#height = len(img)
#width = len(img[0])
for r in range(292,438):#height
    for c in range(0,687):#width
        img2[r][c]=[255,255,0,255] # yellow
#height = len(img)
#width = len(img[0])
for r in range(438,584):#height
    for c in range(0,687):#width
        img2[r][c]=[0,128,0,255] # green
#height = len(img)
#width = len(img[0])
for r in range(584,730):#height
    for c in range(0,687):#width
        img2[r][c]=[0,0,255,255] # blue
#height = len(img)
#width = len(img[0])
for r in range(730,876):#height
    for c in range(0,687):#width
        img2[r][c]=[75,0,130,255] # indigo
#height = len(img)
#width = len(img[0])
for r in range(876,1024):#height
    for c in range(0,687):#width
        img2[r][c]=[238,130,238,255] # violet
img3 = PIL.Image.fromarray(img)        
img4 = PIL.Image.fromarray(img2)        
        
img3.paste(img4,(1,1))
# Show the image data in a subplot
'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 2)
ax[0].imshow(img3, interpolation='none')
ax[1].imshow(img, interpolation='none')
# Show the figure on the screen
fig.show()
