import curses
import curses.textpad as textpad

def cursescli(stdscr):
    #stdscr.immedok(True)
    #stdscr.border(0)
    stdscr.refresh()
    dims = stdscr.getmaxyx()
    history = curses.newwin(dims[0]*4/5, dims[1]*3/4, 0,0)
    history.immedok(True)
    history.box()
    history.addstr(1,1, "Chat history:")

    names = curses.newwin(dims[0]*4/5, dims[1]/4, 0, dims[1]*3/4)
    names.immedok(True)
    names.box()
    names.addstr(1,1,"Users:")

    text = curses.newwin(dims[0]/5, dims[1], dims[0]*4/5, 0)
    text.immedok(True)
    text.box()
    text.addstr(1,1, "Input:")
    curses.noecho()
    textbox = textpad.Textbox(text, insert_mode = True)
    text_input = textbox.edit()
    names.addstr(2,1, text_input.encode('utf-8'))
    stdscr.getch()
    curses.endwin()

if __name__ == '__main__':
    curses.wrapper(cursescli)
