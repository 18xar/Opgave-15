import socket

class Client():
  def __init__(self):
    self.name = ""
    self.ip = ""

  def connect(self, ip):
    self.ip = ip

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(MESSAGE)
    data = s.recv(BUFFER_SIZE)
    s.close()
    
    print "received data:", data
  