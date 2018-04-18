for table in document.tables:
		print(counter)
		for i in range(0,len(table.rows)-1):
			for j in range(0, len(table.columns)-1):
					if regex in table.cell(i,j).text:
											
						a = str(table.cell(i,j).text)
						a = a.replace("Findme1","This is a test")
						a = a.replace("Findme2","This is a test2")
						table.cell(i,j).text =  a
		counter+=1
		
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