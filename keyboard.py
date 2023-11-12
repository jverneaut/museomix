# from pynput import keyboard
import keyboard
import vlc

instance = vlc.Instance('--no-xlib --quiet')
player = instance.media_list_player_new()

media_list = []

media_list.append('video-1.mp4')
media_list.append('video-2.mp4')
media_list.append('video-3.mp4')
media_list.append('video-4.mp4')

player.set_media_list(instance.media_list_new(media_list))

# def on_press(key):
#     if key == keyboard.Key.up:
#         player.play_item_at_index(0)
#     if key == keyboard.Key.down:
#         player.play_item_at_index(1)
#     if key == keyboard.Key.left:
#         player.play_item_at_index(2)
#     if key == keyboard.Key.left:
#         player.play_item_at_index(3)

# with keyboard.Listener(on_press=on_press) as listener:
#     listener.join()

while True:
    if keyboard.read_key() == "w":
        print("You pressed w")
    if keyboard.read_key() == "a":
        print("You pressed a")
    if keyboard.read_key() == "s":
        print("You pressed s")
    if keyboard.read_key() == "d":
        print("You pressed d")
