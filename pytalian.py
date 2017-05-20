import random

def testVocab():

	filename = getUnit()
	if filename == "exit":
		return
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
		translation =raw_input("Italian:   ")
		translation = formatVocab(translation)
		if (translation != "exit" and translation != "-1"):
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
	file.close()


# function used to add new vocabulary to system.
def addVocab():

	filename = getUnit()
	if filename == "exit":
		return
	file = open(filename,"a") #opens file with name of "vocab.txt"
	if filename != "vocab0.txt":
		file2 = open("vocab0.txt","a")
	
	while True:
		italianWord = raw_input("\nInsert italian vocab:   ")
		if italianWord == "exit" or italianWord == "-1":
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

def testVerbsPresent():

	while (True):
		filename = getVerb()
		if filename == "exit":
			return
		file = open(filename,"r") #opens file with name of "vocab.txt"
			
		correctVerb = []
		wrongCount = 0
		wrong = []
		people = ["Io", "Tu", "Lui/lei", "Noi", "Voi", "Loro"]

		for line in file: 
			correctVerb.append(line.replace('\n',''))

		print("\n{}".format(filename[:-4]))

		for i in range(len(people)):
			userPerson = raw_input("{}:   ".format(people[i]))
			if formatVocab(userPerson) == "exit" or userPerson == "-1":
				file.close()
				return
			if (formatVocab(userPerson) != formatVocab(correctVerb[i])):
				wrongCount += 1
				print("    Wrong! It should be: {}".format(correctVerb[i]))

		if wrongCount == 0:
			print("\n                                    Perfect!\n")
		else:
			print("                              You made {} mistakes!".format(wrongCount))
		file.close()


def testVerbsPP():

	filename = "passatoprossimo.txt"
	file = open(filename,"r")
	
	# PREPARATION OF VOCAB
	messList = [] 
	errors = []
	correct = 0
	total = 0
	for line in file:
		messList.append(line)
	italian = []
	speng = []
	speng = [i.replace('\n','') for i in messList[::2]] #even elements, zero indexed
	italian = [i.replace('\n','') for i in messList[1::2]] #odd elements, zero indexed
	verbs = zip(italian, speng)
	
	
	random.shuffle(verbs)
	for item in verbs:
		print(item[0])
		translation = raw_input("Italian:   ")
		translation = formatVocab(translation)
		if (translation != "exit" and translation != "-1"):
			total = total +1
			if translation != formatVocab(item[1]):
				print("\n    Nah: {}\n".format(item[1]))
				if (not formatVocab(item[1]) in errors):
					errors.append(formatVocab(item[1]))
				verbs.append(item) #add word to the loop again to be redone
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
	file.close()


def testGrammar():

	filename = "grammar.txt"
	file = open(filename,"r")
	
	# PREPARATION OF VOCAB
	messList = [] 
	errors = []
	correct = 0
	total = 0
	for line in file:
		messList.append(line)
	italian = []
	speng = []
	speng = [i.replace('\n','') for i in messList[::2]] #even elements, zero indexed
	italian = [i.replace('\n','') for i in messList[1::2]] #odd elements, zero indexed
	grammar = zip(italian, speng)
	
	
	random.shuffle(grammar)
	for item in grammar:
		print(item[0])
		translation = raw_input("Italian:   ")
		translation = formatVocab(translation)
		if (translation != "exit" and translation != "-1"):
			total = total +1
			if translation != formatVocab(item[1]):
				print("\n    Nah: {}\n".format(item[1]))
				if (not formatVocab(item[1]) in errors):
					errors.append(formatVocab(item[1]))
				grammar.append(item) #add word to the loop again to be redone
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
	file.close()


