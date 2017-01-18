#python parser script 
#made by: Brock Barlow
#date created: 1/11/2017
#final due date: 1/25/2017

import sys #import system.

def findLiteralIndex(): #This function finds the index value of the literal. Used to convert the literal character value into a chromosome integer value.
	#
findLiteralIndex(); #End of the findLiteralIndex function.

def main(): #Main parser function.
	#fileOne = "CNFExpressions.txt"; #Name of the file being used. Main file.
	fileTwo = "TestCNFExpression.txt"; #Name of the file being used. Test file.
	inFile = open(fileTwo, 'r'); #Open the file and read it.
	
	#print("Question Mark ? = NOT"); #Display to the user what the question mark represents.
	#print("Capital V = OR"); #Display to the user what the capital V represents.
	#print("Ampersand & = AND"); #Display to the user what the Ampersand represents.
	#print("Open Bracket { = BEGIN CLAUSE"); #Display to the user what the open bracket represents.
	#print("Close Bracket } = END CLAUSE"); #Display to the user what the close bracket represents.
	#print("\n"); #Add a new line.
	
	for string in inFile: #For every string, do the following.
		
		if (inFile): #If these are present in the file...
			
			#numOfClauses = 0; #Number of clauses in the string.
			#openClause = 0; #Is there an open clause in the string?
			#numOfNots = 0; #Number of NOTs present in the string.
			#numOfOrs = 0; #Number of ORs present in the string.
			#numOfAnds = 0; #Number of ANDs present in the string.
			
			literalList = []; #List of literals in the string.
			clauseList = []; #List of clauses in the string.
			literalValues = [1, 0, 1, 0, 1, 0]; #Holds the chromosome values of the literals being used. a = 1, b = 0, c = 1, d = 0, e = 1, f = 0. This value will get overwritten.
			withinClause = "false"; #Bool variable. If processing data in a clause then this will equal true. Otherwise, this variable will always equal false.
			stringDataHolder = ""; #Holds string data. Starts empty.
			tempStringDataHolder = ""; #Holds string data. Used to temporary hold data. Starts empty.
			chromosomeStringDataHolder = ""; #Holds the converted string data. Starts empty.
			inverseValue = "false"; #Bool variable. If true, inverse the data. Otherwise, don't inverse.
			literalIndexValue = 0; #Holds the chromosome values of the literal values.
			
			for char in string: #For every character in the string, do the following.
			
				if char == '?' and withinClause == "true": #If the character is a Question Mark and we are within the clause...
					#numOfNots += 1; #increment the NOTs variable.
					stringDataHolder += char; #increment the stringDataHolder variable with the char value.
				
				elif char == 'V' and withinClause == "true": #If the character is a Capital V and we are within the clause...
					#numOfOrs += 1; #increment the ORs variable.
					stringDataHolder += char; #increment the stringDataHolder variable with the char value.
				
				elif char == '&' and withinClause == "true": #If the character is an Ampersand and we are within the clause...
					#numOfAnds += 1; #increment the ANDs variable.
					stringDataHolder += char; #increment the stringDataHolder variable with the char value.
				
				elif char == ' ': #If the character is a space...
					continue; #move on to the next character.
				
				elif char == '\n': #If the character is a new line...
					continue; #move on to the next character.
				
				elif char == '{' and withinClause == "false": #If the character is an Open Bracket and we are not within the clause...
					#openClause = 1; #increment the openClause variable.
					withinClause = "true"; #change the withinClause value to true.
				
				#elif char == '}' and openClause == 1: #If the character is an Close Bracket and if openClause has a value in it...
					#numOfClauses += 1; #increment the Number of Clauses variable and...
					#openClause = 0; #set the openClause variable to zero.
				
				elif withinClause == "true": #If withinClause is equal to true...
					stringDataHolder += char; #increment the stringDataHolder variable with the char value.
					if char in literalList: #If the character in the literals list is already present...
						continue; #move on.
					literalList.append(char); #Otherwise, add the character to the literals list.
				
				elif char == '}' and withinClause == "true": #If the character is an Close Bracket and we are within the clause...
					withinClause = "false"; #change the withinClause value to false.
					clauseList.append(stringDataHolder); #add the stringDataHolder variable value(s) to the clause list.
					stringDataHolder = ""; #clear the stringDataHolder variable.
				
				#else: 
					#if char in literals: #If the character in the literals list is already present...
						#continue; #move on.
					#literals.append(char); #Otherwise, add the character to the literals list.
					
			for string in clauseList: #For every string in the clause list, do the following.
				for char in string: #For every character in the string, do the following.
				
					if char == '?': #If the character is a Question Mark...
						tempStringDataHolder += char; #increment the tempStringDataHolder variable with the char value.
						
					elif char == 'V': #If the character is a Capital V...
						tempStringDataHolder += char; #increment the tempStringDataHolder variable with the char value.
						
					elif char == '&': #If the character is an Ampersand...
						tempStringDataHolder += char; #increment the tempStringDataHolder variable with the char value.
						
					else:
						literalIndexValue = findLiteralIndex(literalList, char); #The literalIndexValue will equal the result of the findLiteralIndex function.
			
		#literalList.sort(); #Sort thought the literals list.
	
		#print(string); #Display the string.
		#print("Number of ANDs: ", numOfAnds); #Display the number of ANDs within the string.
		#print("Number of NOTs: ", numOfNots); #Display the number of NOTs within the string.
		#print("Number of ORs: ", numOfOrs); #Display the number of ORs within the string.
		#print("Number of literals: ", len(literals)); #Display the number of literals within the string.
		#print("Literals: ", literals); #Display the literals being used within the string.
		#print("Number of clauses: ", numOfClauses); #Display the number of clauses within the string.
		#print("\n"); #Add a new line.
	
	inFile.close(); #Close the file.
	
main(); #End of main function.