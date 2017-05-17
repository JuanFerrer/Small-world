from msvcrt import getch
def listenKey():
	key = ord(getch())
	if key == 27: #ESC
		return "esc"
	if key == 13: #Enter
		return "enter"
	if key == 224: #Special keys (arrows, f keys, ins, del, etc.)
		key = ord(getch())
		if key == 72: #Up arrow
			return "up"
		elif key == 80: #Down arrow
			return "down"
		elif key == 75: #Left arrow
			return "left"
		elif key == 77: #Right arrow
			return "right"
			