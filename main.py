import pyperclip as pc

def to_pitch(text, delimiter):
	pitched = ""
	marked = False
	for character in text:
		if character == delimiter:
			pitched += "__"
			marked = not marked
			continue
		if marked:
			pitched += "＿"
		else:
			pitched += "‎　"
	return pitched

def main():
	text = pc.paste()
	delimiter = "^"
	stripped = text.replace(delimiter, "")
	pc.copy(to_pitch(text, delimiter) + "\n" + stripped)

main()
