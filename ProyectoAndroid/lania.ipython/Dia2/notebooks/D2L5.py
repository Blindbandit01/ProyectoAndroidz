import android
droide=android.Android()

archivo = droide.dialogGetInput("Ecriba nombre de archivo")
dt = 100
fin = 30000
tiempo = 0
droide.startSensingTimed(2,dt)

lecturas = []
droide.ttsSpeak("Inicio de recorrido")
import time
while tiempo <= fin:
    lecturas.append(droide.sensorsReadAccelerometer().result)
    time.sleep(dt/1000.0)
    tiempo += dt
    
droide.stopSensing();
droide.ttsSpeak("Fin de recorrido")

import csv
#c = csv.writer(open("MYFILE.csv", "wb"))
#c.writerow(lecturas)
with open(archivo.result + '.csv', 'w') as fp:
    a=csv.writer(fp,delimiter=',')
    a.writerows(lecturas)