#python parser script 
#made by: Brock Barlow
#date created: 1/11/2017

def main(): #Main parser function.
	file = "CNFExpressions.txt"; #Name of the file being used.
	inFile = open(file, 'r'); #Open the file and read it.
	
	for string in inFile: #For every string, do the following.
		
		if (inFile): #If these are present in the file...
			
			numOfClauses = 0; #Number of clauses in the string.
			literals = []; #Number of literals in the string.
			openClause = 0; #Is there an open clause in the string?
			numOfNots = 0; #Number of NOTs present in the string.
			numOfOrs = 0; #Number of ORs present in the string.
			numOfAnds = 0; #Number of ANDs present in the string.
			
			for char in string: #For every character in the string, do the following.
			
				if char == '?': #If the character is a Question Mark...
					numOfNots += 1; #increment the NOTs variable.
				
				elif char == 'V': #If the character is a Capital V...
					numOfOrs += 1; #increment the ORs variable.
				
				elif char == '&': #If the character is an Ampersand...
					numOfAnds += 1; #increment the ANDs variable.
				
				elif char == ' ': #If the character is a space...
					continue; #move on to the next character.
				
				elif char == '\n': #If the character is a new line...
					continue; #imove on to the next character.
				
				elif char == '{': #If the character is an Open Bracket...
					openClause = 1; #increment the openClause variable.
				
				elif char == '}' and openClause == 1: #If the character is an Close Bracket and if openClause has a value in it...
					numOfClauses += 1; #increment the Number of Clauses variable and...
					openClause = 0; #set the openClause variable to zero.
				
				else: 
					if char in literals: #If the character in the literals list is already present...
						continue; #move on.
					literals.append(char); #Otherwise, add the character to the literals list.
	
	literals.sort(); #Sort thought the literals list.
	
	inFile.close(); #Close the file.
	
	print(string); #Display the string.
	print("\n"); #Add a new line.
	
	print("Number of ANDs: ", numOfAnds); #Display the number of ANDs within the string.
	print("Number of NOTs: ", numOfNots); #Display the number of NOTs within the string.
	print("Number of ORs: ", numOfOrs); #Display the number of ORs within the string.
	print("\n"); #Add a new line.
	
	print("Number of literals: ", len(literals)); #Display the number of literals within the string.
	print("Literals: ", literals); #Display the literals being used within the string.
	print("\n"); #Add a new line.
	
	print("Number of clauses: ", numOfClauses); #Display the number of clauses within the string.
	print("\n"); #Add a new line.
main() #End of main function.