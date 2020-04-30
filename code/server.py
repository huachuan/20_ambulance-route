#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket
import sys

#local information
s_addr='127.0.0.1'
s_port=8081

#client info
c_port=12345

def get_ids(address):
    f = open("light.conf",'r')
    result = list()
    for line in open('light.conf'):
        line = f.readline().replace('\n', '').replace('\r', '')
        if line.startswith('#'):
            continue
        if line.startswith(address):
            ip,ips1,ips2 = line.split(' ',2)
            f.close()
            return ip,ips1,ips2
        #result.append(line)
    f.close()
    return None

def change_lights(address,csig):
    ip,ips1,ips2 = get_ids(address)
    ips1_list = ips1.split(',')
    ips2_list = ips2.split(',')

    send_msg(csig,ip);

    for i in range(0, len(ips1_list)):
        send_msg(csig,ips1_list[i])
    if csig == '1':
        csig_opposite = '0'
    elif csig == '0':
        csig_opposite = '1'
    else:
        csig_opposite = ''
    for i in range(0, len(ips2_list)):
        send_msg(csig_opposite,ips2_list[i])
    #print ips2

def send_msg(msg, host):
    c=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    c.sendto(msg,(host,c_port))
    print('send ', host, 'signal:', msg)

#def control_lights()
def green_light(s,addr,msg):
    send_data="1"
    s.sendto(send_data,addr)

def yellow_light(s,addr,msg):
    send_data="2"
    s.sendto(send_data,addr)

def red_light(s,addr,msg):
    send_data="0"
    s.sendto(send_data,addr)

def main():
    #test
    '''
    testaddr='127.0.0.1'
    change_lights(testaddr,'0')
    return
    '''
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind((s_addr,s_port))

    print('waiting for receiving...')
    #cid,csignal = teststr.split('-',1)
    while True:
        data,addr=s.recvfrom(1024)
        print('Received:',data,'from',addr)
        cid,csignal = data.split('-',1)
        #print('Received csignal:',csignal)

        if csignal == "1":
            green_light(s,addr,data)
            change_lights(addr,'1')
        elif csignal == "2":
            yellow_light(s,addr,data)
            change_lights(addr,'2')
        elif csignal == "0":
            red_light(s,addr,data)
            change_lights(addr,'0')
        else:
            print('client no light')
        print('\n')

if __name__ == "__main__":
    main()
