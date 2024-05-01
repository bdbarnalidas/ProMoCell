
# -------------------------------------------------------------------------------------------------------------------
# This code extracts the molecular weight of the proteins of the PLG and calculates their volume and surface area.

# Input - The UniProt files of the proteins of PLG stored in 'PLG_Filtering/MolecularWeight_From_UniProt'.
# Output - 1) The file containing the extracted molecular weights and the calculated volume of the PLG proteins stored 
#			  in 'PLG_Filtering/Volume_SA_Filtered_PLG_Nodes/MolecularWeight_Vol.txt'.
#		   2) The surface area of the filtered PLG proteins stored in 
#			  'PLG_Filtering/Volume_SA_Filtered_PLG_Nodes/Surface_Area.txt'.
#		   3) The PLG nodes after removing the obsolete proteins as per UniProt which is stored in
#			  'PLG_Filtering/Filtered_PLG/Nodes.txt'.
# -------------------------------------------------------------------------------------------------------------------

from __future__ import division
from lxml import html
import requests
import time
import math
import sys, os, warnings

def main():
	count = 0
	flag = 0 
	fp_write = open('../Volume_SA_Filtered_PLG_Nodes/MolecularWeight_Vol.txt','w') # Output File
	fp_write1 = open('../Filtered_PLG/Nodes.txt','w') # Output File
	fp_write2 = open('../Volume_SA_Filtered_PLG_Nodes/Surface_Area.txt','w') # Output File
	rootDir = '../MolecularWeight_From_UniProt' # Input Folder
	for dirName, subdirList, fileList in os.walk(rootDir):		
		for fname in fileList:	
			filename = dirName+'/'+fname
			# print filename
			count += 1
			with open(filename) as fp:
				flag = 0
				for ln in fp:
					word2 = fname.split('.')
					if '(Da)' in ln:
						word = ln.split('(Da):')
						# print word
						# print word[8]
						# print word[1]
						word1 = word[1].split('</span>')
						# print word1
						# print word1[0]
						word4 = word1[1].split('>')
						# print word4[1]

						mw = word4[1].replace(',','')
						mw1 = float(mw)
						area = 4.44*pow(mw1,0.77) 
						radius = math.sqrt(area/(4*math.pi))
						vol = (4/3)*math.pi*pow(radius,3)
						fp_write.write(word2[0]+'\t'+str(mw1)+'\t'+str(vol)+'\n')
						fp_write1.write(word2[0]+'\n')
						fp_write2.write(word2[0]+'\t'+str(area)+'\n')
						flag = 1
						break
				if flag == 0:
					print(word2[0]+' I am obsolete')
			print count


	fp_write.close();
	fp_write1.close();
	fp_write2.close()


#---------------------------------------------------------------------------------------

if __name__=='__main__':
	main()