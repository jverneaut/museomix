import vlc
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

videos = [
    {'media_path': 'video-1.mp4', 'pin': 11},
    {'media_path': 'video-2.mp4', 'pin': 13},
    {'media_path': 'video-3.mp4', 'pin': 15},
    {'media_path': 'video-4.mp4', 'pin': 16},
]

instance = vlc.Instance('--no-xlib --quiet')
player = instance.media_list_player_new()

media_list = []

for video in videos:
    media_list.append(video['media_path'])

player.set_media_list(instance.media_list_new(media_list))

def sensorCallback(channel):
    if GPIO.input(channel):
        index = 0
        for item in videos:
            if item['pin'] == channel:
                player.play_item_at_index(index)

            index += 1

for video in videos:
    GPIO.setup(video['pin'], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(video['pin'], GPIO.BOTH, callback=sensorCallback, bouncetime=200)

mp = player.get_media_player()
mp.toggle_fullscreen()

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    mp.release()
    GPIO.cleanup()
