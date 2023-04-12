import cv2
import numpy as np
import matplotlib.pyplot as plt

apple = cv2.imread(r"C:\Users\VikeeDada\Downloads\apple img opencv.jpg")
orange = cv2.imread(r"C:\Users\VikeeDada\Downloads\orange img opencv.jpg")

orange = cv2.resize(orange,(500,500))
apple = cv2.resize(apple,(500,500))

print(apple.shape)
print(orange.shape)

apple_orange = np.hstack((apple[:, :250], orange[:, 250:]))
cv2.imshow('img',apple_orange[:,:,::1])

apple_copy = apple.copy
gp_apple = [apple_copy]

for i in range(6):
    apple_copy = cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

    orange_copy = orange.copy()
    gp_orangec = [orange_copy]
    for i in range(6):
        orange_copy = cv2.PyDown(orange_copy)
        gp_orange.append(orange_copy)

apple_copy = gp_apple[5]
lp_apple = [apple_copy]
for i in range (5,0,-1):
    gaussian_expanded = cv2.pyrUp(gp_apple[i])
    laplacian = cv2.substract (gp_apple[i-1], gaussian_expanded)
    lp_apple.append(laplacian)

orange_copy = gp_orange[5]
lp_orange = [orange_copy]
for i in range (5,0,-1):
    gaussian_expanded = cv2.pyrUp(gp_apple[i])
    laplacian = cv2.substract (gp_orange[i-1], gaussian_expanded)
    lp_orange.append(laplacian)


apple_orange_pyramid = []
n = 0
for apple_lap, orange_lap in zip(lp_apple, lp_orange):
    n += 1
    cols, rows, ch = apple_lap.shape
    laplacian = np.hstack(apple_lap[:, 0:int(cols/2)],orange_lap[:, 0:int(cols/2):])
    apple_orange_pyramid.append(laplacian)

apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range (1,6):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv2.add(apple_orange_pyramid[i],apple_orange_reconstruct)

cv2.imshow('final',apple_orange_reconstruct[:, :, ::-1 ])
cv2.imshow(apple_orange_reconstruct[:, :, ::-1 ])

