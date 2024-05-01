
# ---------------------------------------------------------------------------------------------------------------------------
# This code performs a statistical analysis on the clusters.

# Input - Frela output stored in 'GO/Frela_Output',clusters for analysis in 'GO/Clusters_After_Removing_Obsolute_Proteins'.
# Output - The statistical outputs saved in 'GO/Analysis_Output'.
# ---------------------------------------------------------------------------------------------------------------------------

#!/usr/bin/env python
import sys, os, warnings
import numpy as np



def ComputeMeanSD(data_list):
	
	min_data = min(data_list)
	max_data = max(data_list)
	
	np_list = []
	np_list = np.array(data_list)
	#print np_list
	mean_list = []
	mean_list = np.mean(np_list)	
	std_list = []
	std_list = np.std(np_list)
#print std_list
	
	return min_data, max_data, mean_list, std_list

def matrix():
	rootDir = '../Frela_Output' # Input Folder
	
	# file_write = 'Score_matrix.tsv'
	
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
			
				scr_mat[GO_list[word[1]]][GO_list[word[3]]] = word[4] + ',' + word[6] + ',' + word[8]
				scr_mat[GO_list[word[3]]][GO_list[word[1]]] = word[4] + ',' + word[6] + ',' + word[8]


	return scr_mat,GO_list,Reverse_GO_list
	
	# fp_write = open(file_write, 'w')
	
	# fp_write.write(' \t')
	# for i in Reverse_GO_list.keys():
	# 	fp_write.write(Reverse_GO_list[i] + '\t')
	# fp_write.write('\n')
	
	# for i in range(1,3749):
	# 	fp_write.write(Reverse_GO_list[i] + '\t')
	# 	for j in range(1,3749):
	# 		fp_write.write(str(scr_mat[i-1][j-1]) + '\t')
	# 	fp_write.write('\n')


