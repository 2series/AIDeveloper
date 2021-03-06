import os, platform
import numpy as np
import PIL
import matplotlib.pyplot as plt
import tensorflow as tf
import keras
from keras.preprocessing.image import ImageDataGenerator,load_img
import imgaug
import time
import cv2
import aid_img

color_mode = "RGB"

#Load an image
path = os.path.join("imgaug","quokka.jpg")
img = load_img(path,color_mode=color_mode.lower()) #This uses PIL and supports many many formats!
img = np.array(img)
images = []
for i in range(250):
    images.append(img)
images = np.array((images), dtype="uint8")

print("""
##########################AFFINE AUGMENTATION##################################
""")
#Define some parameters
v_flip = True#bool, if random vertical flipping should be applied
h_flip = True#bool, if random horizontal flipping should be applied
rotation = 45#degrees of random rotation
width_shift = 0.2#shift the image left right
height_shift = 0.2#shift the image up down
zoom = 0.2#random zooming in range
shear = 0.2#random shear in range

#For imgaug, define a function that performs affine augmentations in sequence
def imgaug_affine(images,v_flip,h_flip,rotation,width_shift,height_shift,zoom,shear,backend):
    v_flip_imgaug = 0.5 if v_flip==True else 0.0
    h_flip_imgaug = 0.5 if h_flip==True else 0.0

    #Imgaug image augmentation pipeline for affine augmentation
    gen = imgaug.augmenters.Sequential([
            imgaug.augmenters.Fliplr(h_flip_imgaug), #flip 50% of the images horizontally
            imgaug.augmenters.Flipud(v_flip_imgaug), #flip 50% of the images vertically
            imgaug.augmenters.Affine(
                    rotate=(-rotation, rotation),
                    translate_percent={"x": (-width_shift, width_shift), "y": (-height_shift, height_shift)},
                    scale={"x": (1-zoom, 1+zoom), "y": (1-zoom, 1+zoom)},
                    shear=(-shear, shear),backend=backend)  ])
    return gen(images=images) #Imgaug image augmentation

#####Affine, Keras ImageDataGenerator
t1 = time.time()
gen = ImageDataGenerator(rotation_range=rotation,vertical_flip=v_flip,horizontal_flip=h_flip,width_shift_range=width_shift,height_shift_range=height_shift,zoom_range=zoom,shear_range=shear,dtype="unit8")
gen_keras = gen.flow(images, np.repeat(0,images.shape[0]), batch_size=images.shape[0])
images_keras = next(gen_keras)[0].astype(np.uint8)
t2 = time.time()
dt = t2-t1
print("Keras ImageDataGenerator "+str(np.round(dt,2))+"s")

fig=plt.figure(1)
for i in range(1,5):
    ax=fig.add_subplot(2,2,i)        
    ax.imshow(images_keras[i])
    ax.axis("off")
fig.suptitle("Keras ImageDataGenerator "+str(np.round(dt,2))+"s")
plt.savefig("02_Affine_Keras.png")
plt.close(1)

#####Affine, imgaug, skimage
t1 = time.time()
images_imgaug_sk = imgaug_affine(images,v_flip,h_flip,rotation,width_shift,height_shift,zoom,shear,backend="skimage")
t2 = time.time()
dt = t2-t1
print("imgaug (backend skimage) "+str(np.round(dt,2))+"s")

fig=plt.figure(1)
for i in range(1,5):
    ax=fig.add_subplot(2,2,i)        
    ax.imshow(images_imgaug_sk[i])
    ax.axis("off")
fig.suptitle("imgaug (backend skimage) "+str(np.round(dt,2))+"s")
plt.savefig("02_Affine_imgaug_sk.png")
plt.close(1)


#####Affine, imgaug, cv2
t1 = time.time()
images_imgaug_cv = imgaug_affine(images,v_flip,h_flip,rotation,width_shift,height_shift,zoom,shear,backend="cv2")
t2 = time.time()
dt = t2-t1
print("imgaug (backend cv2) "+str(np.round(dt,2))+"s")

