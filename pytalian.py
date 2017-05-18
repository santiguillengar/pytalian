import random

def testVocab():

	input_func = None
	try:
		input_func = raw_input
	except NameError:
		input_func = input

	filename = getUnit()
	file = open(filename,"r") #opens file with name of "vocab.txt"
	
	
	# PREPARATION OF VOCAB
	messList = [] 
	errors = []
	translation = ""
	item = ()
	correct = 0
	total = 0
	for line in file:
		messList.append(line)
	italian = []
	speng = []
	speng = [i.replace('\n','') for i in messList[::2]] #even elements, zero indexed
	italian = [i.replace('\n','') for i in messList[1::2]] #odd elements, zero indexed
	vocab = zip(italian, speng)
	
	
	random.shuffle(vocab)
	for item in vocab:
		print(item[0])
		translation = input_func("Italian:   ")
		translation = formatVocab(translation)
		if (translation != "exit" and translation != "3"):
			total = total +1
			if translation != formatVocab(item[1]):
				print("\n    Nah: {}\n".format(item[1]))
				errors.append(formatVocab(item[1]))
			else:
				print("\n    Correct!\n")
				correct = correct + 1 
		else:
			if total != 0:
				print("\nYou answered {} / {} correctly!".format(correct, total))
				errorString = ""
				for error in errors:
					errorString += error + ", "
				print("You should revise:\n{}.\n\n".format(errorString[:-2]))
			main()


# function used to add new vocabulary to system.
def addVocab():

	filename = getUnit()
	file = open(filename,"a") #opens file with name of "vocab.txt"
	if filename != "vocab0.txt":
		file2 = open("vocab0.txt","a")
	
	while True:
		italianWord = raw_input("\nInsert italian vocab:   ")
		if italianWord == "exit" or italianWord == "3":
			file.close()
			if filename != "vocab0.txt":
				file2.close()
			return 
		else: 
			spengWord = raw_input("Insert translation:   ")
			italianWord+="\n"
			spengWord+="\n"
			file.write(italianWord)
			file.write(spengWord)
			if filename != "vocab0.txt":
				file2.write(italianWord)
				file2.write(spengWord)
		
def getUnit():

	print("\nUNITS:")
	print("0. Random")
	print("1. Come ti chiami?")
	print("2. Al lavoro e in famiglia")
	print("3. Una giornata tipica")
	print("4. Il tempo libero")
	print("5. Al bar")
	print("6. A casa")
	print("7. In citta")
	print("8. Ti va di...?")
	print("9. Cosa hai fatto ieri?")
	print("10. Ieri, oggi, domani")
									
	unit = raw_input("What unit do you want?   ")
	units = ["0","1","2","3","4","5","6","7","8","9","10"]
	filename = "vocab0.txt"

	print("\n")

	if unit in units:
		filename = "vocab" + unit + ".txt"

	return filename

def formatVocab(vocab):
	if (vocab.endswith(" ")): 
		vocab = vocab[:-1]
	return vocab.lower()

def main():
	print("UoE Foundation Italian 1 revision tool\nMay 2017, @SantiGuillenGar\n")
	while True:
		print("\n                               ***** Ciao *****\n")
		mode = raw_input("To quit press 3 or type \"exit\"\nAre you adding vocab (1) or testing yourself (2)?   ")
		if mode == "1" or mode == "add":
	 		addVocab()
		if mode == "2" or mode == "test":
			testVocab()
		if mode == "3" or mode == "exit":
			print("\n\nCiao!\n\n")
			quit()
		else:
			print("\nError: option not available!")


if __name__ == "__main__":
	main()
