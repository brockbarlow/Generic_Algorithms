#python parser script, main file.
#made by: Brock Barlow.
#date created: 1/11/2017.
#final due date: 1/25/2017.

#Imports.
import sys #import system.
import random #import random.
import time #import time.

#Classes.


#Functions.	
def Main(): #Main function.
	#File.
	file = "CNFExpression.txt"; #Name of file. Holds a test cnf expression.
	inFile = open(file, 'r'); #Open and read file.
	
	#Part one: Parser the file and evaluate the data within.
	for string in inFile: #For every string in file, do the following.
		
		if(inFile): #If in the file...
			
			#Lists.
			clauseList = []; #List of clauses in the expression.
			literalList = []; #List of literals in the expression.
			populationList = []; #List of populations.
			
			#Strings.
			evaluationString = ""; #Holds data after evaluating the file.
			expressionString = ""; #Holds the clause(s) of the expression.
			
			#Bools.
			withinClause = "false"; #Bool variable. Used to identify if we're in a clause or not. Starts false.
			
			for char in string: #For each character in the string, do the following.
				
				if char == '{' and withinClause == "false": #If the char equals an open bracket and is not within the clause...
					withinClause = "true"; #turn withinClause to true.
					evaluationString += '{'; #increment the open bracket to the evaluation string.
				
				elif char == ' ': #If the char equals a space...
					continue; #move on to the next character.
				
				elif char == '?' and withinClause == "true": #If the char equals a question mark and is within the clause...
					evaluationString += '?'; #increment the question mark to the evaluation string.
				elif char == 'V' and withinClause == "true": #If the char equals a capital v and is within the clause...
					evaluationString += 'V'; #increment the capital v to the evaluation string.
				
				elif char == '&': #If the char equals an ampersand...
					evaluationString += '&'; #increment the ampersand to the evaluation string.
				
				elif char == '}' and withinClause == "true": #If the char equals a closed bracket and is within the clause...
					withinClause = "false"; #turn withinClause to false.
					evaluationString += '}'; #increment the closed bracket to the evaluation string.
					clauseList.append(evaluationString); #add the data from the evaluation string to the clause list.
					evaluationString = ""; #clear the evaluation string.
				
				elif char == '\n': #If the char equals a new line...
					continue; #move on to the next character.
				
				elif withinClause == "true": #If withinClause is equal to true...
					evaluationString += char; #increment the character to the evaluation string.
					if char in literalList: #If the character is in the literal list...
						continue; #move on.
					literalList.append(char); #otherwise, add the character to the literal list.
			
			for string in clauseList: #For each string in the clause list, do the following.
				expressionString += string; #Increment the string data to the expression string variable.
			
			#Part two: Generate offspring and mutations.
			
			
			#Results.
			#print(literalList); #Displays literals within list.
			#print("\n"); #Prints a new line.
			#print(clauseList); #Displays clauses within list.
			#print("\n"); #Prints a new line.
			print(expressionString); #Displays the expression within the file.
			print("\n"); #Prints a new line.
Main(); #End of main function.