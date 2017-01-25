#Generic Algorithm Parser Script, Constructor File.
#Made by: Brock Barlow.
#Date created: 1/24/2017.
#Final due date: 2/1/2017.

#Imports.
import sys 
import random 
import time 

#Classes.
class Candidate(object):
	def __init__(self, string): #Initialize values.
		dataString = ""
		
		for data in string:
			dataString += data
			
		self.value = dataString
		
	def DataEvaluation(self, variableChar, variableList, can): #Evaluate the data.
		valueList = []
		tempDataString = ""
		finalDataString = ""
		canInverse = "false"
		chromosomeValue = 0
		
		for string in variableChar:
		
			for char in string:
			
				if char == ")":
					tempDataString += char
					valueList.append(tempDataString)
					tempDataString = ""
					
				elif char == '&':
					continue
					
				elif char == ' ':
					continue
					
				elif char == '\n':
					continue
					
				else:
				
					if char != '?' and char != '(' and char != 'V' and char != '&':
						tempDataString += can.value[FindValueIndex(variableList, char)]
						
					else:
						tempDataString += char
						
		for string in valueList:
		
			for char in string:
			
				if canInverse == "true":
				
					if char == '1':
						finalDataString += '0'
						
					elif char == '0':
						finalDataString += '1'
						
					canInverse = "false"
					
				else:
				
					if char == '?':
						canInverse = "true"
						
					else:
						finalDataString += char
						
			valueList[FindValueIndex(valueList, string)] = finalDataString
			finalDataString = ""
			
		for value in valueList:
		
			chromosomeValue += eval(value)
			
		return chromosomeValue / float(len(valueList))
		
	def InverseFrontOffspring(self, variableList, dataValue): #Inverse the front part of the offspring.
		for data in range(len(variableList) / 2, len(variableList)):
		
			if dataValue[data] == '0':
				dataValue[data - (len(variableList) / 2)] = '1'
				
			elif dataValue[data] == '1':
				dataValue[data - (len(variableList) / 2)] = '0'
				
		return dataValue
		
	def MutateValues(self, chanceValue): #Mutate the values.
		finalDataList = []
		dataString = ""
		
		for data in self.value:
		
			if random.randrange(1, 101, 1) <= chanceValue:
			
				if data == '1':
					finalDataList.append('0')
					
				elif data == '0':
					finalDataList.append('1')
					
			else:
			
				finalDataList.append(data)
		
		for data in finalDataList:
		
			dataString += data
			
		return dataString
		
	def DisplayResults(self, expressionString, fittness): #Display the results to the user.
		print("Expression: " + expressionString)
		print("Value: " + self.value)
		print("Fittness: " + fittness)
		print("\n")

#Functions.
def FindValueIndex(variableList, variableChar): #Find the index of the value(s).
	intDataHolder = 0
	
	for item in variableList:
		
		if item == variableChar:
			return intDataHolder
		
		else:
			intDataHolder += 1

def GenerateRandomValues(variableListLength, maxValue): #Generate random values to use.
	valueList = []
	
	for value in range(0, maxValue):
		tempDataString = Candidate("")
		
		for data in range(0, variableListLength):
			rand = random.randrange(0, 100, 1)
			
			if rand < 49:
				tempDataString.value += '1'
			
			else:
				tempDataString.value += '0'
				
		valueList.append(tempDataString)
		
	return valueList
			
def AddCandidateToList(can): #Add the candidate to the list.
	canList = [] 
	
	for char in can.value: 
		canList.append(char)
		
	return canList