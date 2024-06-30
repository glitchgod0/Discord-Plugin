import json
from telnetlib import Telnet
import re, time
from pypresence import Presence
import time

File = open("AppID.txt", "r")
ID = File.readline(1)
RPC = Presence(ID)
HOST = File.readline(2)


# Load game titles from JSON file
with open('ps4IDs.json') as f:
    game_titles = json.load(f)

def print_game_title(title_id):
    for game in game_titles:
        if game['TitleID'] == title_id:
            return game['Title']
    return None



RPC.connect()
while True:
    try:
        with Telnet(HOST, 3232) as tn:
            tn.read_until(b"[DISCORD]")

            # Read the next 10 characters
            data = tn.read_until(b"\n")
            CleanData = data.decode('utf-8').strip()
            game_title = print_game_title(CleanData)

            if game_title:
                RPC.update(
                    details="Playing:",  # Example details
                    state=game_title,
                    start=time.time(),
                )
                print(f"Game title for {CleanData}: {game_title}")
            else:
                RPC.update(
                    details="Playing:",  # Example details
                    state=CleanData,
                    start=time.time(),
                )
                print(f"No game found with title ID {CleanData}, Please open an issue on the github to add more games to the ps4IDs.json ")

    except EOFError as e:
        time.sleep(1)  # Wait for 1 second before retrying
    except Exception as e:
        time.sleep(1)  # Wait for 1 second before retrying
