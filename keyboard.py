import vlc
import curses

instance = vlc.Instance('--no-xlib --quiet')
player = instance.media_list_player_new()

media_list = []

media_list.append('video-1.mp4')
media_list.append('video-2.mp4')
media_list.append('video-3.mp4')
media_list.append('video-4.mp4')

media_list_instance = instance.media_list_new(media_list)
player.set_media_list(media_list_instance)

# Set the playback mode to not loop
media_list_instance.set_media_player(player.get_media_player())
media_list_instance.set_playback_mode(vlc.PlaybackModeDefault)

def main(stdscr):
    stdscr.keypad(True)

    while True:
        key = stdscr.getch()
        if key == curses.KEY_LEFT:
            player.play_item_at_index(1)
        if key == curses.KEY_UP:
            player.play_item_at_index(2)
        if key == curses.KEY_RIGHT:
            player.play_item_at_index(3)
        if key == curses.KEY_DOWN:
            player.play_item_at_index(0)
        elif key == ord('q'):
            break

if __name__ == "__main__":
    curses.wrapper(main)
