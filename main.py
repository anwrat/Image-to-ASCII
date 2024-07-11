import cv2
import numpy as np

image_path="eiffel.png"
#Reading image file from path
image=cv2.imread(image_path)
#resizing the image, we use interpolation INTER_AREA to shrink the image
image=cv2.resize(image,(100,100),interpolation=cv2.INTER_AREA)
print(image)#this gives a 3 dimensional value which represents rgb values of a pixel
print(image.shape)#the structure, dimensions of the image
#Creating an empty array 
brightness=np.empty((image.shape[0],image.shape[1]))
ascii_image=[]
#Calculating brightness values by taking average of rgb of a pixel
for x in range(len(image)):
    for y in range(len(image[x])):
        pixel=image[x][y]
        avg=(int(pixel[0])+int(pixel[1])+int(pixel[2]))//3#(R+G+B)/3
        brightness[x][y]=avg
print("The brightness values of all pixels in the image are: ")
print(brightness)
print(brightness.shape)
