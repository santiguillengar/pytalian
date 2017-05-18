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
				if (not formatVocab(item[1]) in errors):
					errors.append(formatVocab(item[1]))
				vocab.append(item) #add word to the loop again to be redone
			else:
				print("\n    Correct!\n")
				correct = correct + 1 
		else:
			break
	if total != 0:
		print("\nYou answered {} / {} correctly!".format(correct, total))
		if (len(errors) != 0):
			errorString = ""
			for error in errors:
				errorString += error + ", "
			print("You should revise:\n{}.\n\n".format(errorString[:-2]))


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
			italianWord = "\n" + italianWord
			spengWord = "\n" + spengWord
			file.write(italianWord)
			file.write(spengWord)
			if filename != "vocab0.txt":
				file2.write(italianWord)
				file2.write(spengWord)

def testVerbs():
	while (True):
		filename = getVerb()
		if filename == "exit":
			return
		file = open(filename,"r")
		correctVerb = []
		wrongCount = 0
		wrong = []
		people = ["Io", "Tu", "Lui/lei", "Noi", "Voi", "Loro"]

		for line in file: 
			correctVerb.append(line.replace('\n',''))

		print("\n{}".format(filename[:-4]))

		for i in range(len(people)):
			userPerson = raw_input("{}:   ".format(people[i]))
			if formatVocab(userPerson) == "exit" or userPerson == "3":
				file.close()
				return
			if (formatVocab(userPerson) != formatVocab(correctVerb[i])):
				wrongCount += 1
				print("    Wrong! It should be: {}".format(correctVerb[i]))
		if wrongCount == 0:
			print("\n    Perfect!\n")



def getVerb():

	# (!) I must add the four last verbs when I get home and I have my notes for the code to work properly.

	print("\nVERBS:\n")
	print("0.  RANDOM")
	print("1.  ESSERE       11. DIRE")
	print("2.  AVERE        12. LEGGERE")
	print("3.  FARE         13. MANGIARE")
	print("4.  ANDARE       14. VENDERE")
	print("5.  USCIRE       15. PARTIRE")
	print("6.  VENIRE       16. FINIRE")
	print("7.  DARE         17. -")
	print("8.  BERE         18. -")
	print("9.  POTERE       19. -")
	print("10. VOLERE       20. -")
									
	verb = raw_input("What verb do you want?   ")
	verbs = {"0":"RANDOM","1":"ESSERE","2":"AVERE","3":"FARE","4":"ANDARE","5":"USCIRE","6":"VENIRE","7":"DARE",
	"8":"BERE","9":"POTERE","10":"VOLERE","11":"DIRE","12":"LEGGERE","13":"MANGIARE","14":"VENDERE","15":"PARTIRE",
	"16":"FINIRE","17":"-","18":"-","19":"-","20":"-"}
	filename = ""

	while (not(verb in verbs.keys()) and (formatVocab(verb) != "exit")): 
		verb = raw_input("Please choose a valid verb number:   ")
		print(verb)

	if verb == "exit":
		return verb
	
	if verb != "0" and str(verbs.get(verb)) != "-":
		filename = str(verbs.get(verb)) + ".txt"
	if verb == "0":
		randnum = random.randint(1, (len(verbs) -1))
		filename = verbs.get(str(randnum)) + ".txt"
	return filename

		
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
		print("\n                            ***** Main menu *****\n")
		mode = raw_input("To quit press 3 or type \"exit\"\nAre you adding vocab (1) or testing yourself (2)?   ")
		if mode == "1" or mode == "add":
	 		addVocab()
		if mode == "2" or mode == "test":
			testmode = raw_input("Do you want to test yourself on vocab (1) or on verbs (2)?   ")
			if testmode == "1":
				testVocab()
			if testmode == "2":
				testVerbs()
		if mode == "3" or mode == "exit":
			print("\n\nCiao!\n\n")
			quit()


if __name__ == "__main__":
	main()
