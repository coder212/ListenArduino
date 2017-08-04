import serial
import os
def create_file(text):
   f = open('/home/arba/suhuruangan.txt', 'a')
   f.write(text)
   f.close()

def read_file():
   f = open('/home/arba/suhuruangan.txt', 'r+')
   text=f.read()
   f.close()
   return text

def rewrite_file(text):
   f = open('/home/arba/suhuruangan.txt', 'r+')
   f.seek(0)
   f.truncate()
   f.write(text)
   f.close()
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=5) 
while True:
     data= ser.readline()
     if data != None:
        if not os.path.isfile('/home/arba/suhuruangan.txt'):
           create_file(data);
        else:
           if data != "":
              rewrite_file(data);
