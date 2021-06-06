def remake(text):
	text = text.replace("|", ",")
	text = text.replace('"', "")
	text = text.replace('\t', "")
	text = text.replace(" ","")
	if text[0] == ",":
		return text[1:]
	else:
		return text

def write_file(f_name):
	with open(f"{f_name}.csv", 'a') as file1:
		file1.write(remake(line))
		file1.close()

position = 0
with open('data.csv', 'r') as data:
	for line in data:
		if line[0] != "+":
			if remake(line.strip()) == 'Region,':
				position = 'region'
				continue
			elif remake(line.strip()) == 'Location,':
				position = 'location'
				continue
			elif remake(line.strip()) == 'employees.csv,':
				position = 'employees'
				continue

			if position == 'region':
				write_file("regions")
			elif position == 'location':
				write_file("locations")
			elif position == 'employees':
				write_file("employees")