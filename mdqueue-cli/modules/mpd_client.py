from mpd.asyncio import MPDClient

async def connect_to_mpd(host='localhost', port=6600):
    client = MPDClient()
    await client.connect(host, port)
    return client
