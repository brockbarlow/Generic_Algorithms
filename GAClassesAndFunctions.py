#Imports.
import sys 
import random 
import time 

#Classes.
class EvaluateFile(object):
	def __init__(self, file):
		self.expressionList = []
	
		self.ReadFile(file)
		
	def ReadFile(self, fileName):
		dataFile = ""
		dataFile = open(fileName, 'r')
		
		contentsOfFile = dataFile.read()
		
		self.ParseData(contentsOfFile)
		
		dataFile.close()
		
	def ParseData(self, contentsOfFile):
		numberOfAnds = 0
		numberOfOrs = 0
		numberOfNots = 0
		
		numberOfLiterals = 0
		numberOfClauses = 0
		
		lengthOfFile = len(contentsOfFile)
		
		evaluationString = ""
		expressionString = ""
		
		withinClause = "false"
		
		literalList = []
		clauseList = []
		
		for index in range(lengthOfFile):
		
			if contentsOfFile[index] == '(' and withinClause == "false":
				withinClause = "true"
				evaluationString += '('
				
			elif contentsOfFile[index] == ' ':
				continue
				
			elif contentsOfFile[index] == '?' and withinClause == "true":
				evaluationString += '?'
				numberOfNots += 1
			
			elif contentsOfFile[index] == 'V' and withinClause == "true":
				evaluationString += 'V'
				numberOfOrs += 1
				
			elif contentsOfFile[index] == '&':
				evaluationString += '&'
				numberOfAnds += 1
				
			elif contentsOfFile[index] == ')' and withinClause == "true":
				withinClause = "false"
				evaluationString += ')'
				clauseList.append(evaluationString)
				evaluationString = ""
				numberOfClauses += 1
				
			elif contentsOfFile[index] == '\n':
				continue
				
			elif withinClause == "true":
				evaluationString += contentsOfFile[index]
				
				if contentsOfFile[index] in literalList:
					continue
					
				literalList.append(contentsOfFile[index])
				numberOfLiterals += 1
				
		for index in clauseList:
			expressionString += index
			self.expressionList.append(expressionString)
				
		literalList.sort()
		
		self.DisplayResults(numberOfLiterals, literalList, numberOfClauses, clauseList, expressionString, numberOfAnds, numberOfOrs, numberOfNots)
		
	def DisplayResults(self, numberOfLiterals, literalList, numberOfClauses, clauseList, expressionString, numberOfAnds, numberOfOrs, numberOfNots):
		print("The number of literals: ", numberOfLiterals)
		print("\n")
		
		print("The literals: ", literalList)
		print("\n")
		
		print("The number of clauses: ", numberOfClauses)
		
		print("The clauses: ", clauseList)
		print("\n")
		
		print("The expression in the file: ", expressionString)
		print("\n")
		
		print("The number of Ands: ", numberOfAnds)
		print("\n")
		
		print("The number of Ors: ", numberOfOrs)
		print("\n")
		
		print("The number of Nots: ", numberOfNots)
		print("\n")
		
	def GetExpressionList(self):
		return self.expressionList

class CreatePopulation(object):
	def __init__(self, newExpressionString):
		self.currentExpressionString = newExpressionString
		self.oldExpressionString = currentExpressionString
		self.fitnessScore = 0
		self.dictionary = {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1,
						   'g': 1, 'h': 1, 'i': 1, 'j': 1, 'k': 1, 'l': 1,
						   'm': 1, 'n': 1, 'o': 1, 'p': 1, 'q': 1, 'r': 1,
						   's': 1, 't': 1, 'u': 1, 'v': 1, 'w': 1, 'x': 1,
						   'y': 1, 'z': 1}
		
#Functions.