'''
Redimensionamento é o processo de aumentar ou diminuir o zoom de uma imagem para alterar a resolução da imagem. Quando você redimensiona uma imagem, diferentes valores de pixel nessa imagem são copiados para torná-la mais pixelizada, e os valores de pixel são removidos para torná-la menor.

Esse método é usado principalmente para classificação de imagens e detecção de objetos, pois você precisa redimensionar a imagem para o tamanho de entrada do modelo.
'''
import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


img = Image.open('IMAGE.jpg')  # MODIFICAR O CAMINHO DA IMAGEM NO COMPUTADOR
dst = img.resize((50,50))

titles = ["Original Image", "Rescaled Image"]
images = [np.asarray(img), np.asarray(dst)]
plt.figure(figsize=(20,20))

for i in range(2):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
