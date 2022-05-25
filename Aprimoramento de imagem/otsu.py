'''
Binarização de Otsu
Este método não requer nenhum parâmetro de limite, pois é determinado automaticamente. 
Este método determina o limite criando um histograma de todos os valores de pixel e calculando a média a partir dele.
'''


import cv2
from PIL import Image
import matplotlib.pyplot as plt


img = cv2.imread('lighting_conditions.jpg', 0)

## apply Otru's thresholding
ret3,th1 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

titles = ["Original Image", "Binary Otsu's Thresholding"]
images = [img, th1]
plt.figure(figsize=(20,20))

for i in range(2):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