def getVerb():

	print("\nVERBS:\n")
	print("0.  RANDOM")
	print("1.  ESSERE       11. DIRE           21. APRIRE")
	print("2.  AVERE        12. LEGGERE        22. ALZARSI")
	print("3.  FARE         13. MANGIARE       23. TORNARE")
	print("4.  ANDARE       14. VENDERE")
	print("5.  USCIRE       15. PARTIRE")
	print("6.  VENIRE       16. FINIRE")
	print("7.  DARE         17. CHIAMARSI")
	print("8.  BERE         18. PREFERIRE")
	print("9.  POTERE       19. STARNUTIRE")
	print("10. VOLERE       20. CHIUDERE")
									
	verb = raw_input("What verb do you want?   ")
	verbs = {"0":"RANDOM","1":"ESSERE","2":"AVERE","3":"FARE","4":"ANDARE","5":"USCIRE","6":"VENIRE","7":"DARE",
	"8":"BERE","9":"POTERE","10":"VOLERE","11":"DIRE","12":"LEGGERE","13":"MANGIARE","14":"VENDERE","15":"PARTIRE",
	"16":"FINIRE","17":"CHIAMARSI","18":"PREFERIRE","19":"STARNUTIRE","20":"CHIUDERE", "21":"APRIRE", "22":"ALZARSI",
	"23":"TORNARE"}


	while (not(verb in verbs.keys()) and (formatVocab(verb) != "exit") and (formatVocab(verb) != "-1") ): 
		verb = raw_input("Please choose a valid verb number:   ")
		print(verb)

	if verb == "exit" or verb == "-1":
		filename = "exit"
	else:
		if verb == "0":
			randnum = random.randint(1, (len(verbs) -1))
			filename = verbs.get(str(randnum)) + ".txt"
		else:
			filename = str(verbs.get(verb)) + ".txt"
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
									
	unit = raw_input("What unit do you want to add vocab to?   ")
	units = ["0","1","2","3","4","5","6","7","8","9","10"]
	filename = "vocab0.txt"

	print("\n")

	if unit in units:
		filename = "vocab" + unit + ".txt"
	if unit == "exit":
		filename = "exit"
	return filename

def translate():
	print("\nTRANSLATION")
	lang = raw_input("Is your word in italian (1) or in english (2)?   ")
	while (lang != "1" and lang!="2" and lang !="-1" and lang!= "exit"): 
		lang = raw_input("Please select language of your word: italian (1) or english (2):   ")
	if lang == "-1" or lang == "exit":
		return

	word = raw_input("Insert word to translate:   ")

	filename = "vocab0.txt"
	file = open(filename,"r") #opens file with name of "vocab.txt"
	
	
	# PREPARATION OF VOCAB
	messList = [] 
	italian = []
	speng = []

	for line in file:
		messList.append(line)

	italian = [i.replace('\n','') for i in messList[::2]] #even elements, zero indexed
	speng = [i.replace('\n','') for i in messList[1::2]] #odd elements, zero indexed

	for item in speng:
		formatVocab(item)
	for item in italian:
		formatVocab(item)

	if (lang == "1"):
		if(not(formatVocab(word) in italian)):
			print("Error: {} not found in system!\n".format(word))
		else:
			print("Translation: {}\n".format(speng[italian.index(word)]))

	else:
		if(not(formatVocab(word) in speng)):
			print("Error: {} not found in system!\n".format(word))
		else:
			print("Translation: {}\n".format(italian[speng.index(word)]))

	file.close()



def formatVocab(vocab):
	if (vocab.endswith(" ")): 
		vocab = vocab[:-1]
	return vocab.lower()

def main():
	print("UoE Foundation Italian 1 revision tool\nMay 2017, @SantiGuillenGar\n")
	while True:
		print("\n                            ***** Main menu *****\n")
		mode = raw_input("To quit type \"-1\" or type \"exit\"\nAre you adding vocab (1), testing yourself (2) or translating something (3)?   ")
		if mode == "1" or mode == "add":
	 		addVocab()
		if mode == "2" or mode == "test":
			testmode = raw_input("Do you want to test yourself on vocab (1), on verbs (2) or on grammar (3)?   ")
			if testmode == "1":
				testVocab()
			if testmode == "2":
				verbmode = raw_input("Present (1) or passato prossimo (2)?   ")
				if verbmode == "1": 
					testVerbsPresent()
				if verbmode == "2":
					testVerbsPP()
				if verbmode == "-1" or verbmode == "exit":
					mode == "-1"
				else:
					print("Error: That verb tense is not available!") 
			if testmode == "3":
				testGrammar()
		if mode == "3" or mode == "translate":
			translate()
		if mode == "-1" or mode == "exit":
			print("\n\nCiao!\n\n")
			quit()



if __name__ == "__main__":
	main()
