<img src="https://raw.githubusercontent.com/naisu-dev/naisu-dev/main/minecraftinfo.png" width=30px> minecraftinfo
==========
<a href="https://pypi.python.org/pypi/minecraftinfo">
<img src="https://img.shields.io/pypi/v/minecraftinfo.svg" alt="pypi">
</a> 
<a href="https://discord.com/invite/xWvSTkjNm3">
<img src="https://img.shields.io/discord/1164890966507913237?color=5865f2&label=Discord&logo=Discord&logoColor=ffffff" alt="discord">
</a>
<a href="https://opensource.org/license/MIT/">
<img src="https://img.shields.io/github/license/naisu-dev/minecraftinfo" alt="MIT">
</a>

<br>
minecraftinfo is a library that allows you to get information about minecraft servers, skins, etc. in python

usage rules
==========
```python
import minecraftinfo as mcinfo

server = mcinfo.mcje_server("minecraft.com", 25565)
print(server.icon)
print(server.players)
print(server.maxplayers)
print(server.version)
print(server.protocol)
print(server.motd)
print(server.ping)

skin = mcinfo.get_skin("notch")
print(skin)

cape = mcinfo.get_cape("notch")
print(cape)
```

error
==========
### ping error
`Server is not running or server has been modified to not respond to status requests`<br>
If you get this error message, the server you want to retrieve is not running or is configured not to respond to status requests.
