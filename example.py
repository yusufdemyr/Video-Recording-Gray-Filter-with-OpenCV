import cv2
import time
import numpy as np

#######################
wCam, hCam = 1280,720
#######################

cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
pTime = 0

# Video kaydı için gerekli olan değişkenler
record = False # kayıt durumu
out = None # video dosya yazarı
filename = 'recorded.mp4' # kaydedilecek video dosyası adı
frame_size = (int(cap.get(3)), int(cap.get(4))) # video boyutu

while True:
    success, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(gray, f'FPS: {int(fps)}',(40,70), cv2.FONT_HERSHEY_COMPLEX, 3,(255,0,255),3)

    cv2.imshow("Frame", gray)
    
    key = cv2.waitKey(1)
    if key == 27: # eğer anahtar kodu 27 (esc tuşunun anahtar kodu) ise while döngüsünden çık
        break
    elif key == ord('1'): # eğer '1' tuşuna basıldıysa kayıt durumunu değiştir
        record = not record
        if record:
            # video dosyasını aç
            out = cv2.VideoWriter(filename, cv2.CAP_FFMPEG, 30.0, frame_size)
            print('Recording started.')
        else:
            # video dosyasını kapat
            out.release()
            print('Recording stopped.')

    # eğer kayıt modunda ise, kayıt dosyasına frame yaz
    if record:
        out.write(gray)

cap.release()
