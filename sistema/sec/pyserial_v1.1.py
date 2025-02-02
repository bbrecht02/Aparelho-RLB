import serial as sers
import time
import json #utilizar arquivo json para guardar as ids dos usuarios 
ser = sers.Serial('COM21', baudrate = 9600, timeout = 1)

data = []
dado = []
card_id = 0
btn_data = open('btn_data.txt', 'a+')
cid_data = open('cid_data.txt', 'a+')

def getValues():
    
    ser.write(b'g')
    arduinoData = ser.readline().decode('UTF-8').split('\r\n')

    return arduinoData[0]

while True:

    s = serial.Serial(15, 9600) #port is 11 (for COM12, and baud rate is 9600
    time.sleep(2)    #wait for the Serial to initialize
    s.write('Ready...')
    while True:
    str = raw_input('Enter text: ')
    str = str.strip()
    if str == 'exit' :
            break
    s.write(str)

    dado = getValues().split(',')
    if dado != '':

        if dado[0] == "k":
            print('numberpad identificado')
            btn = dado[1]
            print(btn)
            
        if dado[0]  == "r":
            print('rfid identificado')
            cid = dado[1]
            id= []
            id.append(cid)
            id.append("\n")
            cid_data.writelines(id)
            cid_data.close()
            print(cid)
            """ trocar essa print(cid) posteriormente 
            pelo nome do usuario que regigtrou a baia  atraves de uma checagem no json"""
            print("Sua Baia foi registrada")
            break

cid_data.close()
