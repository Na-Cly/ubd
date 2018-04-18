#Takes any number of files as specified in the json and will run the insertion process for every file listed.
import json, sys

#open the json file.
if len(sys.argv) > 1:
	loadFile = open(sys.argv[1])

def loadData(json_data):
	fileCounter = 0
	files = list(json_data.keys())
	tempDict = {}
	#loops through each file listed in the json and prints the list of dictionary contents for each
	for each in files:
		tempDict[each]=json_data[each] 
	return tempDict

#gets a list of codes from the document.
def generateCodeList(document, regex):
	repList = ""
	rePattern = re.compile(regex)
	for table in document.tables:
		for i in range(0,len(table.rows)-1):
				for j in range(0, len(table.columns)-1):
					found = rePattern.findall(table.cell(i,j).text)
					if found:
						for item in found:
							if item in repList:
								found.remove(item)
					if found:			
						repList = repList + ",".join(found) + "," 
	repList = repList.split(",")
	if "" in repList:
		repList.remove("")
	return repList

#uses the document codes to create a suitable json file.
def generateJson(filename, numFiles):
	json_file = open(filename,'a')
	
	for i in range(0, numFiles):
		for item in generateCodeList(document,regex):
			#in here we need to create our json
	