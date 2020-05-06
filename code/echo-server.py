import socket
import time
 
HOST = '192.168.0.105'
PORT = 8081
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
sock.bind((HOST, PORT))  
sock.listen(5) 
flash = False #flash mode off
em = False # emergency mode off
north = 0 #receive 11 north == 1 
          #receive 12 north == 2
while True:  
    connection,address = sock.accept()  
    try:  
        connection.settimeout(10)  
        buf = connection.recv(1024)  
        if buf == b'1':  
            connection.send(b'1')
            flash = True
            print('turn on flash mode!')
        elif buf == b'11':  #green
            north = 1
            connection.send(b'11')
            em = True
            print('turn on emergency mode!')
        elif buf == b'12':  #red
            north = 2
            connection.send(b'12')
            em = True
            print('turn on emergency mode!')
        elif buf == b'0':  
            connection.send(b'0') 
            flash = False
        elif buf == b'5':  
            connection.send(b'5') 
            em = False
            north = 0
        elif buf == b'3' and flash == True and em == False:
            connection.send(b'1')
            print('turn on amber flash!')
        elif buf == b'3' and flash == False and em == False:
            connection.send(b'10')
            print('regular mode on!')
        elif buf == b'3' and em == True and north == 1:
            connection.send(b'11')
            print('turn north and south green!')
        elif buf == b'3' and em == True and north == 2:
            connection.send(b'12')
            print('turn east and west green!')

    except socket.timeout:  
        print ('time out')
    connection.close()  


