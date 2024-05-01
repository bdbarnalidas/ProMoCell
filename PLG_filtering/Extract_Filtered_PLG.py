
# -------------------------------------------------------------------------------------------------------------------
# This code extracts the filtered PLG edges.

# Input - The PLG stored in 'PLG/PLG.txt' and the filtered nodes present in 'PLG_Filtering/Filtered_PLG/Nodes.txt'.
# Output - The filtered PLG edges stored in 'PLG_Filtering/Filtered_PLG/Edges.txt'.
# -------------------------------------------------------------------------------------------------------------------

def main():
	fp_write = open('../Filtered_PLG/Edges.txt','w') # Output File
	fp = open("../Filtered_PLG/Nodes.txt") # Input File 
	allIds = []
	for line in fp.readlines():
		ids = line.replace('\n','')
		allIds.append(ids)
	fp.close()
	with open('../../PLG/PLG.txt') as fp: # Input File
		for ln in fp:
			ln = ln.replace('\n','')
			word = ln.split(' ')
			if word[0] in allIds and word[1] in allIds:
				fp_write.write(word[0]+'\t'+word[1]+'\t'+word[2]+'\n')
	fp_write.close()


if __name__ == '__main__':
	main()
