discord.py
==========
<a href="https://pypi.python.org/pypi/minecraftinfo">
<img src="https://img.shields.io/pypi/v/minecraftinfo.svg" alt="pypi">
</a> 
<a href="https://discord.com/invite/xWvSTkjNm3">
<img src="https://discord.com/api/guilds/1164890966507913237/embed.png" alt="discord">
</a> 

minecraftinfoはpythonでマインクラフトのサーバーやスキンなどの情報を取得することができるライブラリです

使用方法
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
