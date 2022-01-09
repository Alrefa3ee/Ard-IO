from pywebio.input import input
import serial
import time

text = str(input("add your text : "))

s = serial.Serial('COM8', 9600) #port is 11 (for COM12, and baud rate is 9600
time.sleep(1)    #wait for the Serial to initialize
while True:
    x = text.encode()
    x = x.strip()
    s.write(x)