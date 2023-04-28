import asyncio
from rustplus import RustSocket
from PIL import Image


async def drawMap(s):
    # Draws Map to PNG
    res = await s.get_map(True,True, True, None, False)
    res.save("map.png")

async def findMonument(monument):
    global rustmap
    for m in rustmap.monuments:
        if m.token == monument:
            return m
    return None




async def main(**tcID):
    socket = RustSocket("64.52.81.217", "28092", 76561198096181161, 1578316819)
    await socket.connect()

    print(f"It is {(await socket.get_time()).time}")

    await getTCStuff(tcID, socket)
    await drawMap(socket)
    await socket.send_team_message("Sent with Rust+")
    await socket.disconnect()


async def getTCStuff(tcID):
    socket = RustSocket("64.52.81.217", "28092", 76561198096181161, 1578316819)
    tcContents = socket.get_contents(tcID, False)
    print(tcContents.protection_time)




    
