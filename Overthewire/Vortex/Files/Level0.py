#!/usr/bin/env python3
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket is created.")
sock.connect(("vortex.labs.overthewire.org", 5842))
print("Connected to the server.")
sum = 0
for i in range(4):
    msg = sock.recv(4)
    print("data = ",msg)
    num = int.from_bytes(msg, byteorder='little', signed=False)
    print("num = ",num)
    sum=sum+num
    print("Sum = ",sum)
    print("="*100)
byte_sum = sum.to_bytes(sum,byteorder='little',signed=False)
#print("Sending back to server:\t",byte_sum)
sock.send(byte_sum)
response = sock.recv(1024)
print("Response:\t",response)

