30 lines (22 sloc)  1.12 KB
   
'''
Manipulação morfológica:
As operações morfológicas são algumas formas simples de operações usadas para transformações de imagens. 
Quando você tem alguns objetos cujos limites não são claros, você pode usar operações morfológicas para expandir seus limites,
o que ajudará a encontrar objetos facilmente.

Dilatação: Esta operação é oposta à erosão, ela tenta maximizar as áreas brancas na imagem. Também depende do tamanho do kernel e do número de iterações.
'''
import cv2
from PIL import Image
import matplotlib.pyplot as plt


img = cv2.imread('text_document.jpg', 0)

kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(img,kernel,iterations = 1)

titles = ["Original Image", "Dilated Image"]
images = [img, dilation]
plt.figure(figsize=(20,20))

for i in range(2):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

