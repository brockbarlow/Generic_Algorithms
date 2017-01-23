#python parser script, class file.
#made by: Brock Barlow.
#date created: 1/21/2017.
#final due date: 1/25/2017.

import sys #import system.
import random #import random.
import functions #import functions python file.
from functions import * #import everything from functions python file.

class Canidate(object):
	def __init__(self, string):
		bitString = "";
		for bit in string:
			bitString += bit;
		self.value = bitString;
		
	def EvaluateData(self, clauseList, literalList, value):
		tempString = "";
		chromosomeValue = 0;
		for string in clauseList:
			for char in string:
				if char == '?':
					tempString += char;
				elif char == '&':
					tempString += char;
				elif char == 'V':
					tempString += char;
				else:
					index = FindIndex(literalList, char);
					tempString += str(value.value[index]);
			inverse = 0;
			printString = "";
			finalString = "";
			for char in tempString:
				if inverse == 1:
					if char == '1':
						finalString += str(0);
					elif char == '0':
						finalString += str(1);
					inverse = 0;
				elif char == '?' and inverse == 0:
					inverse = 1;
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
		finalList = [];
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