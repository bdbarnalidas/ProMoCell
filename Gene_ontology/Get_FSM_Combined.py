
# ---------------------------------------------------------------------------------------------------------------------------
# This code extracts the FSM where each cell (i,j) denotes the combined FS value between proteins i and j.

# Input - Frela output of the clusters saved in 'GO/Frela_Output'. 
# Output - The FSM containing combined FS value stored in 'GO/Functional_Similarity_Matrix/FSM_Combined.tsv'. 
# ---------------------------------------------------------------------------------------------------------------------------

#!/usr/bin/env python
import sys, os, warnings



def main():
	rootDir = '../Frela_Output' # Input Folder
	
	file_write = '../Functional_Similarity_Matrix/FSM_Combined.tsv' # Output File
	
	scr_mat = [['--' for i in range(3748)] for j in range(3748)]
	
	GO_list = {}
	Reverse_GO_list = {}
	
	i = 1
	with open('../../PLG_Filtering/Filtered_PLG/Nodes.txt') as fp: # Input File - Panel File
		for line in fp:
			line = line.replace('\n','')
			GO_list.update({line : i})
			Reverse_GO_list.update({i : line})
			
			i += 1
		
	#for dirName, subdirList, fileList in os.walk(rootDir):
		#for fname in fileList:
			#if '.tsv' in fname and '#' not in fname:
	
	files = range(1,125)
	files.append('Single_Node')
	
	for fname in files:
		# print fname
		filename = rootDir + '/' + str(fname) + '.tsv'
		fp = open(filename,'r')
		#first_line = fp.readline()
		
		lines = fp.readlines()
		
		lines = lines[1:]
		# print lines[0]
		for line in lines:
			if 'UniProt' not in line:
				word = line.replace('\n','').split('\t')
			
				# scr_mat[GO_list[word[1]]][GO_list[word[3]]] = word[4] + ',' + word[6] + ',' + word[8]
				scr_mat[GO_list[word[1]]][GO_list[word[3]]] = word[10]
				scr_mat[GO_list[word[3]]][GO_list[word[1]]] = word[10]
	
	
	fp_write = open(file_write, 'w')
	
	fp_write.write(' \t')
	for i in Reverse_GO_list.keys():
		fp_write.write(Reverse_GO_list[i] + '\t')
	fp_write.write('\n')
	
	for i in range(1,3748):
		fp_write.write(Reverse_GO_list[i] + '\t')
		for j in range(1,3748):
			fp_write.write(str(scr_mat[i][j]) + '\t')
		fp_write.write('\n')



#---------------------------------------------------------------------------------------

if __name__=='__main__':
	main()