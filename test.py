from docx import Document
import re, sys
regex = re.compile(r'xx[A-Za-z0-9]{2}xx')

#returns a list of every coded entry in the UBD template document.
def allFinds(document):
	repList = ""
	for table in document.tables:
		for i in range(0,len(table.rows)-1):
				for j in range(0, len(table.columns)-1):
					found = regex.findall(table.cell(i,j).text)
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
	
if len(sys.argv) >= 2:
	document = Document(sys.argv[1])
#replace with function that parses the json file.
repDict = {'xxS1xx':'replacement s1','xxT1xx':'Replacement t1'}
print(allFinds(document))

#document.save('testout.docx')