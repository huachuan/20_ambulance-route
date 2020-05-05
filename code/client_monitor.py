#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket
import sys

#local information
s_port = 12345
s_addr = '127.0.0.1'

'''
def green_light(s,addr,msg):
    send_data="1"
    s.sendto(send_data,addr)

def yellow_light(s,addr,msg):
    send_data="2"
    s.sendto(send_data.encode("utf-8"),addr)

def red_light(s,addr,msg):
    send_data="0"
    s.sendto(send_data,addr)
'''
def main():
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind((s_addr,s_port))

    print('waiting for receiving...')
    while True:
        data,addr=s.recvfrom(1024)
        print('Received:',data,'from',addr)
        if data == '1':
            #Should change the light to Green
            print('Green_light on')
        elif data == '2':
            #Should change the light to Yellow
            print('Yellow_light on')
        elif data == '0':
            #red_light(s,addr,data)
            print('Red_light on')
        else:
            print('No change')

if __name__ == "__main__":
    main()
