
# -------------------------------------------------------------------------------------------------------------------
# This code extracts the nodes of PPIM of E. coli.

# Input - The unweighted edges of PPIM stored in 'PPIM/Nodes_Edges_PPIM/Unweighted_Edges.txt'.
# Output - Nodes of PPIM stored in 'PPIM/Nodes_Edges_PPIM/Nodes.txt'.
# -------------------------------------------------------------------------------------------------------------------

#!/usr/bin/env python

def main():
	fp_write = open('../Nodes_Edges_PPIM/Nodes.txt','w') # Output File
	count_node = {}
	with open('../Nodes_Edges_PPIM/Unweighted_Edges.txt') as fp: # Input File
		for ln in fp:
			if '\n' in ln:
				ln = ln[:-1]
			word = ln.split('\t')
			if not word[0] in count_node.keys():
				count_node.update({word[0]:1})
			if not word[1] in count_node.keys():
				count_node.update({word[1]:1})
	for key in count_node.keys():
		fp_write.write(key+'\n')
	fp_write.close()

#---------------------------------------------------------------------------------------

if __name__=='__main__':
	main()