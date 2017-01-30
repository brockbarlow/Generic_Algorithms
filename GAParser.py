#Imports.
import GAClassesAndFunctions
from GAClassesAndFunctions import *

#Functions.
def Main():
	file = "TestFile.txt"
	
	parsedFile = EvaluateFile(file)
	evaluatedList = parsedFile.GetExpressionList()
	
Main()