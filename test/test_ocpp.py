import asyncio
import json
from websockets import connect
async def hello(uri):
    request = '''[ 2,
        "",
        "StatusNotification",
    {
        "errorCode": "NoError",
        "status": "Available"
    } ]'''
    async with connect(uri) as websocket:
        await websocket.send(request)
        message = await websocket.recv()
       # message = json.loads(message)
        print(message)
asyncio.run(hello("ws://localhost:1337/123abc"))