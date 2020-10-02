


class Connector:
  def __init__(self, localip,localport,targetip,targetport,msport,timestamp = ):
    self.localip = localip
    self.localport = localport
    self.targetip = targetip
    self.targetport = targetport
    self.msport = msport
    self.timestamp = timestamp




    
if __name__ == "__main__": 
    pass


#ALGO
#ONE ON ONE CONNECTION BOTH SIDES PING EACH OTHER ON CORRECT LOCAL PORT

#FLOOD BOTH SIDES OF PACKET - FULL CONE REPRESENT

#OPEN MULTIPLE PORTS IN SYMMTRIC AND SEND UDP PACKET TO FULL CONE, WHILE
#FULL CONE WILL MAKE BRUTEFORCE UDP PACKETS TO RANDOM PORTS

#SYM-SYM- YOU CANT DO THIS BRUH JUST GIVE UP