fig=plt.figure(1)
for i in range(1,5):
    ax=fig.add_subplot(2,2,i)        
    ax.imshow(images_imgaug_cv[i])
    ax.axis("off")
fig.suptitle("imgaug (backend cv2) "+str(np.round(dt,2))+"s")
plt.savefig("02_Affine_imgaug_cv2.png")
plt.close(1)


#####Affine, AIDeveloper aid_img.py
t1 = time.time()
images_aid = aid_img.affine_augm(images,v_flip,h_flip,rotation,width_shift,height_shift,zoom,shear) #Affine image augmentation
t2 = time.time()
dt = t2-t1
print("AIDeveloper "+str(np.round(dt,2))+"s")

fig=plt.figure(1)
for i in range(1,5):
    ax=fig.add_subplot(2,2,i)        
    ax.imshow(images_aid[i])
    ax.axis("off")
fig.suptitle("AIDeveloper "+str(np.round(dt,2))+"s")
plt.savefig("02_Affine_aid_img.png")
plt.close(1)



print("""
#########################Brightness augmentation###############################
""")

add_lower = -50
add_upper = 50
mult_lower = 0.8
mult_upper = 1.2
gaussnoise_mean = 0
gaussnoise_scale = 15

def imgaug_brightness_noise(images,add_low,add_high,mult_low,mult_high,noise_mean,noise_std):
    seq = imgaug.augmenters.Sequential([
        imgaug.augmenters.Add((add_low, add_high)),
        imgaug.augmenters.Multiply((mult_low, mult_high)),
        imgaug.augmenters.AdditiveGaussianNoise(loc=noise_mean, scale=(noise_std, noise_std)),
    ])
    images = seq(images=images)
    return images


#####Brightness, Keras
t1 = time.time()
gen = ImageDataGenerator(brightness_range=(mult_lower,mult_upper),dtype="unit8")
gen_keras = gen.flow(images, np.repeat(0,images.shape[0]), batch_size=images.shape[0])
images_keras = next(gen_keras)[0].astype(np.uint8)
t2 = time.time()
dt = t2-t1
print("Keras ImageDataGenerator "+str(np.round(dt,2))+"s")

fig=plt.figure(1)
for i in range(1,5):
    ax=fig.add_subplot(2,2,i)        
    ax.imshow(images_keras[i])
    ax.axis("off")
fig.suptitle("Keras ImageDataGenerator "+str(np.round(dt,2))+"s")
plt.savefig("02_Brightness_Keras.png")
plt.close(1)


#####Brightness, imgaug
t1 = time.time()
images_imgaug = imgaug_brightness_noise(images,add_lower,add_upper,mult_lower,mult_upper,gaussnoise_mean,gaussnoise_scale)
#plt.imshow(img_aug_1[0,:,:,0],cmap='gray')
t2 = time.time()
dt = t2-t1
print("imgaug "+str(np.round(dt,2))+"s")

fig=plt.figure(1)
for i in range(1,5):
    ax=fig.add_subplot(2,2,i)        
    ax.imshow(images_imgaug[i])
    ax.axis("off")
fig.suptitle("imgaug "+str(np.round(dt,2))+"s")
plt.savefig("02_Brightness_imgaug.png")
plt.close(1)


#####Brightness; AIDevelopers aid_img
t1 = time.time()
images_aid = aid_img.brightn_noise_augm_cv2(images,add_lower,add_upper,mult_lower,mult_upper,gaussnoise_mean,gaussnoise_scale)
#plt.imshow(img_aug_1[0,:,:,0],cmap='gray')
t2 = time.time()
dt = t2-t1
print("AIDeveloper "+str(np.round(dt,2))+"s")

fig=plt.figure(1)
for i in range(1,5):
    ax=fig.add_subplot(2,2,i)        
    ax.imshow(images_aid[i])
    ax.axis("off")
