'''
Limiar Binário:
definir um limite abaixo do qual todos os valores de pixel são convertidos para preto 
e o restante é convertido para branco para obter uma imagem binarizada.

Técnica é usada para converter uma imagem de RGB para monocromática (preto e branco).
'''
import cv2
from PIL import Image
import matplotlib.pyplot as plt

img = cv2.imread('IMAGE.jpg',0)   # ALTERAR AQUI O CAMINHO DA IMAGEM NO COMPUTADOR
 
ret,thresh1 = cv2.threshold(img,170,255,cv2.THRESH_BINARY)

titles = ['Original Image', 'Binary Thresholding']
images = [img, thresh1]
for i in range(2):
    plt.figure(figsize=(20,20))
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
