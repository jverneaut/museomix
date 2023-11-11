import vlc

def play_video(name):
    player = vlc.MediaPlayer(name)
    player.play()

play_video('sample.mp4')
