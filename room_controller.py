import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import asyncio
from kasa import SmartPlug

cid ="###################################" 
secret = "################################"
username = "#############"
redirect_url='http://localhost:8000'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret) 
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
scope = "playlist-modify-public playlist-modify-private playlist-read-private user-modify-playback-state"
token = util.prompt_for_user_token(username, scope,cid,secret,redirect_url)

if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("Can't get token for", username)    

reader = SimpleMFRC522()
p = SmartPlug("#######")


async def run_rfid():
    is_playing = False
    while 1:
            await p.update()
            id, text = reader.read()
            if id == ##########:
                print("first")
                try:
                    if is_playing == False:
                        try:
                            sp.start_playback(device_id='####################',context_uri="spotify:playlist:##############",position_ms = 500000000 )
                            sp.shuffle(True,device_id='######################')
                            is_playing = True
                        except:
                            print("Device is offline")
                    else:
                        try:
                            sp.pause_playback(device_id='##########################')
                            is_playing = False
                        except:
                            print("Device is offline")
                    
                finally:
                        GPIO.cleanup()
                        time.sleep(5)
            elif id == #############:
                try:
                    print("second")
                    if p.is_on == True:
                        await p.turn_off()
                    else:
                        await p.turn_on()
                    
                finally:
                    GPIO.cleanup()
                    time.sleep(5)

            elif id ==  873688728395:
                try:
                    if is_playing == False:
                        try:
                            sp.start_playback(device_id='########################',context_uri="spotify:playlist:################",position_ms = 500000000 )
                            sp.shuffle(True,device_id='##########################')
                            is_playing = True
                        except:
                            print("Device is offline")
                    else:
                        try:
                            sp.pause_playback(device_id='###########################')
                            is_playing = False
                        except:
                            print("Device is offline")
                finally:
                    GPIO.cleanup()
                    time.sleep(5)

if __name__ == "__main__":
    asyncio.run(run_rfid())
