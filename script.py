import vlc
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

vlc_instance = vlc.Instance('--no-xlib')
vlc_player = vlc_instance.media_player_new()

videos = [
    { 'path': 'sample.mp4', 'pin': 11 },
    { 'path': 'sample-2.mp4', 'pin': 13 },
]

for video in videos:
    video['media'] = vlc_instance.media_new(video['path'])

    def sensorCallback(channel):
        print(channel)
        if GPIO.input(video['pin']):
            for item in videos:
                if item['pin'] == channel:
                    vlc_player.set_media(item['media'])
                    vlc_player.play()
        else:
            vlc_player.pause()

    GPIO.setup(video['pin'], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(video['pin'], GPIO.BOTH, callback=sensorCallback, bouncetime=200)

while True:
    pass
