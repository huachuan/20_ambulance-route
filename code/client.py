#!/usr/bin/python
# -*- coding: UTF-8 -*-
import socket
import sys

CID='11' #The first 1 represents lights, the second 1 represent the light ID

#Server information
s_port=8081
s_host='127.0.0.1'

def main():
    if len(sys.argv) != 2:
        print("argv number:",sys.argv)
        print('Please input the signal(0-Red,1-Green,2-Yellow)')
        return
    client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s_msg = CID + '-' + sys.argv[1]
    print("s_msg:",s_msg)
    #client.sendto(b'hello,this is a test info !',(host,port))
    client.sendto(s_msg,(s_host,s_port))
    recv, addr=client.recvfrom(1024)
    print("Recv msg:",recv)
        

if __name__ == "__main__":
    main()
