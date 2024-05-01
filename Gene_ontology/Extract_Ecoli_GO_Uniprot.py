
# ---------------------------------------------------------------------------------------------------------------------------
# This code extracts the GO information of those proteins present in the PLG constructed for E. coli.

# Input - The nodes of the filtered PLG saved in 'PLG_Filtering/Filtered_PLG/Nodes.txt'.
#		  The GO database of all proteins of all organisms saved in 'GO/Input/goa_uniprot_all.gpa'.
# Output - The GO information of the PLG proteins only saved in 'GO/Input/Ecoli_GO.txt'.
# ---------------------------------------------------------------------------------------------------------------------------

def main():
	nodeList = []
	with open("../../PLG_Filtering/Filtered_PLG/Nodes.txt") as fp: # Input File
		for ln in fp:
			ln = ln.replace('\n','')
			nodeList.append(ln)
	count = 0
	fpWrite = open("../Input/Ecoli_GO11.txt","w") # Output File

	with open("../Input/goa_uniprot_all.gpa") as infile: # Input File
		for line in infile:
			lineParts =  line.split("\t")
			if lineParts[0] == "UniProtKB" and lineParts[1] in nodeList:
				fpWrite.write(line)
			count += 1
			if count % 500000 == 0 :
				print count,"/315846800\t", 100*count/315846800.0,"% approximately"
	fpWrite.close()
	
if __name__ == '__main__':
	main()
