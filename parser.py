#Generic Algorithm Parser Script, Main File.
#Made by: Brock Barlow.
#Date created: 1/11/2017.
#Final due date: 2/1/2017.

#Imports.
import constructor
from constructor import *

#Functions.
def Main(): 
	file = "CNFExpression.txt" 
	inFile = open(file, 'r') 
	
	#Lists.
	literalList = [] 
	clauseList = [] 
	populationList = []
	newPopulationList = []
	breedList = []
			
	#Strings.
	evaluationString = "" #Holds data after evaluating the file. Used in part one.
	expressionString = "" #Holds the clause(s) of the expression. Used in part two and at the end of part one.
			
	#Bools.
	withinClause = "false" 
	isActive = "true"
			
	#Data holders.
	foundSolution = 0
	solution = None
	generation = 0
	
	#Part one: Parser the file and evaluate the data within.
	for string in inFile: 
		
		if inFile: 
			
			for char in string: 
				
				if char == '(' and withinClause == "false": 
					withinClause = "true" 
					evaluationString += '(' 
				
				elif char == ' ': 
					continue 
				
				elif char == '?' and withinClause == "true": 
					evaluationString += '?' 
				
				elif char == 'V' and withinClause == "true": 
					evaluationString += 'V' 
				
				elif char == '&': 
					evaluationString += '&' 
				
				elif char == ')' and withinClause == "true": 
					withinClause = "false" 
					evaluationString += ')' 
					clauseList.append(evaluationString) 
					evaluationString = "" 
				
				elif char == '\n': 
					continue 
				
				elif withinClause == "true": 
					evaluationString += char 
					
					if char in literalList: 
						continue 
						
					literalList.append(char) 
			
			for string in clauseList: 
				expressionString += string 
			
			literalList.sort()
			
			#Part two: Generate offspring and mutations.
			populationList = GenerateRandomValues(len(literalList), 16)
			
			while(foundSolution == 0):
				generation += 1
				
				for can in populationList:
					
					if can.DataEvaluation(expressionString, literalList, can) >= 1:
						print(can.DataEvaluation(expressionString, literalList, can))
						solution = can
						foundSolution = 1
						break
					
				for can in populationList:
					breedList.append(can)
					
				for parent in range(0, 4):
					
					parentOne = breedList[parent]
					parentTwo = Candidate("")
					
					while isActive == "true":
						parentTwo = breedList[random.randrange(parent, len(breedList))]
						
						if parentTwo in breedList:
							isActive = "false"
							
					#childOne = Candidate(parentTwo.InverseFrontOffspring(literalList, AddCandidateToList(parentTwo)))
					#childTwo = Candidate(parentOne.InverseFrontOffspring(literalList, AddCandidateToList(parentOne)))
					#newPopulationList.append(childOne)
					#newPopulationList.append(childTwo)
			
			#Results.
			print("The literals: ", literalList) #Displays literals within list.
			print("\n") #Prints a new line.
			print("The clauses: ", clauseList) #Displays clauses within list.
			print("\n") #Prints a new line.
			print("The expression in the file: ", expressionString) #Displays the expression within the file.
			print("\n") #Prints a new line.
Main() 