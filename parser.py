#Generic Algorithm Parser Script, Main File.
#Made by: Brock Barlow.
#Date created: 1/11/2017.
#Final due date: 2/1/2017.

#Imports.
import constructor
from constructor import *

def Main(): #Main function.
	#File.
	file = "CNFExpression.txt" #Name of file. Holds a test cnf expression.
	inFile = open(file, 'r') #Open and read file.
	
	#Part one: Parser the file and evaluate the data within.
	for string in inFile: #For every string in file, do the following.
		
		if inFile: #If in the file...
			
			#Lists.
			literalList = [] #List of literals in the expression.
			clauseList = [] #List of clauses in the expression.
			populationList = []
			breedList = []
			newPopulationList = []
			finalPopulationList = []
			
			#Strings.
			evaluationString = "" #Holds data after evaluating the file.
			expressionString = "" #Holds the clause(s) of the expression.
			
			#Bools.
			withinClause = "false" #Used to identify if we're in a clause or not. Starts false.
			active = "true"
			
			#Data holders.
			foundSolution = 0
			solution = None
			generation = 0
			populationCounter = 0
			
			for char in string: #For each character in the string, do the following.
				
				if char == '(' and withinClause == "false": #If the char equals an open bracket and is not within the clause...
					withinClause = "true" #turn withinClause to true.
					evaluationString += '(' #increment the open bracket to the evaluation string.
				
				elif char == ' ': #If the char equals a space...
					continue #move on to the next character.
				
				elif char == '?' and withinClause == "true": #If the char equals a question mark and is within the clause...
					evaluationString += '?' #increment the question mark to the evaluation string.
				elif char == 'V' and withinClause == "true": #If the char equals a capital v and is within the clause...
					evaluationString += 'V' #increment the capital v to the evaluation string.
				
				elif char == '&': #If the char equals an ampersand...
					evaluationString += '&' #increment the ampersand to the evaluation string.
				
				elif char == ')' and withinClause == "true": #If the char equals a closed bracket and is within the clause...
					withinClause = "false" #turn withinClause to false.
					evaluationString += ')' #increment the closed bracket to the evaluation string.
					clauseList.append(evaluationString) #add the data from the evaluation string to the clause list.
					evaluationString = "" #clear the evaluation string.
				
				elif char == '\n': #If the char equals a new line...
					continue #move on to the next character.
				
				elif withinClause == "true": #If withinClause is equal to true...
					evaluationString += char #increment the character to the evaluation string.
					if char in literalList: #If the character is in the literal list...
						continue #move on.
					literalList.append(char) #otherwise, add the character to the literal list.
			
			for string in clauseList: #For each string in the clause list, do the following.
				expressionString += string #Increment the string data to the expression string variable.
			
			#Part two: Generate offspring and mutations.
			populationList = GenerateValues(len(literalList), 16)
			
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
					while active == "true":
						parentTwo = breedList[random.randrange(parent, len(breedList))]
						if parentTwo in breedList:
							active = "false"
					childOne = Candidate(parentTwo.InverseFrontOffspring(literalList, AddCandidateToList(parentTwo)))
					childTwo = Candidate(parentOne.InverseFrontOffspring(literalList, AddCandidateToList(parentOne)))
					newPopulationList.append(childOne)
					newPopulationList.append(childTwo)
					if parentOne in breedList:
						breedList.remove(parentOne)
					if parentTwo in breedList:
						breedList.remove(parentTwo)
					for can in newPopulationList:
						dataString = ""
						for data in can.value:
							dataString += data
						can.value = dataString
						
				for newCan in newPopulationList:
					newCan.value = newCan.MutateValues(25)
					populationList.append(newCan)
					
				for can in populationList:
					if len(finalPopulation) < 10:
						finalPopulation.append(can)
					else:
						for check in finalPopulation:
							if can.DataEvaluation(expressionString, literalList, can) > check.DataEvaluation(clauseList, literalList, check):
								check = can
				populationList = finalPopulation
				for p in populationList:
					p.DisplayResults(expressionString, p.DataEvaluation(expressionString, literalList, p))
								
			print("Solution: " + solution.value)
			print("Generation: " + str(generation))
			
			#Results.
			#print(literalList) #Displays literals within list.
			#print("\n") #Prints a new line.
			#print(clauseList) #Displays clauses within list.
			#print("\n") #Prints a new line.
			#print(expressionString) #Displays the expression within the file.
			#print("\n") #Prints a new line.
Main() #End of main function.