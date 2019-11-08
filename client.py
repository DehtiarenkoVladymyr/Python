import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        name = input("What is your name? : ")
        await websocket.send(name)
        greeting = await websocket.recv()
        print(f" {greeting}")

        age = input("How old are you? : ")
        await  websocket.send(age)
        greeting = await  websocket.recv()
        print(f" {greeting}")

asyncio.get_event_loop().run_until_complete(hello())