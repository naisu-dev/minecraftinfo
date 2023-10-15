from mcstatus import JavaServer

class mcje_server:
    def __init__(self, ipaddress:str, port:int):
        self.ipaddress = ipaddress
        self.port = port
        self.server = JavaServer.lookup(ipaddress+":"+str(port))
        self.data = self.server.status()
        self.icon = self.data.icon
        self.players = self.data.players.sample
        self.maxplayers = self.data.players.max
        self.version = self.data.version.name
        self.protocol = self.data.version.protocol
        self.motd = self.data.motd
        self.icon = self.data.icon
        self.ping = self.server.ping()