def main(mat,go,rev_go):
	folder1 = '../Clusters_After_Removing_Obsolute_Proteins' # Input Folder
	# remove = '/home/user/Desktop/W_2/Source/GO/remove_proteins/remove.txt'

	# obsol = []
	# with open(remove) as fp:
	# 	for ln in fp:
	# 		ln = ln.replace('\n','')
	# 		if ln != '':
	# 			obsol.append(ln)
	# print len(obsol)

	in_cluster = []
	out_cluster = []
	in_cluster_BP = []
	in_cluster_MF = []
	in_cluster_CC = []
	out_cluster_BP =[]
	out_cluster_MF = []
	out_cluster_CC = []
	count = 1
	# tot_count = 256
	
	file_incluster = '../Analysis_Output/InClusterAnalysis.csv' # Output File
	fp_incluster = open(file_incluster,'w')
	fp_incluster.write('#Cluster,BP Min,BP Max,BP Mean,BP Std,MF Min, MF Max,MF Mean,MF Std,CC Min,CC Max,CC Mean,CC Std\n')
	
	file_outcluster = '../Analysis_Output/OutClusterAnalysis.csv' # Output File
	fp_outcluster = open(file_outcluster,'w')
	fp_outcluster.write('#Cluster,BP Min,BP Max,BP Mean,BP Std,MF Min, MF Max,MF Mean,MF Std,CC Min,CC Max,CC Mean,CC Std\n')

	# while count <= tot_count:

	# 	print count
		
	# 	filename1 = folder1 + str(count) +'.txt'
	# 	with open(filename1) as f:
	# 		lines = f.read().splitlines()
	for filename in os.listdir(folder1):
		barn = filename.split('.')
		filename1 = folder1 + '/' + filename 
		print count
		with open(filename1) as f:
			lines = f.read().splitlines()
		count += 1
		# lines.pop()
		# lines.pop()
		# print lines
		# print len(lines)

		in_cluster = []
		out_cluster = []
		in_cluster_BP = []
		in_cluster_MF = []
		in_cluster_CC = []
		out_cluster_BP =[]
		out_cluster_MF = []
		out_cluster_CC = []

		if len(lines) > 1:
			print 'cluster no='+str(count-1)+'\n'
			# for i in range(0,len(lines)):
			# 	a = lines[i]
			# 	for j in range(1,len(lines)):
			# 		b = lines[j]
			# 		value = mat[go[a]][go[b]]
			# 		word = value.split(',')
			# 		if word[0] == '--':
			# 			in_cluster_BP.append(0)
			# 		else:
			# 			in_cluster_BP.append(float(word[0]))
			# 		if word[1] == '--':
			# 			in_cluster_MF.append(0)
			# 		else:
			# 			in_cluster_MF.append(float(word[1]))
			# 		if word[2] == '--':
			# 			in_cluster_CC.append(0)
			# 		else:
			# 			in_cluster_CC.append(float(word[2]))
			for i in range(1,3748):
				a = rev_go[i]
				for j in range(1,3748):
					b = rev_go[j]
					if a in lines and b in lines and a != b :
						print a
						print b
						value = mat[i][j]
						# print value
						word = value.split(',')
						print word
						if word[0] == '--':
							in_cluster_BP.append(0)
							# continue
						else:
							in_cluster_BP.append(float(word[0]))
						if word[1] == '--':
							in_cluster_MF.append(0)
							# continue
						else:
							in_cluster_MF.append(float(word[1]))
						if word[2] == '--':
							in_cluster_CC.append(0)
							# continue
						else:
							in_cluster_CC.append(float(word[2]))
					elif (a in lines and b not in lines) or (a not in lines and b in lines):
						# if a not in obsol and b not in obsol:
						print a
						print b
						value = mat[i][j]
						print value
						word = value.split(',')
						if word[0] == '--':
							out_cluster_BP.append(0)
						else:
							out_cluster_BP.append(float(word[0]))
						if word[1] == '--':
							out_cluster_MF.append(0)
						else:
							out_cluster_MF.append(float(word[1]))
						if word[2] == '--':
							out_cluster_CC.append(0)
						else:
							out_cluster_CC.append(float(word[2]))

			# Compute mean and SD of in cluster for BP
			min_in_cluster_BP, max_in_cluster_BP, mean_in_cluster_BP, sd_in_cluster_BP = ComputeMeanSD(in_cluster_BP)
			# Compute mean and SD of in cluster for MF
			min_in_cluster_MF, max_in_cluster_MF, mean_in_cluster_MF, sd_in_cluster_MF = ComputeMeanSD(in_cluster_MF)
			# Compute mean and SD of in cluster for CC
			min_in_cluster_CC, max_in_cluster_CC, mean_in_cluster_CC, sd_in_cluster_CC = ComputeMeanSD(in_cluster_CC)

			# Compute mean and SD of out cluster for BP
			min_out_cluster_BP, max_out_cluster_BP, mean_out_cluster_BP, sd_out_cluster_BP = ComputeMeanSD(out_cluster_BP)
			# Compute mean and SD of out cluster for MF
			min_out_cluster_MF, max_out_cluster_MF, mean_out_cluster_MF, sd_out_cluster_MF = ComputeMeanSD(out_cluster_MF)
			# Compute mean and SD of out cluster for CC
			min_out_cluster_CC, max_out_cluster_CC, mean_out_cluster_CC, sd_out_cluster_CC = ComputeMeanSD(out_cluster_CC)

			# Write in File
			fp_incluster.write(str(barn[0]) + ',') 
			fp_incluster.write(str(min_in_cluster_BP) + ',' + str(max_in_cluster_BP) + ',' + str(mean_in_cluster_BP) + ',' + str(sd_in_cluster_BP) + ',')
			fp_incluster.write(str(min_in_cluster_MF) + ',' + str(max_in_cluster_MF) + ',' + str(mean_in_cluster_MF) + ',' + str(sd_in_cluster_MF) + ',')
			fp_incluster.write(str(min_in_cluster_CC) + ',' + str(max_in_cluster_CC) + ',' + str(mean_in_cluster_CC) + ',' + str(sd_in_cluster_CC) + '\n')

			fp_outcluster.write(str(barn[0]) + ',')
			fp_outcluster.write(str(min_out_cluster_BP) + ',' + str(max_out_cluster_BP) + ',' + str(mean_out_cluster_BP) + ',' + str(sd_out_cluster_BP) + ',')
			fp_outcluster.write(str(min_out_cluster_MF) + ',' + str(max_out_cluster_MF) + ',' + str(mean_out_cluster_MF) + ',' + str(sd_out_cluster_MF) + ',')
			fp_outcluster.write(str(min_out_cluster_CC) + ',' + str(max_out_cluster_CC) + ',' + str(mean_out_cluster_CC) + ',' + str(sd_out_cluster_CC) + '\n')

	fp_incluster.close()
	fp_outcluster.close()



	# print go[lines[0]]
	# print mat[go[lines[0]]][go[lines[0]]]

	
#---------------------------------------------------------------------------------------

if __name__=='__main__':
	mat,go,rev_go = matrix()
	main(mat,go,rev_go)

