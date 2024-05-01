
# -------------------------------------------------------------------------------------------------------------------
# This code downloads node information from the KEGG website.

# Input - The nodelist of GPG stored in 'GPG/Nodes_Edges_GPG/Nodes_Pathway_Maps.txt'.
# Output - Each node information is stored in the form of a html file in 'GPG/Nodes_GPG'.
# -------------------------------------------------------------------------------------------------------------------


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
	filecount = 0
	with open('../Nodes_Edges_GPG/Nodes_Pathway_Maps.txt') as fp: # Input file
		for ln in fp:
			count += 1
			if count%2 == 0:
				print count
				filecount += 1
				filename = '../Nodes_GPG/'+str(filecount)+'.html' # Output file
				fp_write = open(filename,'w')
				ln = ln.replace('\n','') # contains the url
				url = ln
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
				page=page.replace('\n','')
				fp_write.write(page)
				fp_write.close()
			else:
				continue


#---------------------------------------------------------------------------------------

if __name__=='__main__':
	main()
