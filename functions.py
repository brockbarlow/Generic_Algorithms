#python parser script, class file.
#made by: Brock Barlow.
#date created: 1/21/2017.
#final due date: 1/25/2017.

import sys #import system.
import random #import random.
import classes #import classes python file.
from classes import * #import everything from classes python file.

def FindIndex(list, case): #Find index function. Takes in a list and case.
	counter = 0; #Count variable.
	for item in list: #For every item in the list...
		if item == case: #If the item is equal to the case...
			return counter; #return the count variable.
		else: #Otherwise,
			counter += 1; #increment the count variable.
			
def GenerateValues(itemLength):
	valueList = [];
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
			
def AddToList(item): #Add to list function. Takes in a item.
	list = []; #List of items.
	for char in item.value: #For every character in items value...
		list.append(char); #add the character to the list.
	return list; #Otherwise, just return the list.
			
def Print(list): #Print function. Takes in a list.
	for item in list: #For every item in the list...
		print(item); #print the item.