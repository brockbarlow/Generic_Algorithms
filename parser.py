#python parser script, main file.
#made by: Brock Barlow.
#date created: 1/11/2017.
#final due date: 1/25/2017.

#Imports.
import sys #import system.
import random #import random.
			
def Print(list): #Print function. Takes in a list.
	for item in list: #For every item in the list...
		print(item); #print the item.

def Main(): #Main function.
	#Files.
	fileOne = "CNFExpressions.txt"; #Name of file one. Holds cnf expressions.
	fileTwo = "TestCNFExpression.txt"; #Name of file two. Holds a test cnf expression.
	inFileOne = open(fileOne, 'r'); #Open and read file one.
	inFileTwo = open(fileTwo, 'r'); #Open and read file two.
	
	for string in inFileTwo: #For every string in file two, do the following.
		
		if(inFileTwo): #If in the file...
			
			#Lists.
			clauseList = []; #List of clauses in the expression.
			literalList = []; #List of literals in the expression.
			
			#Strings.
			evaluationString = ""; #Holds data after evaluating the file.
			
			#Bools.
			withinClause = "false"; #Bool variable. Used to identify if we're in a clause or not. Starts false.
			
			#Chromosome related variables.
			parentOne = None; #First parent chromosome.
			parentTwo = None; #Second parent chromosome.
			childOne = None; #First child chromosome.
			childTwo = None; #Second child chromosome.
			
			for char in string: #For each character in the string, do the following.
				
				if char == '{' and withinClause == "false": #If the char equals an open bracket and is not within the clause...
					withinClause = "true"; #turn withinClause to true.
				
				elif char == ' ': #If the char equals a space...
					continue; #move on to the next character.
				
				elif char == '?' and withinClause == "true": #If the char equals a question mark and is within the clause...
					evaluationString += '?'; #increment the question mark to the evaluation string.
				elif char == 'V' and withinClause == "true": #If the char equals a capital v and is within the clause...
					evaluationString += 'V'; #increment the capital v to the evaluation string.
				elif char == '&' and withinClause == "true": #If the char equals an ampersand and is within the clause...
					evaluationString += '&'; #increment the ampersand to the evaluation string.
				
				elif char == '}' and withinClause == "true": #If the char equals a closed bracket and is within the clause...
					withinClause = "false"; #turn withinClause to false.
					clauseList.append(evaluationString); #add the data from the evaluation string to the clause list.
					evaluationString = ""; #clear the evaluation string.
				
				elif char == '\n': #If the char equals a new line...
					continue; #move on to the next character.
				
				elif withinClause == "true": #If withinClause is equal to true...
					evaluationString += char; #increment the character to the evaluation string.
					if char in literalList: #If the character is in the literal list...
						continue; #move on.
					literalList.append(char); #otherwise, add the character to the literal list.					
Main(); #End of main function.