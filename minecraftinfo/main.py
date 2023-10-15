from mcstatus import JavaServer
import requests
import ast
import base64

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

class get_skin:
    def __str__(self, mcid:str):
        self.mcid = mcid
        self.uuid = ast.literal_eval(requests.get("https://api.mojang.com/users/profiles/minecraft/"+self.mcid).text)
        self.id = self.uuid["id"]
        self.userdata = (ast.literal_eval(base64.b64decode((ast.literal_eval(requests.get("https://sessionserver.mojang.com/session/minecraft/profile/"+self.id).text))["properties"][0]["value"]).decode()))["textures"]["SKIN"]["url"]
        return self.userdata

class get_cape:
    def __str__(self, mcid:str):
        self.mcid = mcid
        self.uuid = ast.literal_eval(requests.get("https://api.mojang.com/users/profiles/minecraft/"+self.mcid).text)
        self.id = self.uuid["id"]
        self.userdata = (ast.literal_eval(base64.b64decode((ast.literal_eval(requests.get("https://sessionserver.mojang.com/session/minecraft/profile/"+self.id).text))["properties"][0]["value"]).decode()))["textures"]["CAPE"]["url"]
        return self.userdata
