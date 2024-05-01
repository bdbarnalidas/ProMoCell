
# -------------------------------------------------------------------------------------------------------------------
# This code downloads the UniProt information of the proteins from their given entrez locuzlink.

# Input - The E. coli PPIs from BioGRID stored in 'PPIB/Intermediate_Files/Ecoli_PPIs.txt'.
# Output - Each protein's UniProt information is saved in 'PPIB/Nodes_BioGRID'.
#		   Nodecount of PPIB saved in 'PPIB/Intermediate_Files/noOfNodes.txt'.
# -------------------------------------------------------------------------------------------------------------------

#!/usr/bin/env python

import re
import urllib,urllib2
import requests
import time 

http_proxy  = "http://172.16.2.30:8080"
https_proxy = "https://172.16.2.30:8080"
ftp_proxy   = "ftp://172.16.2.30:8080"

proxyDict = { 
              "http"  : http_proxy, 
              "https" : https_proxy, 
              "ftp"   : ftp_proxy
            }

def main():
	count = 0
	with open('../Intermediate_Files/Ecoli_PPIs.txt') as fp: # Input File
		for ln in fp:
			filename = '../Nodes_BioGRID/'+str(count)+'.txt' # Output Folder 
			count += 1
			filename1 = '../Nodes_BioGRID/'+str(count)+'.txt' # Output Folder
			fp_write = open(filename,'w')
			fp_write1 = open(filename1,'w')
			word = re.split(r'\t+',ln)	
			word1 = word[0].split(':')
			word2 = word[1].split(':')
			url = "http://www.uniprot.org/uniprot/?query=reviewed:yes+AND+GeneID:"+str(word1[1]) 
			response = ''
			while response == '':
				try:
					response = requests.get(url,proxies = proxyDict)
				except:
					print("Connection refused by the server..")
					print("Let me sleep for 5 seconds")
					print("ZZzzzz...")
					time.sleep(5)
					print("Was a nice sleep, now let me continue...")
					continue
			page=response.text
			page=page.encode('ascii', 'ignore').decode('ascii')
			fp_write.write(page)
			fp_write.close()
			url = "http://www.uniprot.org/uniprot/?query=reviewed:yes+AND+GeneID:"+str(word2[1]) 
			response = ''
			while response == '':
				try:
					response = requests.get(url,proxies = proxyDict)
				except:
					print("Connection refused by the server..")
					print("Let me sleep for 5 seconds")
					print("ZZzzzz...")
					time.sleep(5)
					print("Was a nice sleep, now let me continue...")
					continue
			page=response.text
			page=page.encode('ascii', 'ignore').decode('ascii')
			fp_write1.write(page)
			fp_write1.close()
			count += 1
			# print count
	fp_write = open('../Intermediate_Files/noOfNodes.txt','w') # Output File
	fp_write.write(str(count))
	fp_write.close()

#---------------------------------------------------------------------------------------

if __name__=='__main__':
	main()