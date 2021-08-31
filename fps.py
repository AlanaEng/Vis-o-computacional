"""
Calcular o número de frames por segundo e mostrar no vídeo em tempo real
by: Alana Melo
"""
# importar as bibliotecas necessárias
import cv2
import time as ts

video = cv2.VideoCapture(0) # inicializa a webcam do computador
endclock = 0 # inicializa o contador de frames

while True:
    __, frame_video = video.read()  # efetua a leitura dos frames de vídeo

    # efetua a contagem dos frames
    startclock = ts.time()
    fps = 1 / (startclock - endclock)
    endclock = startclock

    # exibe no vídeo em tempo real o número de frames por segundo calculados
    cv2.putText(frame_video, "FPS:"+str(int(fps)), (50, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (127,255, 0), 3)

    cv2.imshow("FPS_Counter", frame_video)
    cv2.waitKey(15) # se o número de frames estiver alto podemos aumentar o valor 1 para 15 ou mais desta função.
