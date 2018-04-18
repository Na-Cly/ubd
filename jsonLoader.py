#Takes any number of files as specified in the json and will run the insertion process for every file listed.
import json, sys

#open the json file.
if len(sys.argv) > 1:
	loadFile = open(sys.argv[1])

#load json data from the json file
json_data = json.loads(loadFile.read())

#gets the list of keys in this case the file names.
files = list(json_data.keys())

#loops through each file listed in the json and prints the list of dictionary contents for each
for each in files:
	tempDict = json_data[each]
	print("File Name: " + each + "\n")
	print(tempDict)
	print("-".center(25,"-"))