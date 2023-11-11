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

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
def button_callback(channel):
    print("Button was pushed!")
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge
message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up
