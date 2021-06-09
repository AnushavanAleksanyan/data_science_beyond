import re


def remake(text):
	#text = text.replace("|", ",")
	#text = text.replace('"', "")
	#text = text.replace('\t', "")
	if text[0] != " ":
		text = re.sub('  +', ',', text)
	else:
		text = re.sub('  +', ',', text[4:])
	return text

def write_file(f_name):
	with open(f"{f_name}.csv", 'a') as file1:
		file1.write(remake(line))
		file1.close()

position = 0
with open('data copy.csv', 'r') as data:
	for line in data:
		if line == "Ex1,2 3 4\n":
			position = 'school'
			continue
		elif line == 'Ex5.\n':
			position = 'restourant'
			continue

		if position == 'school':
			write_file("school")
		elif position == 'restourant':
			write_file("restourant")