import os
from rich.console import Console
from rich.text import Text

console = Console(highlight="False")
#a weird hack to remove the console's cursor 
print('\033[?25l', end="")

async def clear():
    os.system('cls' if os.name=='nt' else 'clear')

async def print_queue(client, style, length):
    await clear()
    current_status = await client.status()
    try:
        current_song = int(current_status['song'])
    except:
        current_song = -1
    queue = [x['file'] for x in await client.playlistinfo()]
    to_print = Text()
    if style == 'full':
        for i in range(min(len(queue),length)):
            if i == current_song:
                to_print.append(queue[i]+'\n', style="white on black")
            else:
                to_print.append(queue[i]+'\n', style="blue on black")
            last_index = i
        to_print.append('+'+str(len(queue)-last_index)+'songs')
    elif style == 'follow':
        if current_song == -1:
            to_print.append(queue.join('\n'))
        else:
            to_print.append('\n')
            to_print.append(queue[current_song]+'\n', style="white on black")
            to_print.append('\n')
            for i in range(current_song + 1, min(current_song + length, len(queue))-1):  # Print the next x songs (x=length)
                to_print.append(queue[i]+'\n', style="blue on black")
                last_index = i
            songs_left = len(queue)-last_index-2
            if songs_left > 0:
                to_print.append('- '+str(len(queue)-last_index-2)+' songs left -', style="blue on black")

            
    console.print(to_print)