fig.suptitle("AIDeveloper "+str(np.round(dt,2))+"s")
plt.savefig("02_Brightness_aid_img.png")
plt.close(1)



print("""
#########################Gaussian blur###############################
""")

#Define Parameters
sigma_low = 0
sigma_high = 20

def imgaug_gaussnoise(images,sigma_high):
    seq = imgaug.augmenters.Sequential([
        imgaug.augmenters.blur.GaussianBlur(sigma=(sigma_low, sigma_high))
        ])
    images = seq(images=images)
    return images


#####Gaussian blur, imgaug
t1 = time.time()
images_imgaug = imgaug_gaussnoise(images,sigma_high)
t2 = time.time()
dt = t2-t1
print("imgaug "+str(np.round(dt,2))+"s")

fig=plt.figure(1)
for i in range(1,5):
    ax=fig.add_subplot(2,2,i)        
    ax.imshow(images_imgaug[i])
    ax.axis("off")
fig.suptitle("imgaug "+str(np.round(dt,2))+"s")
plt.savefig("03_Gaussblur_imgaug.png")
plt.close(1)


#####Gaussian blur; AIDevelopers aid_img
t1 = time.time()
images_aid = aid_img.gauss_blur_cv(images,sigma_low,sigma_high)
t2 = time.time()
dt = t2-t1
print("AIDeveloper "+str(np.round(dt,2))+"s")

fig=plt.figure(1)
for i in range(1,5):
    ax=fig.add_subplot(2,2,i)        
    ax.imshow(images_aid[i])
    ax.axis("off")
fig.suptitle("AIDeveloper "+str(np.round(dt,2))+"s")
plt.savefig("03_Gaussblur_aid_img.png")
plt.close(1)



print("""
#########################Saturation/Hue augmentation###############################
""")

#Define Parameters
hue_on = True
hue_low = 0.7
hue_high = 1.3
saturation_on = True
sat_low = 0.5
sat_high = 1.5

def imgaug_contrast(images,sigma_high):
    seq = imgaug.augmenters.Sequential([
        imgaug.augmenters.MultiplyHueAndSaturation(mul_saturation=(sat_low, sat_high),mul_hue=(hue_low, hue_high))
        ])
    images = seq(images=images)
    return images

#####Saturation/Hue augmentation, imgaug
t1 = time.time()
images_imgaug = imgaug_contrast(images,sigma_high)
t2 = time.time()
dt = t2-t1
print("imgaug "+str(np.round(dt,2))+"s")

fig=plt.figure(1)
for i in range(1,5):
    ax=fig.add_subplot(2,2,i)        
    ax.imshow(images_imgaug[i])
    ax.axis("off")
fig.suptitle("imgaug "+str(np.round(dt,2))+"s")
plt.savefig("04_Sat_Hue_imgaug.png")
plt.close(1)


#####Saturation/Hue augmentation; AIDevelopers aid_img
t1 = time.time()
images_aid = aid_img.satur_hue_augm_cv2(images,saturation_on,sat_low,sat_high,hue_on,hue_high-1)
t2 = time.time()
dt = t2-t1
print("AIDeveloper "+str(np.round(dt,2))+"s")

fig=plt.figure(1)
for i in range(1,5):
    ax=fig.add_subplot(2,2,i)        
    ax.imshow(images_aid[i])
    ax.axis("off")
fig.suptitle("AIDeveloper "+str(np.round(dt,2))+"s")
plt.savefig("04_Sat_Hue_aid_img.png")
plt.close(1)


print("""
#############Print system parameters and version numbers#######################
""")



text = ""
text+="System used:\n"
text+="OS: "+platform.platform()+"\n"
text+="CPU: "+platform.processor()+"\n"
text+="Python package versions:\n"
text+="Keras: v"+keras.__version__+"\n"
text+="PIL: v"+PIL.__version__+"\n"
text+="TensorFlow: v"+tf.__version__+"\n"
text+="OpenCV: v"+cv2.__version__+"\n"







