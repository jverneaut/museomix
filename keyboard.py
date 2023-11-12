import vlc
import curses

instance = vlc.Instance('--no-xlib --quiet')
player = instance.media_list_player_new()

media_list = []

media_list.append('video-1.mp4')
media_list.append('video-2.mp4')
media_list.append('video-3.mp4')
media_list.append('video-4.mp4')

player.set_media_list(instance.media_list_new(media_list))

def on_end_reached(event):
    player.stop()

player.event_manager().event_attach(vlc.EventType.MediaPlayerEndReached, on_end_reached)

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
