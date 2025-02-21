import os
import eel
import subprocess

from engine.features import *
from engine.command import *
from engine.auth import recoganize

def start():
    eel.init("www")

    # Add root route handler
    @eel.expose
    def get_root():
        return "JARVIS is running"

    # Play assistant sound
    try:
        playAssistantSound()
    except Exception as e:
        print(f"Error playing sound: {str(e)}")

    @eel.expose
    def init():
        subprocess.call([r'device.bat'])
        eel.hideLoader()
        playAssistantSound()
        speak("Ready for Face Authentication")
        try:
            flag = recoganize.AuthenticateFace()
        except Exception as e:
            print(f"Error during face authentication: {str(e)}")
            speak("Face authentication failed due to an error.")
            return
        if flag == 1:
            eel.hideFaceAuth()
            speak("Face Authentication Successful")
            eel.hideFaceAuthSuccess()
            speak("Hello, Welcome Sir, How can I Help You")
            eel.hideStart()
            playAssistantSound()
        else:
            speak("Face Authentication Fail")
    
    os.system('start chrome.exe --app="http://localhost:8000/index.html"')

    @eel.expose
    def default_route():
        return "Welcome to Jarvis"

    # Modify Eel start with additional parameters
    try:
        eel.start('index.html', 
                 mode=None, 
                 host='localhost', 
                 port=8000,
                 block=True,
                 close_callback=lambda page, sockets: print("JARVIS closed"),
                 shutdown_delay=1.0)
    except Exception as e:
        print(f"Error starting Eel: {str(e)}")
        speak("Unable to start interface")
        return

    print("JARVIS started successfully")