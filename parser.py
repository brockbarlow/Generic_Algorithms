#python parser script, main file.
#made by: Brock Barlow.
#date created: 1/11/2017.
#final due date: 1/25/2017.

import sys #import system.
import random #import random.
import classes #import classes python file.
from classes import * #import everything from classes python file.

def Main(): #Main function.
	fileOne = "CNFExpressions.txt"; #Name of file one. Holds cnf expressions.
	fileTwo = "TestCNFExpression.txt"; #Name of file two. Holds a test cnf expression.
	inFileOne = open(fileOne, 'r'); #Open and read file one.
	inFileTwo = open(fileTwo, 'r'); #Open and read file two.
	
	for string in inFileTwo: #For every string in file two, do the following.
		
		if(inFileTwo): #If in the file...
			
			clauseList = []; #List of clauses in the expression.
			literalList = []; #List of literals in the expression.
			withinClause = "false"; #Bool variable. Used to identify if we're in a clause or not.
			evaluationString = ""; #Holds data after evaluating the file.
			for char in string: #For each character in the string, do the following.
				if char == '?' and withinClause == "true": #If the char equals a question mark and is within the clause...
					evaluationString += char; #increment the character to the evaluation string.
				elif char == '&' and withinClause == "true": #If the char equals an ampersand and is within the clause...
					evaluationString += char; #increment the character to the evaluation string.
				elif char == 'V' and withinClause == "true": #If the char equals a capital v and is within the clause...
					evaluationString += char; #increment the character to the evaluation string.
				elif char == ' ': #If the char equals a space...
					continue; #move on to the next character.
				elif char == '\n': #If the char equals a new line...
					continue; #move on to the next character.
				elif char == '{' and withinClause == "false": #If the char equals an open bracket and is not within the clause...
					withinClause = "true"; #turn withinClause to true.
				elif char == '}' and withinClause == "true": #If the char equals a closed bracket and is within the clause...
					withinClause = "false"; #turn withinClause to false.
					clauseList.append(evaluationString); #add the data from the evaluation string to the clause list.
					evaluationString = ""; #clear the evaluation string.
				elif withinClause == "true": #If withinClause is equal to true...
					evaluationString += char; #increment the character to the evaluation string.
					if char in literalList: #If the character is in the literal list...
						continue; #move on.
					literalList.append(char); #otherwise, add the character to the literal list.
					
			populationList = [];
			populationList = GenerateValues(len(literalList));
			solution = None;
			foundSolution = 0;
			while(foundSolution == 0):
				for canidate in populationList:
					if canidate.EvaluateData(clauseList, literalList, canidate) >= 1:
						print(canidate.EvaluateData(clauseList, literalList, canidate));
						solution = canidate;
						foundSolution = 1;
						break;
				breedableList = [];
				for canidate in populationList:
					breedableList.append(canidate);
				newPopulationList = [];
				populationCounter = len(breedableList);
				for parent in range(0, populationCounter / 2):
					parentOne = breedableList[parent];
					parentTwo = Canidate("");
					active = "true";
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
						bitString = "";
						for bit in canidate.value:
							bitString += bit;
						canidate.value = bitString;
				for newCanidate in newPopulationList:
					newCanidate.value = newCanidate.MutateValues(14);
					populationList.append(newCanidate);
				finalPopulationList = [];
				for canidate in populationList:
					if len(finalPopulationList) < 4:
						finalPopulationList.append(canidate);
					else:
						for check in finalPopulationList:
							if canidate.EvaluateData(clauseList, literalList, canidate) > check.EvaluateData(clauseList, literalList, canidate):
								check = canidate;
								
			print(string);
			print("Solution: " + solution.value);
Main();