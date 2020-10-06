import random
from random import randint
import socket
import stun
import datetime
import time
from itertools import cycle


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
                UDPClientSocket.close()
                break
          except socket.timeout:
            if(i==LIMIT_MAX_RETRY-1):
              print("Direct Connection Failed.. Going Next Step!!")
            continue

          UDPClientSocket.close()


  def double_fullcone(self):
    d = datetime.datetime.utcnow()
    epoch = datetime.datetime(1970,1,1)
    t = int((d - epoch).total_seconds())

    if(self.timestamp==0):
      self.timestamp = t+3  #TODO CHANGE
      
    while t<self.timestamp:
      print("Seconds Till Remaining:",self.timestamp-t)
      self.timestamp -= 1
      time.sleep(1)

    LIMIT_MAX_RETRY = 4096
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
              break
        except socket.timeout:
          if(i==LIMIT_MAX_RETRY-1):
            print("Two Way Failed.. Going Next Step!!")
          continue

        UDPClientSocket.close()


        
  def fullCone_Sym(self):
    NUM_PORTS = 2048
    socket_list = []
    LIMIT_MAX_RETRY_SYM = 200
    LIMIT_BRUTEFORCE_LISTEN_SYM_SECOND = 20
    LIMIT_SECOND_TIMEOUT_SYM = 0.001
    bufferSize = 32
    data = b"sym_full"
    print("Looks Like Connection Has Symmetric Peer, Bruteforcing Ports List!!")
    
    if(self.nat_type == "Symmetric NAT"):
      print("Making Random Ports!")
      target_address = (self.targetip,self.targetport)
      for port in random.sample(range(1025,65536),NUM_PORTS):
        try:
          server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
          server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
          server_socket.bind(('0.0.0.0', port))
          UDPClientSocket.settimeout(LIMIT_SECOND_TIMEOUT_SYM)
          server_socket.listen(1)
          for i in range(2):
            server_socket.sendto(data, target_address)
          socket_list.append(server_socket)
        except Exception:
          pass

      socket_iter = cycle(socket_list)
      max_e_ind = len(socket_list)-1
      i=0
      j=0
      print(max_e_ind)
      while True:
        if (i>int(LIMIT_BRUTEFORCE_LISTEN_SYM_SECOND//LIMIT_SECOND_TIMEOUT_SYM)):
          break
        if(j==max_e_ind):
          j=0
        print(j)
        current_sock = socket_iter[j]
        print(i)
        try:
            msgFromServer = current_sock.recv(bufferSize)
            if(msgFromServer==data):
              print("Bruteforce Succeeded! Peer Connected!!")
              self.status = 1
              self.lport = current_sock.getsockname()[1]
              self.connection_ip = self.targetip
              self.connection_port = self.targetport
              break
        except socket.timeout:
          if(i==LIMIT_MAX_RETRY-1):
            print("Bruteforce Failed! Looks Like Connection Cant Be Made, Sorry :(")
          continue
        i+=1
        j+=1

    elif(self.nat_type == "Symmetric NAT"):
        pass


    for socks in socket_list:
      socks.close()
        
  
  def __init__(self, targetip = "",targetport = 0,msport= 0,timestamp = 0):
    self.status = 0
    self.connection_ip = ""
    self.connection_port = 0
    self.lport = 0

    self.nat_type, self.localip, self.localport = stun.get_ip_info()
    
    self.targetip = str(targetip)
    self.targetport = int(targetport)
    self.msport = int(msport)
    self.timestamp = int(timestamp)


  def setOn(self,targetip,targetport,msport= 0,timestamp = 0):
    self.targetip = targetip
    self.targetport = targetport
    self.msport = msport
    self.timestamp = timestamp


  def local_info(self):
    return (self.nat_type, self.localip, self.localport)

  def start_connection(self):
    if(not self.targetip):
      print("No IP Assigned, Use setOn Before Starting Connection..")
      return
    if(self.msport==0):
      self.msport = randint(1025,65536)
      
      print("Starting Connector On Port {}, Punching Hole Might Take Some Time!!".format(self.msport))      
    else:
      print("Starting Connector On Port {}, Punching Hole Might Take Some Time!!".format(self.msport))
      self.OneOne()

    if(self.status==0):
      self.double_fullcone()

    if(self.status==0):
      self.fullCone_Sym()

    

    
  def load(self):
        return (self.status, self.connection_ip,self.connection_port, self.lport)

    
def main():
    print("Wait.. Getting Your Data!!")
    x=Connector()
    print(x.local_info())
    targetip = input("Target IP:")
    targetport = int(input("Target PORT:"))
    timestamp = int(input("Enter Connection Timestamp:"))
    print(Connector(targetip,targetport,24252,timestamp).load())


#ALGO
#ONE ON ONE CONNECTION BOTH SIDES PING EACH OTHER ON CORRECT LOCAL PORT ---- DONE

#FLOOD BOTH SIDES OF PACKET - FULL CONE REPRESENT

#OPEN MULTIPLE PORTS IN SYMMTRIC AND SEND UDP PACKET TO FULL CONE, WHILE
#FULL CONE WILL MAKE BRUTEFORCE UDP PACKETS TO RANDOM PORTS

#SYM-SYM- YOU CANT DO THIS BRUH JUST GIVE UP
