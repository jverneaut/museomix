import vlc
import time

def play_video(file_path):
    # Creating a VLC instance
    instance = vlc.Instance('--no-xlib')

    # Creating a MediaPlayer with the given instance
    player = instance.media_player_new()

    # Creating a Media object
    media = instance.media_new(file_path)

    # Setting the media to the player
    player.set_media(media)

    # Playing the video
    player.play()

    # Waiting for the video to finish
    while player.get_state() != vlc.State.Ended:
        time.sleep(1)

    # Stopping the player
    player.stop()

if __name__ == "__main__":
    # Replace 'path/to/your/video/file.mp4' with the actual path to your video file
    video_path = 'sample-2.mp4'

    play_video(video_path)
