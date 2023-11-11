import vlc
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

videos = [
    {'media_path': 'sample.mp4', 'pin': 11},
    {'media_path': 'sample-2.mp4', 'pin': 13},
]

def sensorCallback(channel):
    if GPIO.input(channel):
        for item in videos:
            if item['pin'] == channel:
                item['player'].play()
    else:
        for item in videos:
            if item['pin'] == channel:
                item['player'].play()

for video in videos:
    video['player'] = vlc.MediaPlayer(video['media_path'])

    GPIO.setup(video['pin'], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(video['pin'], GPIO.BOTH, callback=sensorCallback, bouncetime=200)

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    for video in videos:
        video['player'].stop()
    GPIO.cleanup()
