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
		if (translation != "exit"):
			total = total +1
			if translation != formatVocab(item[1]):
				print("\nNah: {}".format(item[1]))
			else:
				print("\nCorrect!\n")
				correct = correct + 1 
		else:
			if total != 0:
				print("\nYou answered {} / {} correctly!".format(correct, total))
			main()


# function used to add new vocabulary to system.
def addVocab():

	filename = getUnit()
	file = open(filename,"a") #opens file with name of "vocab.txt"
	if filename != "vocab11.txt":
		file2 = open("vocab11.txt","a")
	
	while True:
		italianWord = raw_input("\nInsert italian vocab:   ")
		if italianWord == "exit":
			file.close()
			if filename != "vocab11.txt":
				file2.close()
			return 
		else: 
			spengWord = raw_input("Insert translation:   ")
			italianWord+="\n"
			spengWord+="\n"
			file.write(italianWord)
			file.write(spengWord)
			if filename != "vocab11.txt":
				file2.write(italianWord)
				file2.write(spengWord)
		
def getUnit():

	print("\nUNITS:")
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
	print("11. Random")
									
	unit = raw_input("What unit do you want?   ")
	units = ["1","2","3","4","5","6","7","8","9","10","11"]
	filename = "vocab11.txt"

	if unit in units:
		filename = "vocab" + unit + ".txt"

	return filename

def formatVocab(vocab):
	if (vocab.endswith(" ")): 
		vocab = vocab[:-1]
	return vocab.lower()

def main():
	while True:
		print("\n***** Hi! *****")
		mode = raw_input("Are you adding vocab (1) or testing yourself (2)? \nTo quit press 3 or type \"exit\"   ")
		if mode == "1" or mode == "add":
	 		addVocab()
		if mode == "2" or mode == "test":
			testVocab()
		if mode == "3" or mode == "exit":
			print("\n\nCiao!\n\n")
			quit()


if __name__ == "__main__":
	main()
