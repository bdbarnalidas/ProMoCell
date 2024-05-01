
# -------------------------------------------------------------------------------------------------------------------
# This code lists the names of the pathway maps or the filenames stored in '/GPG/KEGG_Pathway_Maps' and saves the
# filenames in a separate file named as 'Pathway_Filenames.txt' and keeps the file in the folder
# '/GPG/KEGG_Pathway_Maps'. This file is needed in other parts of the project.

# Input - The filenames (Pathway Maps) stored in '/GPG/Input/KEGG_Pathway_Maps_eco.txt'.
# Output - '/GPG/KEGG_Pathway_Maps/Pathway_Filenames.txt'
# -------------------------------------------------------------------------------------------------------------------

def main():
	fp = open("../Input/KEGG_Pathway_Maps_eco.txt") # Input
	fp_out = open("../KEGG_Pathway_Maps/Pathway_Filenames.txt","w") # Output
	for line in fp.readlines():
		newLine = line.split("\t")
		newLine = newLine[0].split(":")[1]
		newLine += ".txt"
		fp_out.write(newLine+"\n")
	fp.close()
	fp_out.close()
	return
if __name__ == '__main__':
	main()
