
# ---------------------------------------------------------------------------------------------------------------------------
# This code extracts the FSM where each cell (i,j) denotes the FS value between proteins i and j for a particular ontology.

# Input - Frela output of the clusters saved in 'GO/Frela_Output'. 
# Output - The FSM containing FS value for BP ontology stored in 'GO/Functional_Similarity_Matrix/FSM_BP.tsv'. 
#		   The FSM containing FS value for CC ontology stored in 'GO/Functional_Similarity_Matrix/FSM_CC.tsv'. 
#		   The FSM containing FS value for MF ontology stored in 'GO/Functional_Similarity_Matrix/FSM_MF.tsv'. 
# ---------------------------------------------------------------------------------------------------------------------------

#!/usr/bin/env python
import sys, os, warnings



def main():
	rootDir = '../Frela_Output' # Input Folder
	
	file_write1 = '../Functional_Similarity_Matrix/FSM_BP.tsv' # Output File - FSM for BP ontology
	file_write2 = '../Functional_Similarity_Matrix/FSM_MF.tsv' # Output File - FSM for MF ontology
	file_write3 = '../Functional_Similarity_Matrix/FSM_CC.tsv' # Output File - FSM for CC ontology
	
	scr_mat_BP = [['--' for i in range(3748)] for j in range(3748)]
	scr_mat_MF = [['--' for i in range(3748)] for j in range(3748)]
	scr_mat_CC = [['--' for i in range(3748)] for j in range(3748)]
	
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
				scr_mat_BP[GO_list[word[1]]][GO_list[word[3]]] = word[4]
				scr_mat_BP[GO_list[word[3]]][GO_list[word[1]]] = word[4]
				scr_mat_MF[GO_list[word[1]]][GO_list[word[3]]] = word[6]
				scr_mat_MF[GO_list[word[3]]][GO_list[word[1]]] = word[6]
				scr_mat_CC[GO_list[word[1]]][GO_list[word[3]]] = word[8]
				scr_mat_CC[GO_list[word[3]]][GO_list[word[1]]] = word[8]
	
	
	fp_write1 = open(file_write1, 'w')
	fp_write2 = open(file_write2, 'w')
	fp_write3 = open(file_write3, 'w')
	
	fp_write1.write(' \t')
	fp_write2.write(' \t')
	fp_write3.write(' \t')
	for i in Reverse_GO_list.keys():
		fp_write1.write(Reverse_GO_list[i] + '\t')
		fp_write2.write(Reverse_GO_list[i] + '\t')
		fp_write3.write(Reverse_GO_list[i] + '\t')
	fp_write1.write('\n')
	fp_write2.write('\n')
	fp_write3.write('\n')
	
	for i in range(1,3748):
		fp_write1.write(Reverse_GO_list[i] + '\t')
		fp_write2.write(Reverse_GO_list[i] + '\t')
		fp_write3.write(Reverse_GO_list[i] + '\t')
		for j in range(1,3748):
			fp_write1.write(str(scr_mat_BP[i][j]) + '\t')
			fp_write2.write(str(scr_mat_MF[i][j]) + '\t')
			fp_write3.write(str(scr_mat_CC[i][j]) + '\t')
		fp_write1.write('\n')
		fp_write2.write('\n')
		fp_write3.write('\n')



#---------------------------------------------------------------------------------------

if __name__=='__main__':
	main()