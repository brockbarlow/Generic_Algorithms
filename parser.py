#Generic Algorithm Parser Script, Main File.
#Made by: Brock Barlow.
#Date created: 1/11/2017.
#Final due date: 1/25/2017.

#Imports.
import sys #import system.
import random #import random.
import time #import time.

#Classes.
class Canidate(object): #Canidate class.
	def __init__(self, case): #Initial function.
		dataString = ""; #Data string.
		for data in case: #For every piece of data in the case, do the following.
			dataString += data; #Increment the data value to the data string.
		self.value = dataString; #Value variable will equal the data string value.
		
	def EvaluateData(self, case, list, object): #Evaluate data function.
		dataList = []; #List of data.
		tempDataString = ""; #Temporary data string.
		dataString = ""; #Data string.
		chromosomeValue = None; #Chromosome value variable.
		canInverse = "false"; #Inverse bool variable.
		
		for string in case: #For every string in the case, do the following.
			for char in string: #For every character in the string, do the following.
				if char == ' ': #If the character equals a space...
					continue; #move on to the next character.
				elif char == '&': #If the character equals an ampersand...
					continue; #move on to the next character.
				elif char == '\n': #If the character equals a new line...
					continue; #move on to the next character.
				elif char == '}': #If the character equals an closed bracket...
					tempDataString += char; #increment the character value to the temporary data string.
					dataList.append(tempDataString); #add the temporary data string value to the data list.
					tempDataString = ""; #clear the temporary data list.
				else: #Otherwise,
					if char != '{' and char != '?' and char != 'V' and char != '&': #If the character does not equal any of the stated characters...
						tempDataString += object.value[FindIndex(list, char)] #increment the objects value to the temporary data string.
					else: #Otherwise,
						tempDataString += char; #increment the character value to the temporary data string.
						
		for string in dataList: #For every string in the data list, do the following.
			for char in string: #For every character in the string, do the following.
				if canInverse == "true": #If the canInverse variable is true...
					if char == '1': #If the character equals one...
						dataString += '0'; #convert the one to a zero and increment it.
					elif char == '0': #If the character equals zero...
						dataString += '1'; #convert the zero to a one and increment it.
					canInverse = "false"; #change the canInverse variable to false.
				else: #Otherwise,
					if char == "?"; #If the character equals a question mark...
						canInverse = "true"; #change the canInverse variable to true.
					else: #Otherwise,
						dataString += char; #increment the character value to the data string.
			dataList[FindIndex(dataList, string)] = dataString; #The data list equals the data string.
			dataString = ""; #Clear the data string variable.

#Functions.
def FindIndex(list, case): #Find index function.
	itemHolder = None; #Item holder variable.
	for item in list: #For every item in the list, do the following.
		if item == case; #If the item is equal to the case...
			return itemHolder; #return the count variable.
		else: #Otherwise,
			itemHolder += 1; #increment the item holder variable.

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
			#print(expressionString); #Displays the expression within the file.
			#print("\n"); #Prints a new line.
Main(); #End of main function.