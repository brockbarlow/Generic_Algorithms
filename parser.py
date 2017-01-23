#python parser script, main file.
#made by: Brock Barlow.
#date created: 1/11/2017.
#final due date: 1/25/2017.

#Imports.
import sys #import system.
import random #import random.

#Classes.
class Canidate(object):
	def __init__(self, string):
		#Strings.
		bitString = "";
		
		for bit in string:
			bitString += bit;
		self.value = bitString;
		
	def EvaluateData(self, clauseList, literalList, value):
		#Strings.
		tempString = "";
		printString = "";
		finalString = "";
		
		#Bools.
		inverse = "false";
		
		#Data holders.
		chromosomeValue = None;
		
		for string in clauseList:
			
			for char in string:
				
				if char == '?':
					tempString += '?';
				elif char == '&':
					tempString += '&';
				elif char == 'V':
					tempString += 'V';
				
				else:
					index = FindIndex(literalList, char);
					tempString += str(value.value[index]);
			
			for char in tempString:
				
				if inverse == "true":
					
					if char == '1':
						finalString += str(0);
					elif char == '0':
						finalString += str(1);
					inverse = "false";
				
				elif char == '?' and inverse == "false":
					inverse = "true";
				
				else:
					finalString += char;
			
			chromosomeValue += (eval(finalString));
			printString += finalString;
			tempString = "";
			finalString = "";
		
		print(printString);
		return chromosomeValue / len(literalList);
		
	def InverseOffspring(self, literalList, value):
		for bit in range(len(literalList) / 2, len(literalList)):
			
			if value[bit] == '0':
				value[bit - (len(literalList) / 2)] = '1';
			elif value[bit] == '1':
				value[bit - (len(literalList) / 2)] = '0';
		
		return value;
		
	def MutateValues(self, chancevalue):
		#Lists.
		finalList = [];
		
		#Strings.
		bitString = "";
		
		for bit in self.value:
			
			if random.randrange(1, 101, 1) <= chancevalue:
				
				if bit == '1':
					finalList.append('0');
				elif bit == '0':
					finalList.append('1');
			
			else:
				finalList.append(bit);
		
		for bit in finalList:
			bitString += bit;
		return bitString;
		
#Functions.
def FindIndex(list, case): #Find index function. Takes in a list and case.
	counter = 0; #Count variable.
	for item in list: #For every item in the list...
		if item == case: #If the item is equal to the case...
			return counter; #return the count variable.
		else: #Otherwise,
			counter += 1; #increment the count variable.
			
def GenerateValues(itemLength): #Generate values function. Takes in the length of an item.
	valueList = []; #Value list.
	for value in range(0, 4):
		tempString = Canidate("");
		for bit in range(0, itemLength):
			rand = random.randrange(0, 100, 1);
			if rand < 49:
				tempString.value += '1';
			else:
				tempString.value += '0';
		valueList.append(tempString);
	return valueList;
			
def AddToList(item): #Add to list function. Takes in an item.
	list = []; #List of items.
	for char in item.value: #For every character in items value...
		list.append(char); #add the character to the list.
	return list; #Otherwise, just return the list.
			
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
			populationList = []; #List of populations.
			newPopulationList = []; #List of new populations.
			finalPopulationList = []; #List of final populations.
			breedableList = []; #List of breedable chromosomes.
			
			#Strings.
			evaluationString = ""; #Holds data after evaluating the file.
			bitString = ""; #Bit string variable.
			
			#Bools.
			withinClause = "false"; #Bool variable. Used to identify if we're in a clause or not. Starts false.
			active = "true"; #Active variable. Starts true. If the second parent is within the breedable list, this variable will be false.
			foundSolution = "false"; #Found solution variable. Starts false. When a solution is found, the variable will become true.
			
			#Chromosome related variables.
			parentOne = None; #First parent chromosome.
			parentTwo = None; #Second parent chromosome.
			childOne = None; #First child chromosome.
			childTwo = None; #Second child chromosome.
			
			#Data holders.
			solution = None; #Solution variable. At start, equals nothing. Will be used to hold the canidate object.
			populationCounter = None; #Counter variable. At start, equals nothing. Holds breedable list length.
			
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
					
			populationList = GenerateValues(len(literalList));
			
			while(foundSolution == "false"):
				
				for canidate in populationList:
					
					if canidate.EvaluateData(clauseList, literalList, canidate) >= 1:
						print(canidate.EvaluateData(clauseList, literalList, canidate));
						solution = canidate;
						foundSolution = "true";
						break;
				
				for canidate in populationList:
					breedableList.append(canidate);
				
				populationCounter = len(breedableList);
				
				for parent in range(0, populationCounter / 2):
					parentOne = breedableList[parent];
					parentTwo = Canidate("");
					
					while active == "true":
						parentTwo = breedableList[random.randrange(parent, len(breedableList))];
						
						if parentTwo in breedableList:
							active = "false";
					
					childOne = Canidate(parentTwo.InverseOffspring(literalList, AddToList(parentTwo)));
					childTwo = Canidate(parentOne.InverseOffspring(literalList, AddToList(parentOne)));
					newPopulationList.append(childOne);
					newPopulationList.append(childTwo);
					
					if parentOne in breedableList:
						breedableList.remove(parentOne);
					
					if parentTwo in breedableList:
						breedableList.remove(parentTwo);
					
					for canidate in newPopulationList:
						
						for bit in canidate.value:
							bitString += bit;
						canidate.value = bitString;
				
				for newCanidate in newPopulationList:
					newCanidate.value = newCanidate.MutateValues(14);
					populationList.append(newCanidate);
				
				for canidate in populationList:
					
					if len(finalPopulationList) < 4:
						finalPopulationList.append(canidate);
					
					else:
						
						for check in finalPopulationList:
							
							if canidate.EvaluateData(clauseList, literalList, canidate) > check.EvaluateData(clauseList, literalList, canidate):
								check = canidate;
								
			print(string);
			print("Solution: " + solution.value);
			
Main(); #End of main function.