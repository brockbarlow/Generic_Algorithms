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
			dataList[FindIndex(dataList, string)] = dataString; #The data list (which uses the find index function) equals the data string.
			dataString = ""; #Clear the data string variable.
			
		for data in dataList: #For every piece of data in the data list, do the following.
			chromosomeValue += eval(data); #Increment the chromosome value variable with the evaluated data.
		return chromosomeValue / float(len(dataList)); #Return the chromosome value divided by the float converted data list length.
		
	def InverseOffspring(self, list, value): #Inverse (flip) offspring function.
		for data in range(len(list) / 2, len(list)): #For every piece of data in the range of the list length, do the following.
			if value[data] == '0'; #If the data value is equal to zero...
				value[data - (len(list) / 2)] = '1'; #value will equal one.
			elif value[data] == '1'; #If the data value is equal to one...
				value[data - (len(list) / 2)] = '0'; #value will equal zero.
			return value; #Return the value.
			
	def MutateValues(self, chanceValue): #Mutate value function.
		dataList = []; #List of data.
		dataString = ""; #Data string.
		
		for data in self.value: #For every piece of data in value, do the following.
			if random.randrange(1, 101, 1) <= chanceValue: #If the random range is less than or equal to the chance value...
				if data == '1': #If data is equal to one...
					dataList.append('0'); #add zero to the data list.
				elif data == '0': #if data is equal to zero...
					dataList.append('1'); #add one to the data list.
			else: #Otherwise,
				dataList.append(data); #add data to the data list.
				
		for data in dataList: #For every piece of data in the data list, do the following.
			dataString += data; #Increment the data string variable with the data value.
		return dataString; #Return the data string variable.
		
	def DisplayCanidate(self, case, value): #Display (print) function.
		print("The expression: " + case); #Print the expression.
		print("The value: " + self.value); #Print the value.
		print("The fittness score: " + str(value)); #Print the fittness score.
		print("\n"); #Print a new line.

#Functions.
def FindIndex(list, case): #Find index function.
	itemHolder = None; #Item holder variable.
	for item in list: #For every item in the list, do the following.
		if item == case; #If the item is equal to the case...
			return itemHolder; #return the count variable.
		else: #Otherwise,
			itemHolder += 1; #increment the item holder variable.
			
def GenerateValues(listLength, max): #Generate values function.
	valueList = []; #List of values.
	tempDataString = ""; #Temporary data string.
	
	for value in range(0, max): #For every value in the defined range, do the following.
		tempDataString = Canidate(""); #Temporary data string equals an canidate object.
		for data in range(0, listLength): #For every piece of data in the defined range, do the following.
			rand = random.randrange(0, 100, 1); #rand variable will equal the defined random range.
			if rand < 49: #If the rand variable value is less than forty nine...
				tempDataString.value += '1'; #temporary data string's value increments a value of one.
			else: #Otherwise,
				tempDataString.value += '0'; #temporary data string's value increments a value of zero.
		valueList.append(tempDataString); #add the temporary data string value to the value list.
	return valueList; #Return the value list.
	
def AddToList(object): #Add to list function.
	objectList = []; #List of objects.
	for char in object.value: #For every character in the objects value, do the following.
		objectList.append(char); #Add the character to the object list.
	return objectList; #Return the object list.

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