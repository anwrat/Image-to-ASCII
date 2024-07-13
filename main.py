import cv2
import numpy as np

image_path="coc.jpg"
#Reading image file from path
image=cv2.imread(image_path)
#resizing the image, we use interpolation INTER_AREA to shrink the image
image=cv2.resize(image,(100,100),interpolation=cv2.INTER_AREA)
#print(image)#this gives a 3 dimensional value which represents rgb values of a pixel
#print(image.shape)#the structure, dimensions of the image
#Creating an empty array 
brightness=np.empty((image.shape[0],image.shape[1]))
ascii_image=[]
#Calculating brightness values by taking average of rgb of a pixel
for x in range(len(image)):
    for y in range(len(image[x])):
        pixel=image[x][y]
        avg=(int(pixel[0])+int(pixel[1])+int(pixel[2]))//3#(R+G+B)/3
        brightness[x][y]=avg
#print("The brightness values of all pixels in the image are: ")
#print(brightness)
#print(brightness.shape)


#Brightness to ASCII Values
ascii_vals = [' ', '`','^','"',',',':',';','I','l','!','i','~','+','_','-','?',']',
        '[','}','{','1',')','(','|','/','t','f','j','r','x','n','u','v','c','z',
        'X','Y','U','J','C','L','Q','0','O','Z','m','w','q','p','d','b','k','h',
        'a','o','*','#','M','W','&','8','%','B','@','$'] #Arranged in lightest to darkest order

ascii_vals_brightness={}#Empty dictionary
val=0
increment=255//len(ascii_vals) #Dividing the maximum brightness by the number of ASCII characters

#Using a for loop to assign key,value for each ASCII character
for x in ascii_vals:
    #Here x represents the character and x is the key while (val,val+increment) is the value of the dict
    ascii_vals_brightness[(val,val+increment)]=x 
    val+=increment+1

#for key,val in ascii_vals_brightness.items():
#    print(f'{val}:{key}') #Printing to understand the range of brightness for each ASCII character

# assigning values
for x in range(len(brightness)): #Looping through each row
    temp = [] #Temporary list that will be empty in each iteration
    for y in range(len(brightness[x])): #Looping through each brightness value for pixel
        val = brightness[x][y] #Assigning the brightness value to a variable
        for low, high in ascii_vals_brightness.keys(): # Looping over the keys of dictionary
            if val >= low and val <= high: #If brightness value is between low and high, the ASCII character will be used
                temp.append(ascii_vals_brightness[(low, high)]) #Appending the ASCII character to temp list
                break
    ascii_image.append(temp) #Appending to the main ascii_image list

#Printing it out!
for row in ascii_image:
    line = [x+x+x for x in row] #Printing three characters to avoid having big spaces in image
    print("".join(line))

