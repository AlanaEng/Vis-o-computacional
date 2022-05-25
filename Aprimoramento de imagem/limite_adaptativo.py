'''
Limite Adaptativo: Ao contrário do método de limite binário, este método determina seu limite com base em uma pequena área circundante do valor do pixel. 
Existem também dois tipos deste método:

Adaptive Threshold Mean: O limiar é a área ao redor da média menos um C fixo.
Adaptive gaussian thresholding: O limiar é uma soma ponderada gaussiana de valores de vizinhança menos uma constante C.
Esse método é usado principalmente para remover diferentes condições de iluminação em uma imagem, pois obtemos valores de pixel com base em sua área circundante.
'''
## import dependencies

import cv2
from PIL import Image
import matplotlib.pyplot as plt

img = cv2.imread('IMAGE.jpg', 0)   # MODIFICAR O CAMINHO DA IMAGEM SALVA NO COMPUTADOR

## adaptive mean thresholding
th1 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)

## adaptive gaussian thresholding
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

titles = ['Original Image', 'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2]
plt.figure(figsize=(20,20))

for i in range(3):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
