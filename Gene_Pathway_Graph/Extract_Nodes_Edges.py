
# -------------------------------------------------------------------------------------------------------------------
# This code extracts the node information and the edge information from the Pathway Maps.

# Input - The Pathway Maps stored in '/GPG/KEGG_Pathway_Maps'.
# Output - The node information saved in 'GPG/Nodes_Edges_GPG/Nodes_Pathway_Maps.txt'
#		   The edge information saved in 'GPG/Nodes_Edges_GPG/Edges_Pathway_Maps.txt'
# -------------------------------------------------------------------------------------------------------------------

import os
import xml.etree.ElementTree as ET

#this functions iterate over all maps, parse them and stores information about them for further proessing
def getAllEntry(files):
	entryCount = 0
	allEntryTemp = []
	for fileName in files:
		tree = ET.parse("../KEGG_Pathway_Maps/"+fileName) # Input folder
		root = tree.getroot()
		for child in root:
			if child.tag == 'entry':
				tempDict = child.attrib
				tempDict['id'] =  "%s_%s"%(root.attrib['name'],tempDict['id'])
				tempDict['newID'] = entryCount
				tempArr = ["%s_%s"%(root.attrib['name'],i.attrib['id']) for i in child if i.tag != 'graphics']
				tempDict['subPartList'] = tempArr
				allEntryTemp.append(tempDict)
				entryCount += 1
	allEntry = {}
	for i in allEntryTemp: allEntry[i['id']] = i
	return allEntry

#this extract all relations and maplinks from maps and store them in list of dict
def getAllRelations(files):
	relations = []
	maplinks = []
	for fileName in files:
		tree = ET.parse("../KEGG_Pathway_Maps/"+fileName) # Input folder
		root = tree.getroot()
		pathWayName = root.attrib['name']
		for relation in root.findall('relation'):
			if relation.attrib['type'] != 'maplink':
				tempDict = {}
				tempDict['entry1'] = "%s_%s"%(pathWayName,relation.attrib['entry1'])
				tempDict['entry2'] = '%s_%s'%(pathWayName,relation.attrib['entry2'])
				tempDict['subTypeList'] = []
				for i in relation:
					if i.attrib['value'].isdigit() :
						tempDict['subTypeList'].append(pathWayName+'_'+i.attrib['value'])
				relations.append(tempDict)
			elif relation.attrib['type'] == 'maplink':
				tempDict = {}
				tempDict['entry1'] = "%s_%s"%(pathWayName,relation.attrib['entry1'])
				tempDict['entry2'] = '%s_%s'%(pathWayName,relation.attrib['entry2'])
				tempDict['subTypeList'] = []
				for i in relation:
					if i.attrib['value'].isdigit() :
						tempDict['subTypeList'].append(pathWayName+'_'+i.attrib['value'])
				maplinks.append(tempDict)
	return relations,maplinks
#this extract reactions and stores in dictionary as ar, substrate, product
def getAllRections(files):
	reactions = []
	for fileName in files:
		tree = ET.parse("../KEGG_Pathway_Maps/"+fileName) # Input folder
		root = tree.getroot()
		pathWayName = root.attrib['name']
		for reaction in root.findall('reaction'):
			tempDict = {}
			tempDict['ar'] = "%s_%s"%(pathWayName,reaction.attrib['id'])
			tempDict['type'] = reaction.attrib['type']
			tempDict['substrate'] = []
			tempDict['product'] = []
			for i in reaction:
				if i.tag == 'substrate':
					tempDict['substrate'].append(pathWayName+"_"+i.attrib['id'])
				if i.tag == 'product':
					tempDict['product'].append(pathWayName+"_"+i.attrib['id'])
			reactions.append(tempDict)
	return reactions

#this function add edges taking relations and reaction as input and also accroding to reversible and irreversible				
def generateEdges(relations,reactions):
	edges = []
	for relation in relations:
		edges.append([relation['entry1'],relation['entry2']])
	for reaction in reactions:
		for sub in reaction['substrate']:
			edges.append([reaction['ar'],sub])	
		if reaction['type'] == 'reversible':
			for product in reaction['product']:
				edges.append([reaction['ar'],sub])
	return edges

#this function find out and add inter-map edges
def removeMapLink(maplinks,edges,allEntry):
	mlEdges = []
	for i in maplinks:
		l1 = []
		l2 = []
		if allEntry[i['entry1']]['type'] == 'map':
			for key in allEntry:
				if key.startswith(allEntry[i['entry1']]['name']+"_") and allEntry[key]['name'] == allEntry[i['subTypeList'][0]]['name']:
					l1.extend([x[0] for x in edges if x[1]==key])
		else:
			l1 = [i['entry1']]

		if allEntry[i['entry2']]['type'] == 'map':
			for key in allEntry:
				if key.startswith(allEntry[i['entry2']]['name']+"_") and allEntry[key]['name'] == allEntry[i['subTypeList'][0]]['name']:
					l2.extend([x[1] for x in edges if x[0] == key])
		else :
			l2 = [i['entry2']]
		for j in l1:
			for k in l2:
				mlEdges.append([j,k])
	return mlEdges

#this function remove groups and add edge for every one of compound in group
def removeGroups(edges,allEntry):
	newEdges = []
	for i in edges:
		l1 = []
		l2 = []
		if allEntry[i[0]]['type'] == 'group':
			l1 = allEntry[i[0]]['subPartList']
		else: 
			l1 = [i[0]]
		if allEntry[i[1]]['type'] == 'group':
			l2 = allEntry[i[1]]['subPartList']
		else: 
			l2 = [i[1]]
		for j in l1:
			for k in l2:
				newEdges.append([j,k])
	return newEdges

def main():
	path = "../KEGG_Pathway_Maps/" # Input folder
	files = os.listdir(path)
	files = [x for x in files if x.startswith("eco")]
	allEntry = getAllEntry(files)
	relations,maplinks = getAllRelations(files)
	reactions = getAllRections(files)
	edges = generateEdges(relations,reactions)
	temp = removeMapLink(maplinks,edges,allEntry)
	edges.extend(temp)
	edges = removeGroups(edges,allEntry)
	fp = open('../Nodes_Edges_GPG/Nodes_Pathway_Maps.txt','w') # Output file for saving node information
	toPrintNodes = [(allEntry[x]['name'],allEntry[x]['link']) for x in allEntry if allEntry[x]['type']!='group']
	toPrintNodes = list(set(toPrintNodes))
	for i in toPrintNodes:
		fp.write(i[0]+'\n')
		fp.write(i[1]+'\n')
	fp.close()
	fp = open("../Nodes_Edges_GPG/Edges_Pathway_Maps.txt","w") # Output file for saving edge information
	for i in edges:
		fp.write(allEntry[i[0]]['name']+'\n')
		fp.write(allEntry[i[1]]['name']+'\n')
	fp.close()
if __name__ == '__main__':
	main()
