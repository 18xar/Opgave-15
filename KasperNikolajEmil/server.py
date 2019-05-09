import socket


class Server():
  def __init__(self):
    self.ip = socket.gethostbyname(socket.gethostname())

  def getIP(self):
    return self.ip


sv = Server()

print(sv.getIP())