'''
Manipulação morfológica:
As operações morfológicas são algumas formas simples de operações usadas para transformações de imagens. 
Quando você tem alguns objetos cujos limites não são claros, você pode usar operações morfológicas para expandir seus limites,
o que ajudará a encontrar objetos facilmente.

A erosão a corroer o primeiro plano da imagem, minimizando assim os valores de pixels brancos na imagem. 
O grau de corrosão depende inteiramente do tamanho do kernel e do número de iterações às quais você aplica esse kernel. 
O kernel é uma matriz de tamanho quadrado com apenas valores 1 e 0 para gerar a imagem de erosão.
'''


import cv2
from PIL import Image
import matplotlib.pyplot as plt


img = cv2.imread('IMAGE.jpg', 0)  # MODIFICAR PARA O CAMINHO DA SUA IMAGEM NO COMPUTADOR

kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)

titles = ["Original Image", "Eroded Image"]
images = [img, erosion]
plt.figure(figsize=(20,20))

for i in range(2):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
