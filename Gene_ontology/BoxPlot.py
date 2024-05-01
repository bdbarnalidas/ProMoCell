
# ---------------------------------------------------------------------------------------------------------------------------
# This code generates the boxplot of the statistical analysis of the clusters.

# Input - The statistical analysis output files saved in 'GO/Analysis_Output/'.
# Output - The boxplots saved in 'GO/BoxPlots'.
# ---------------------------------------------------------------------------------------------------------------------------

#!/usr/bin/env python

import numpy
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm
import gc 
import matplotlib.patches as mpatches
import matplotlib.mlab as mlab


font = {'family' : 'normal',
				'size' : 44}

matplotlib.rc('font', **font)



def BoxPlot(mean1,std1,mean2,std2,filename):
	fig1 = plt.figure(figsize=(100, 50))
	length = range(1,len(mean1)+1)
	length1 = []
	length2 = []

	a = range(1,125) # Input - Total no of clusters
	for i in [31,62,65,66,67,76,77,83,84,86,90,91,92,101,103,109,112,121]: # Input - The missing clusters
		b = a.index(i)
		del a[b]

	length1[:] = [x for x in length]
	plt.errorbar(a, mean1, std1 ,fmt='o', markersize=30, capsize=20, elinewidth=4, mfc='magenta', ecolor='magenta', label="in-group")
	length2[:] = [x for x in length]
	plt.errorbar(a, mean2, std2 ,fmt='o', markersize=30, capsize=20, elinewidth=4, mfc='blue', ecolor='blue', label="out-group")
		
	#plt.xticks(numpy.arange(min(length), max(length)+500, 250.0))
	plt.xlim([0,125])
	plt.ylim([-0.5,1.25])
	a = range(1,125) # Input - Total no of clusters
	for i in [31,62,65,66,67,76,77,83,84,86,90,91,92,101,103,109,112,121]: # Input - The missing clusters
		b = a.index(i)
		del a[b]
	# for i in range(len(a)):
	# 	a[i] = str(a[i])

	
	plt.xticks(numpy.array(a), rotation='vertical')
	
	plt.grid(False)
	#plt.ylim([25,75])
	#plt.yticks(numpy.arange(min(length), max(length)+500, 250.0))
	
	plt.legend(loc='upper right')
	#plt.show()
	#filename = outputdir + '/Gadiformes_MS.pdf'
	plt.savefig(filename)





def ReadScores(inputfile):
		
	fp = open(inputfile,'r')
	first_line = fp.readline()
	
	BP_mean = []
	BP_std = []
	MF_mean = []
	MF_std = []
	CC_mean = []
	CC_std = []
	
	lines = fp.readlines()
	for line in lines:
		word = line.replace('\n','').replace(' ','').split(',')
		BP_mean.append(float(word[3]))
		BP_std.append(float(word[4]))
		MF_mean.append(float(word[7]))
		MF_std.append(float(word[8]))
		CC_mean.append(float(word[11]))
		CC_std.append(float(word[12]))
	
	# return BP_mean,BP_std,MF_mean,MF_std,CC_mean,CC_std
	return BP_mean,BP_std,MF_mean,MF_std,CC_mean,CC_std
	


def main():
	incluster_file = '../Analysis_Output/InClusterAnalysis.csv' # Input File
	outcluster_file = '../Analysis_Output/OutClusterAnalysis.csv' # Input File

	in_BP_mean,in_BP_std,in_MF_mean,in_MF_std,in_CC_mean,in_CC_std = ReadScores(incluster_file)
	# in_BP_mean,in_BP_std = ReadScores(incluster_file)
	
	out_BP_mean,out_BP_std,out_MF_mean,out_MF_std,out_CC_mean,out_CC_std = ReadScores(outcluster_file)
	# out_BP_mean,out_BP_std = ReadScores(outcluster_file)
	
	BoxPlot(in_BP_mean,in_BP_std,out_BP_mean,out_BP_std,'../BoxPlots/BP.eps') # Output File
	BoxPlot(in_MF_mean,in_MF_std,out_MF_mean,out_MF_std,'../BoxPlots/MF.eps') # Output File
	BoxPlot(in_CC_mean,in_CC_std,out_CC_mean,out_CC_std,'../BoxPlots/CC.eps') # Output File
	

	
#---------------------------------------------------------------------------------------

if __name__=='__main__':
	main()