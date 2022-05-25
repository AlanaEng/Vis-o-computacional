'''
Às vezes, as imagens parecem melhores ao olho humano, mas quando passamos essas imagens para qualquer modelo baseado em visão computacional, 
como classificação e detecção de objetos, os resultados não são ideais porque os objetos ruidosos que queremos encontrar são distorcidos e 
podem não corresponder ao modelo Os objetos treinados não correspondem, portanto, o ruído nas imagens reduz a precisão do modelo.

OpenCV fornece uma função chamada fastNIMeansDenoising() que suaviza imagens para reduzir o ruído da imagem.
'''

import cv2
from PIL import Image
import matplotlib.pyplot as plt


img = cv2.imread('noisy_image.jpg')

dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)

titles = ["Original Image", "Denoised Image"]
images = [img, dst]
plt.figure(figsize=(20,20))

for i in range(2):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
