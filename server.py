import asyncio
import websockets

async def echo(websocket, path):
    name = await websocket.recv()
    print(f" {name}")

    greeting = f"Hello {name}!"

    await  websocket.send(greeting)
    print(f"  {greeting}")

    age = await websocket.recv()
    print(f" {age}")
    greeting = f"Wow! Thanks {name}!"
    await  websocket.send(greeting)
    print(f" {greeting}")

start_server = websockets.serve(echo, "localhost", 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

