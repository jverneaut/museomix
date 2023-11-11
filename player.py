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

# import time
# import RPi.GPIO as GPIO

# # def button_callback(channel):
# #     print("Button was pushed!")

# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BOARD)
# # GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(10, GPIO.IN)

# # GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback)

# # message = input("Press enter to quit\n\n")

# # button_pushed = False

# while True:
#     # print("Listening")
#     # print(GPIO.input(10))
#     sensor = GPIO.input(10)
#     print(sensor)
#     # print(f"Sensor State: {sensor}")

#     time.sleep(0.4)

#     # if GPIO.input(10) == GPIO.HIGH and button_pushed == False:
#     #     button_pushed = True
#     #     print("Button down")

#     # if GPIO.input(10) == GPIO.LOW and button_pushed == True:
#     #     button_pushed = False
#     #     print("Button up")

#     # time.sleep(1)

# # GPIO.cleanup()

# Import required libraries
import time
import datetime
import RPi.GPIO as GPIO

def sensorCallback(channel):
  # Called if sensor output changes
  timestamp = time.time()
  stamp = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
  if GPIO.input(channel):
    # No magnet
    print("Sensor HIGH " + stamp)
  else:
    # Magnet
    print("Sensor LOW " + stamp)

def main():
  # Wrap main content in a try block so we can
  # catch the user pressing CTRL-C and run the
  # GPIO cleanup function. This will also prevent
  # the user seeing lots of unnecessary error
  # messages.

  # Get initial reading
  sensorCallback(17)

  try:
    # Loop until users quits with CTRL-C
    while True :
      time.sleep(0.1)

  except KeyboardInterrupt:
    # Reset GPIO settings
    GPIO.cleanup()

# Tell GPIO library to use GPIO references
GPIO.setmode(GPIO.BCM)

print("Setup GPIO pin as input on GPIO17")

# Set Switch GPIO as input
# Pull high by default
GPIO.setup(17 , GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(17, GPIO.BOTH, callback=sensorCallback, bouncetime=200)

if __name__=="__main__":
   main()
