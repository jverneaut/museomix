# import vlc
# import time
# import RPi.GPIO as GPIO

# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


# def play_video(file_path):
#     instance = vlc.Instance('--no-xlib')
#     player = instance.media_player_new()

#     media = instance.media_new(file_path)
#     player.set_media(media)

#     player.play()

#     while player.get_state() != vlc.State.Ended:
#         time.sleep(1)

#     player.stop()

# # if __name__ == "__main__":
# #     video_path = 'sample-2.mp4'

# #     play_video(video_path)

# while True: # Run forever
#     if GPIO.input(10) == GPIO.HIGH:
#         print("Button was pushed!")

import time
import RPi.GPIO as GPIO

# def button_callback(channel):
#     print("Button was pushed!")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(12, GPIO.IN)

# GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback)

# message = input("Press enter to quit\n\n")

# button_pushed = False

while True:
    # print("Listening")
    # print(GPIO.input(10))
    sensor = GPIO.input(10)
    print(sensor)
    # print(f"Sensor State: {sensor}")

    time.sleep(0.4)

    # if GPIO.input(10) == GPIO.HIGH and button_pushed == False:
    #     button_pushed = True
    #     print("Button down")

    # if GPIO.input(10) == GPIO.LOW and button_pushed == True:
    #     button_pushed = False
    #     print("Button up")

    # time.sleep(1)

# GPIO.cleanup()
