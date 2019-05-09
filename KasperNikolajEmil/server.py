import socket


class Server():
  def __init__(self):
    slef.name = ""
    self.ip = socket.gethostbyname(socket.gethostname())
    self.port = 80
    self.bufferSize = 20

    self.conn
    self.addr

  def getIP(self):
    return self.ip
  
  def startServer(self, name):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((self.ip, self.port))
    s.listen(1)
    self.conn, self.addr = s.accept()

  def loopServer(self):
    data = self.conn.recv(self.buffersize)
    if not data: 
      break
    print("received data:", data)
    self.conn.send(data)

  def stopServer(self):
    self.conn.close()

  def sendMessage(self,):