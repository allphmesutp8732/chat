lines = []

with open("3.txt", "r", encoding = "utf-8-sig") as f:
	for line in f:
		lines.append(line.strip())
for line in lines:
	s = line.split(" ")
	time = s[0][:5]
	person = s[0][5:]
	text = s[1:]
	word = ""
	for w in text:
		word += w
		
	print("Time:", time)
	print("Speaker:", person)
	print("Text:", word)