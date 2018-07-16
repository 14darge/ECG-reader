import serial
import time
import numpy 
import matplotlib.pylab as plt
import sys

serial_port = 'COM3';
baud_rate = 9600; #In arduino, Serial.begin(baud_rate)
ecgText = "señalECG.txt";
tiempoText = "tiempo.txt"

salidaECG = open(ecgText, "w+");
salidaTiempo = open(tiempoText, "w+")
ecg = serial.Serial(serial_port, baud_rate)

validacion = True

guardarTiempo = numpy.array([])
guardarECG = numpy.array([])

#pulso = 0

while validacion == True:

    line = ecg.readline();
    #line = str(line)
    line = line.decode("latin-1") #ser.readline returns a binary, convert to string
    #print(line);
    #if line > 3:
    #	pulso + 1

    salidaECG.write(line);
    
    tiempo = time.clock()
    tiempo = '{:.2f}'.format(tiempo)
    tiempoString = str(tiempo)
    salidaTiempo.write(tiempoString + '\n')
    print(tiempo)


    guardarECG = numpy.append(guardarECG, line)
    guardarTiempo = numpy.append(guardarTiempo, tiempo)


    if tiempoString == '60.00':
    	validacion = False 
   
#print(pulso)
plt.plot(guardarTiempo, guardarECG)
plt.show()