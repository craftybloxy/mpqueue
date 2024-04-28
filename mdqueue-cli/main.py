
import argparse
import asyncio
from modules.mpd_client import connect_to_mpd
from modules.queue_manager import print_queue
import os

# get the size of the terminal
_ , terminal_rows = os.get_terminal_size(0)

#a weird hack to remove the cursor 
print('\033[?25l', end="")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', type=str, default='localhost', help='MPD server host')
    parser.add_argument('--port', type=int, default=6600, help='MPD server port')
    parser.add_argument('--style', type=str, choices=['full','follow'], default='follow', help='Queue style')
    parser.add_argument('--length', type=int, default=terminal_rows, help='How many songs to print in follow mode') 
    args = parser.parse_args()
    length = args.length - 3 #I use "-3" because the last line is taken by the cursor and two lines are empty
    async def run():
        try:
            client = await connect_to_mpd(args.host, args.port)
        except Exception as e:
            print("Connection failed:", e)
            return

        await print_queue(client, args.style, length)
        async for subsystem in client.idle():
            await print_queue(client, args.style, length)

    asyncio.run(run())

if __name__ == '__main__':
    main()
