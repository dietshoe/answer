

import random
lottoUserList = []

class LottoUser():


	def __init__(self,firstName,lastName):
		self.firstName=firstName
		self.lastName = lastName
		self.listOfNumbers1Thru5=[]
		self.powerBallNumber = 0

	

	def attemptToAddNumberTo1Thru5List(self,number):
		if number not in self.listOfNumbers1Thru5 and number>=1 and number<=69:
			self.listOfNumbers1Thru5.append(number)
		else:
			return "failure"
	def __str__(self):
		return self.firstName+" "+self.lastName+" "+formatListOfNumbers(self.listOfNumbers1Thru5)+" PowerBall: "+str(self.powerBallNumber)



def formatListOfNumbers(listOfNumbers1Thru5):
	stringToReturn = ""
	for number in listOfNumbers1Thru5:
		stringToReturn+=str(number)+" "
	return stringToReturn


def runLottoProgram():
	
	count = 1
	firstName = raw_input("Enter first name: ")
	lastName = raw_input("Enter last name: ")
	newLottoUser = LottoUser(firstName=firstName,lastName=lastName)


	while(count<7):

		user_input = raw_input("Enter favorite number "+str(count)+": ")
		user_input = int(user_input)
		
		if count!=6:
			if newLottoUser.attemptToAddNumberTo1Thru5List(user_input)=="failure":
				print "failure to add number no duplicates are allowed and number must be 1-69"
			else:
				count+=1
		else:
			if user_input>=1 and user_input<=26:
				newLottoUser.powerBallNumber=user_input
				count+=1
			else:
				print  "failure to add powerball number..number must be 1-26"
	
	lottoUserList.append(newLottoUser)

	if doesUserWantToContinueProgram():
		
		runLottoProgram()
	else:
		endProgram()


def doesUserWantToContinueProgram():
	doesUserWantToContinueProgram = raw_input("Do you want to know the result? (y/n): ")

	if doesUserWantToContinueProgram != "y":
		
		
		return True

		
	else:
		return False

def endProgram():
	displayLottoUsers()
	print calculatePowerballWinningNumbers()


def calculatePowerballWinningNumbers():
	count=1
	finalNumberString = ""

	while(count<7):
		numberDictWithDupCounts = {}

		if count!=6:
			for lottoUser in lottoUserList:
				if lottoUser.listOfNumbers1Thru5[count-1] not in numberDictWithDupCounts:
					numberDictWithDupCounts[lottoUser.listOfNumbers1Thru5[count-1]] = 1
				else:
					numberDictWithDupCounts[lottoUser.listOfNumbers1Thru5[count-1]]= numberDictWithDupCounts[lottoUser.listOfNumbers1Thru5[count-1]]+1
			finalNumberString+=getMax(numberDictWithDupCounts)+" "

		else:
			for lottoUser in lottoUserList:
				if lottoUser.powerBallNumber not in numberDictWithDupCounts:
					numberDictWithDupCounts[lottoUser.powerBallNumber]=1
				else:
					numberDictWithDupCounts[lottoUser.powerBallNumber]= numberDictWithDupCounts[lottoUser.powerBallNumber]+1

			finalNumberString+=" Powerball: "+getMax(numberDictWithDupCounts)
		count+=1
	return finalNumberString


def getMax(numberDictWithDupCounts):
	listOfTiedNumbers = []
	for key, value in numberDictWithDupCounts.iteritems():
		for key,value in numberDictWithDupCounts.iteritems():
			if value == value:
				listOfTiedNumbers.append(key)
	print "printing list of tied values"
	return str(random.choice(listOfTiedNumbers))




def displayLottoUsers():
	for lottoUser in lottoUserList:
		print str(lottoUser)




runLottoProgram()

