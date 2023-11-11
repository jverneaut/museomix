import vlc
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

videos = [
    {'media_path': 'sample.mp4', 'pin': 11},
    {'media_path': 'sample-2.mp4', 'pin': 13},
]

instance = vlc.Instance('--no-xlib')
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
                # print('Playing video ' + str(channel))
                # item['player'].play()

            index += 1
    # else:
    #     for item in videos:
    #         if item['pin'] == channel:
    #             # print('Stopping video ' + str(channel))
    #             item['player'].pause()

for video in videos:
    # video['player'] = vlc.MediaPlayer(video['media_path'])
    GPIO.setup(video['pin'], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(video['pin'], GPIO.BOTH, callback=sensorCallback, bouncetime=200)

mp = player.get_media_player()
mp.toggle_fullscreen()

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    mp.release()
    video.stop()
    GPIO.cleanup()
