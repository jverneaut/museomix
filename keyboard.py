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

def main(stdscr):
    # Set the cursor to invisible
    curses.curs_set(0)

    # Enable keypad input
    stdscr.keypad(True)

    stdscr.addstr(0, 0, "Press the left arrow key (q to quit)")

    while True:
        key = stdscr.getch()
        if key == curses.KEY_LEFT:
            stdscr.addstr(2, 0, "Left arrow key pressed")
        elif key == ord('q'):
            break

if __name__ == "__main__":
    curses.wrapper(main)
