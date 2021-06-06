def remake(text):
	text = text.replace("|", ",")
	text = text.replace('"', "")
	text = text.replace('\t', "")
	text = text.replace(" ","")
	if text[0] == ",":
		return text[1:]
	else:
		return text


with open('data.csv', 'r') as data:
	for line in data:
		if line[0] != "+":
			with open("new.csv", 'a') as file2:
				if len(line)>2:
					file2.write(remake(line))
					file2.close()
				else:
					file2.write(remake(line))
					file2.close()
