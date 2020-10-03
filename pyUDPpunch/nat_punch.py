import random
from random import randint
import socket
import stun
import datetime
import time


class Connector:

  def OneOne(self):
        LIMIT_MAX_RETRY = 5
    
        target_address = (self.targetip,self.msport)
        bufferSize = 1024
        data = b"oneone"
        UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        UDPClientSocket.settimeout(0.05)
        UDPClientSocket.bind(("0.0.0.0",self.msport))

        for i in range(LIMIT_MAX_RETRY):
          UDPClientSocket.sendto(data, target_address)
          try:
              msgFromServer = UDPClientSocket.recv(bufferSize)
              if(msgFromServer==data):
                print("Direct Connection Succeeded! Peer Connected!!")
                self.status = 1
                self.connection_ip = self.targetip
                self.connection_port = self.msport
                self.lport = self.msport
                return
          except socket.timeout:
            if(i==LIMIT_MAX_RETRY-1):
              print("Direct Connection Failed.. Going Next Step!!")
            continue


  def double_fullcone(self):
    d = datetime.datetime.utcnow()
    epoch = datetime.datetime(1970,1,1)
    t = int((d - epoch).total_seconds())

    timestamp = t+3  #TODO CHANGE
    while t<timestamp:
      print("Seconds Till Remaining:",timestamp-t)
      timestamp -= 1
      time.sleep(1)

    LIMIT_MAX_RETRY = 5000
    LIMIT_SECOND_TIMEOUT = 0.001
    data = b"double_fullcone"
    target_address = (self.targetip,self.targetport)
    bufferSize = 1024
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPClientSocket.settimeout(LIMIT_SECOND_TIMEOUT)
    UDPClientSocket.bind(("0.0.0.0",self.msport))

    for i in range(1,LIMIT_MAX_RETRY):
        if((LIMIT_MAX_RETRY/i).is_integer() and i>1000):
          print("Still Running..")
        UDPClientSocket.sendto(data, target_address)
        try:
            msgFromServer = UDPClientSocket.recv(bufferSize)
            if(msgFromServer==data):
              print("Two Way Hole Succeeded! Peer Connected!!")
              self.status = 1
              self.lport = self.msport
              self.connection_ip = self.targetip
              self.connection_port = self.targetport
              return
        except socket.timeout:
          if(i==LIMIT_MAX_RETRY-1):
            print("Two Way Failed.. Going Next Step!!")
          continue

    
    print(t)

  
  def __init__(self, localip,localport,targetip,targetport,msport= 0,timestamp = 0):
    self.status = 0
    self.connection_ip = ""
    self.connection_port = 0
    self.lport = 0
    
    self.localip = localip
    self.localport = localport
    self.targetip = targetip
    self.targetport = targetport
    self.msport = msport
    self.timestamp = timestamp
    if(msport==0):
      self.msport = randint(10000, 99999)
      print("Starting Connector On Port {}, Punching Hole Might Take Some Time!!".format(self.msport))      
    else:
      print("Starting Connector On Port {}, Punching Hole Might Take Some Time!!".format(self.msport))
      self.OneOne()

    if(self.status==0):
      self.double_fullcone()

    

    
  def load(self):
        return [self.status, self.connection_ip,self.connection_port, self.lport]


def main():
    targetip = input("Target IP:")
    targetport = int(input("Target PORT:"))

    print(Connector("127.0.0.1",12421,targetip,targetport,24252).load())

    
if __name__ == "__main__":
    targetip = input("Target IP:")
    targetport = int(input("Target PORT:"))

    print(Connector("127.0.0.1",12421,targetip,targetport,24252).load())
    
    #print(Connector("127.0.0.1",12421,"10.3.4.5",22254,24252).load())
    pass


#ALGO
#ONE ON ONE CONNECTION BOTH SIDES PING EACH OTHER ON CORRECT LOCAL PORT ---- DONE

#FLOOD BOTH SIDES OF PACKET - FULL CONE REPRESENT

#OPEN MULTIPLE PORTS IN SYMMTRIC AND SEND UDP PACKET TO FULL CONE, WHILE
#FULL CONE WILL MAKE BRUTEFORCE UDP PACKETS TO RANDOM PORTS

#SYM-SYM- YOU CANT DO THIS BRUH JUST GIVE UP
