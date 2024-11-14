import asyncio
import websockets
import logging
import json

# Configure logging
logging.basicConfig(filename='websocket_server.log', level=logging.INFO, format='%(asctime)s - %(message)s')

async def echo(websocket, path):
    try:
        async for message in websocket:
            if path == "/":
                logging.info(f"Received message: {message}")
                websocket.send("ECHO: " + message)
            else:
                endpoint_message = None
                if path == "/github/repos":
                    endpoint_message = "GitHub Repos message received\n"
                elif path == "/github/actions":
                    endpoint_message = "GitHub Actions message received\n"
                elif path == "/azure/repos":
                    endpoint_message = "Azure Repos message received\n"
                elif path == "/azure/actions":
                    endpoint_message = "Azure Actions message received\n"
                try:
                    json_message = json.loads(message)
                    pretty_message = endpoint_message + json.dumps(json_message, indent=4)
                    print(pretty_message)
                    logging.info(pretty_message)
                except json.JSONDecodeError:
                    print(endpoint_message + message)
                    logging.info(endpoint_message + message)
    except websockets.exceptions.ConnectionClosedError as e:
        logging.error(f"Connection closed with error: {e}")

start_server = websockets.serve(echo, "localhost", 8765)
print("WebSocket server started")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()