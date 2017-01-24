#Generic Algorithm Parser Script, Constructor File.
#Made by: Brock Barlow.
#Date created: 1/24/2017.
#Final due date: 1/25/2017.

#Imports.
import sys #import system.
import random #import random.
import time #import time.

#Classes.
class Candidate(object):
	def __init__(self, string):
		dataString = ""
		for data in string:
			dataString += data
		self.value = dataString
		
	def InverseFrontOffspring(self, literalList, value):
		for data in range(len(literalList) / 2, len(literalList)):
			if value[data] == '0':
				value[data - (len(literalList) / 2)] = '1'
			elif value[data] == '1':
				value[data - (len(literalList) / 2)] = '0'
		return value
		
	def DataEvaluation(self, expressionString, literalList, can):
		tempString = ""
		finalString = ""
		canInverse = 0
		clauseList = []
		chromosomeValue = 0
		
		for string in expressionString:
			for char in string:
				if char == ")":
					tempString += char
					clauseList.append(tempString)
					tempString = ""
				elif char == '&':
					continue
				else:
					if char != '?' and char != '(' and char != 'V' and char != '&':
						tempString += can.value[FindIndex(literalList, char)]
					else:
						tempString += char
						
		for string in clauseList:
			for char in string:
				if canInverse == 1:
					if char == '1':
						finalString += '0'
					elif char == '0':
						finalString += '1'
					canInverse = 0
				else:
					if char == '?':
						canInverse = 1
					else:
						finalString += char
			clauseList[FindIndex(clauseList, string)] = finalString
			finalString = ""
			
		for clause in clauseList:
			chromosomeValue += eval(clause)
		return chromosomeValue / float(len(clauseList))
		
	def MutateValues(self, chanceValue):
		finalList = []
		dataString = ""
		
		for data in self.value:
			if random.randrange(1, 101, 1) <= chanceValue:
				if data == '1':
					finalList.append('0')
				elif data == '0':
					finalList.append('1')
			else:
				finalList.append(data)
		
		for data in finalList:
			dataString += data
		return dataString
		
	def DisplayResults(self, expressionString, fittness):
		print("Expression: " + expressionString)
		print("Value: " + self.value)
		print("Fittness: " + fittness)
		print("\n")

#Functions.
def FindIndex(listVariable, caseVariable):
	int = 0
	for item in listVariable:
		if item == caseVariable:
			return int
		else:
			int += 1

def GenerateValues(literalListsLength, max):
	valuesList = []
	
	for value in range(0, max):
		tempDataString = Candidate("")
		for data in range(0, literalListsLength):
			rand = random.randrange(0, 100, 1)
			if rand < 49:
				tempDataString.value += '1'
			else:
				tempDataString.value += '0'
		valuesList.append(tempDataString)
	return valuesList
			
def AddCandidateToList(can): 
	tempList = [] 
	
	for char in can.value: 
		tempList.append(char)
	return tempList