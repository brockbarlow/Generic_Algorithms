#Imports.
import sys 
import random 
import time 

#Classes.
class EvaluateFile:
	def __init__(self, file):
		self.ReadFile(file)
		
	def ReadFile(self, fileName):
		dataFile = ""
		dataFile = open(fileName, 'r')
		
		contentsOfFile = dataFile.read()
		
		self.ParserData(contentsOfFile)
		
		dataFile.close()
		
	def ParserData(self, contentsOfFile):
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
			
			elif contentsOfFile[index] == 'V' and withinClause == "true":
				evaluationString += 'V'
				
			elif contentsOfFile[index] == '&':
				evaluationString += '&'
				
			elif contentsOfFile[index] == ')' and withinClause == "true":
				withinClause = "false"
				evaluationString += ')'
				clauseList.append(evaluationString)
				evaluationString = ""
				
			elif contentsOfFile[index] == '\n':
				continue
				
			elif withinClause == "true":
				evaluationString += contentsOfFile[index]
				
				if contentsOfFile[index] in literalList:
					continue
					
				literalList.append(contentsOfFile[index])
				
		for index in clauseList:
			expressionString += index
				
		literalList.sort()
		
	def DisplayResults(self, literalList, clauseList, expressionString):
		print("The literals: ", literalList)
		print("\n")
		
		print("The clauses: ", clauseList)
		print("\n")
		
		print("The expression in the file: ", expressionString)
		print("\n")

#Functions.