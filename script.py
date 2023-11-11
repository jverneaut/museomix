import vlc
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

vlc_instance = vlc.Instance('--no-xlib')
vlc_player = vlc_instance.media_player_new()

videos = [
    { 'path': 'sample.mp4', 'pin': 17 }
]

for video in videos:
    def sensorCallback():
        if GPIO.input(video['pin']):
            print("HIGH")
        else:
            print("LOW")

    GPIO.setup(video['pin'], pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(video['pin'], callback=sensorCallback, bouncetime=200)
