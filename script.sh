
# Script file for 'PaCeS'
# Author - Barnali Das
# Date - 19.9.2017

Path='GPG/Code/' # The path to all the source codes related to GPG construction
Path1='PPID/Code' # The path to all the source codes related to PPID construction
Path2='GPG_And_PPID/Code' # The path to all the source codes related to GPG_PPID construction
Path3='PPII/Code' # The path to all the source codes related to PPII construction
Path4='GPG_PPID_PPII/Code' # The path to all the source codes related to GPG_PPID_PPII construction
Path5='PPIM/Code' # The path to all the source codes related to PPIM construction
Path6='GPG_PPID_PPII_PPIM/Code' # The path to all the source codes related to GPG_PPID_PPII_PPIM construction
Path7='PPIB/Code' # The path to all the source codes related to PPIB construction
Path8='PLG/Code' # The path to all the source codes related to PLG construction
Path9='PLG_Filtering/Code' # The path to all the source codes related to filtering PLG wrt UniProt
Path10='PLG_Clustering/Code' # The path to all the source codes related to clustering PLG
Path11='GO/Code' # The path to all the source codes related to GO verification
Path12='Cell_Division/Code' # The path to all the source codes related to Computational Cell Division
Path13='Cell_Division/Voro/examples/CCD' # The path to all the source codes related to Voronoi Diagram construction

echo
echo 'export http_proxy=172.16.2.30:8080'
echo 'export https_proxy=172.16.2.30:8080'
echo 'export ftp_proxy=172.16.2.30:8080'

# ----------------------------------------------------------------------------------------------------------------
# Phase1 - GPG construction
# ----------------------------------------------------------------------------------------------------------------
echo 
echo 'A)  GPG Construction--------------------------------------------------------------------------------'
echo

STEP_1=0 # Set STEP_1 to 1 if you want to execute command1

STEP_2=0 # Set STEP_2 to 1 if you want to execute command2

STEP_3=0 # Set STEP_3 to 1 if you want to execute command3

STEP_4=0 # Set STEP_4 to 1 if you want to execute command4

STEP_5=0 # Set STEP_5 to 1 if you want to execute command5

STEP_6=0 # Set STEP_6 to 1 if you want to execute command6

STEP_7=0 # Set STEP_7 to 1 if you want to execute command7

STEP_8=0 # Set STEP_8 to 1 if you want to execute command8

# ----------------------------------------------------------------------------------------------------------------
# Command1 - Download Pathway Maps from KEGG database
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_1 == 1 ] # Command1 will be executed
	then
		echo '1)  Downloading Pathway Maps from KEGG database-----------------------------------------------------'
		command1='cd '$Path
		$command1
		command1='javac Download_Pathway_Maps.java'
		echo '   '$command1
		$command1
		command1='java Download_Pathway_Maps'
		echo '   '$command1
		$command1
		cd ~-
		echo '   Results are present in GPG/KEGG_Pathway_Maps/----------------------------------------------------'
		echo '   Finished downloading all the Pathway Maps from the KEGG database---------------------------------'
elif [ $STEP_1 == 0 ] # Command1 will be skipped
	then
		echo '1)  Pathway Maps are already downloaded in GPG/KEGG_Pathway_Maps/-----------------------------------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command2 - Make a list of the names of the Pathway Maps i.e., the filenames storing the Pathway Maps
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_2 == 1 ] # Command2 will be executed
	then
		echo '2)  Listing the names of the Pathway Maps-----------------------------------------------------------'
		command2='cd '$Path
		$command2
		command2='python Kegg_Pathway_Listing.py'	
		echo '   '$command2
		$command2
		cd ~-
		echo '   Results are present in GPG/KEGG_Pathway_Maps/----------------------------------------------------'
		echo '   Finished listing the names of the Pathway Maps---------------------------------------------------'
elif [ $STEP_2 == 0 ] # Command2 will be skipped	
	then
		echo '2)  The names of the Pathway Maps are already listed in GPG/KEGG_Pathway_Maps/----------------------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command3 - Extract nodes and edges from the KEGG Pathway Maps
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_3 == 1 ] # Command3 will be executed
	then
		echo '3)  Extracting nodes and edges from the KEGG Pathway Maps-------------------------------------------'
		command3='cd '$Path
		$command3
		command3='python Extract_Nodes_Edges.py'
		echo '   '$command3
		$command3
		cd ~-
		echo '   Results are present in GPG/Nodes_Edges_GPG/------------------------------------------------------'
		echo '   Finished extracting nodes and edges from the KEGG Pathway Maps-----------------------------------'
elif [ $STEP_3 == 0 ] # Command3 will be skipped	
	then
		echo '3)  Information on nodes and edges are extracted from the Pathway Maps in GPG/Nodes_Edges_GPG/------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command4 - Download the information of the nodes of GPG
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_4 == 1 ] # Command4 will be executed
	then
		echo '4)  Downloading information on the nodes of the GPG-------------------------------------------------'
		command4='cd '$Path
		$command4
		command4='python Download_Nodes_Pathway_Maps.py'
		echo '   '$command4
		$command4
		cd ~-
		echo '   Results are present in GPG/Nodes_GPG/-------------------------------------------------------------'
		echo '   Finished downloading information on the nodes from the KEGG website-------------------------------'
elif [ $STEP_4 == 0 ] # Command4 will be skipped	
	then
		echo '4)  GPG node information is already downloaded in GPG/Nodes_GPG/------------------------------------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command5 - Count the number of files present in 'GPG/Nodes_GPG'
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_5 == 1 ] # Command5 will be executed
	then
		echo '5)  Counting the number of files of GPG/Nodes_GPG---------------------------------------------------'
		command5='cd '$Path
		$command5
		command5='python Count_No_Of_Files_Nodes_GPG.py'
		echo '   '$command5
		$command5
		cd ~-
		echo '   Results are present in GPG/Nodes_GPG/noOfFiles.txt-----------------------------------------------'
		echo '   Finished counting the number of files of GPG/Nodes_GPG-------------------------------------------'
elif [ $STEP_5 == 0 ] # Command5 will be skipped	
	then
		echo '5)  Count of the number of files in GPG/Nodes_GPG is already present in GPG/Nodes_GPG/noOfFiles.txt-'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command6 - Extract the UniProt IDs of the nodes of GPG present in 'GPG/Nodes_GPG'
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_6 == 1 ] # Command6 will be executed
	then
		echo '6)  Extracting the UniProt IDs of the nodes of the GPG----------------------------------------------'
		command6='cd '$Path
		$command6
		command6='javac Extract_Uniprot_Ids_Nodes_Of_GPG.java'
		echo '   '$command6
		$command6
		command6='java Extract_Uniprot_Ids_Nodes_Of_GPG'
		echo '   '$command6
		$command6
		cd ~-
		echo '   Results are present in GPG/Uniprot_Ids_GPG/IDs.txt-----------------------------------------------'
		echo '   Finished extracting the UniProt IDs of the nodes of GPG------------------------------------------'
elif [ $STEP_6 == 0 ] # Command6 will be skipped	
	then
		echo '6)  UniProt IDs of the nodes of GPG is already present in GPG/Uniprot_Ids_GPG/IDs.txt---------------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command7 - Identify the direct edges of GPG
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_7 == 1 ] # Command7 will be executed
	then
		echo '7)  Extracting the direct edges of GPG--------------------------------------------------------------'
		command7='cd '$Path
		$command7
		command7='javac GPG_Direct_Edges.java'
		echo '   '$command7
		$command7
		command7='java GPG_Direct_Edges'
		echo '   '$command7
		$command7
		cd ~-
		echo '   Results are present in GPG/GPG_Direct_Edges/GPG_DiEdges.txt--------------------------------------'
		echo '   Finished extracting the direct edges of GPG------------------------------------------------------'
elif [ $STEP_7 == 0 ] # Command7 will be skipped	
	then
		echo '7)  The direct edges of GPG is already present in GPG/GPG_Direct_Edges/GPG_DiEdges.txt--------------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command8 - Construct GPG
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_8 == 1 ] # Command8 will be executed
	then
		echo '8)  Constructing GPG--------------------------------------------------------------------------------'
		command8='cd '$Path
		$command8
		command8='python Construct_GPG.py'
		echo '   '$command8
		$command8
		cd ~-
		echo '   Results are present in GPG/GPG_Edges/GPG.txt-----------------------------------------------------'
		echo '   Finished constructing the GPG--------------------------------------------------------------------'
elif [ $STEP_8 == 0 ] # Command8 will be skipped	
	then
		echo '8)  GPG is already present in GPG/GPG_Edges/GPG.txt-------------------------------------------------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Phase2 - PPID construction
# ----------------------------------------------------------------------------------------------------------------
echo 
echo 'B)  PPID Construction-------------------------------------------------------------------------------'
echo

STEP_9=0 # Set STEP_9 to 1 if you want to execute command9

STEP_10=0 # Set STEP_10 to 1 if you want to execute command10

# ----------------------------------------------------------------------------------------------------------------
# Command9 - Remove the obsolete proteins as per UniProt from the DIP database
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_9 == 1 ] # Command9 will be executed
	then
		echo '9)  Removing the obsolete proteins as per UniProt from DIP data-------------------------------------'
		command9='cd '$Path1
		$command9
		command9='javac Remove_Uniprot_Obsolete_Proteins.java'
		echo '   '$command9
		$command9
		command9='java Remove_Uniprot_Obsolete_Proteins'
		echo '   '$command9
		$command9
		cd ~-
		echo '   Results are present in PPID/Reduced_DIP/DIP_After_Removing_Uniprot_Obsolete_Proteins.txt---------'
		echo '   Finished removing the obsolete proteins from DIP-------------------------------------------------'
elif [ $STEP_9 == 0 ] # Command9 will be skipped	
	then
		echo '9)  Filtered DIP is present in PPID/Reduced_DIP/DIP_After_Removing_Uniprot_Obsolete_Proteins.txt----'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command10 - Construct PPID
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_10 == 1 ] # Command10 will be executed
	then
		echo '10) Extracting the nodes and edges of PPID----------------------------------------------------------'
		command10='cd '$Path1
		$command10
		command10='javac Extract_Nodes_Edges_PPID.java'
		echo '   '$command10
		$command10
		command10='java Extract_Nodes_Edges_PPID'
		echo '   '$command10
		$command10
		cd ~-
		echo '   Results are present in PPID/Nodes_Edges_PPID/Nodes.txt and PPID/Nodes_Edges_PPID/Edges.txt-------'
		echo '   Finished constructing PPID-----------------------------------------------------------------------'
elif [ $STEP_10 == 0 ] # Command10 will be skipped	
	then
		echo '10) PPID is present in PPID/Nodes_Edges_PPID/Nodes.txt and PPID/Nodes_Edges_PPID/Edges.txt----------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Phase3 - GPG+PPID Construction 
# ----------------------------------------------------------------------------------------------------------------
echo 
echo 'C)  GPG+PPID Construction---------------------------------------------------------------------------'
echo

STEP_11=0 # Set STEP_11 to 1 if you want to execute command11

# ----------------------------------------------------------------------------------------------------------------
# Command11 - Construct GPG+PPID
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_11 == 1 ] # Command11 will be executed
	then
		echo '11) Combining GPG and PPID--------------------------------------------------------------------------'
		command11='cd '$Path2
		$command11
		command11='javac Construct_GPG_PPID.java'
		echo '   '$command11
		$command11
		command11='java Construct_GPG_PPID'
		echo '   '$command11
		$command11
		cd ~-
		echo '   Results are present in GPG_And_PPID/GPG_PPID/GPG_PPID.txt----------------------------------------'
		echo '   Finished combining GPG and PPID------------------------------------------------------------------'
elif [ $STEP_11 == 0 ] # Command11 will be skipped	
	then
		echo '11) GPG+PPID is already present in GPG_And_PPID/GPG_PPID/GPG_PPID.txt-------------------------------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Phase4 - PPII Construction 
# ----------------------------------------------------------------------------------------------------------------
echo 
echo 'D)  PPII Construction-------------------------------------------------------------------------------'
echo

STEP_12=0 # Set STEP_12 to 1 if you want to execute command12

STEP_13=0 # Set STEP_13 to 1 if you want to execute command13

STEP_14=0 # Set STEP_14 to 1 if you want to execute command14

STEP_15=0 # Set STEP_15 to 1 if you want to execute command15

STEP_16=0 # Set STEP_16 to 1 if you want to execute command16

STEP_17=0 # Set STEP_17 to 1 if you want to execute command17

# ----------------------------------------------------------------------------------------------------------------
# Command12 - Extract only proteins and taxids from IntAct Database
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_12 == 1 ] # Command12 will be executed
	then
		echo '12) Extracting proteins and taxids from IntAct Database---------------------------------------------'
		command12='cd '$Path3
		$command12
		command12='python Extract_Proteins_And_Taxids.py'
		echo '   '$command12
		$command12
		cd ~-
		echo '   Results are present in PPII/Reduced_IntAct/Reduced_IntAct.txt------------------------------------'
		echo '   Finished extracting proteins and taxids from IntAct----------------------------------------------'
elif [ $STEP_12 == 0 ] # Command12 will be skipped	
	then
		echo '12) Reduced IntAct database is already present in PPII/Reduced_IntAct/Reduced_IntAct.txt------------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command13 - Extract PPIs of E. coli from IntAct Database
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_13 == 1 ] # Command13 will be executed
	then
		echo '13) Extracting PPIs of E. coli from IntAct Database-------------------------------------------------'
		command13='cd '$Path3
		$command13
		command13='python Extract_Interactions_Ecoli.py'
		echo '   '$command13
		$command13
		cd ~-
		echo '   Results are present in PPII/Interactions_Ecoli/Ecoli_PPIs.txt------------------------------------'
		echo '   Finished extracting PPIs of E. coli from IntAct--------------------------------------------------'
elif [ $STEP_13 == 0 ] # Command13 will be skipped	
	then
		echo '13) E. coli PPIs from IntAct is already present in PPII/Interactions_Ecoli/Ecoli_PPIs.txt-----------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command14 - Count nodes in PPII
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_14 == 1 ] # Command14 will be executed
	then
		echo '14) Counting nodes of PPII--------------------------------------------------------------------------'
		command14='cd '$Path3
		$command14
		command14='python Count_Nodes_PPII.py'
		echo '   '$command14
		$command14
		cd ~-
		echo '   Results are present in PPII/Interactions_Ecoli/noOfNodes.txt-------------------------------------'
		echo '   Finished counting nodes of PPII------------------------------------------------------------------'
elif [ $STEP_14 == 0 ] # Command14 will be skipped	
	then
		echo '14) Nodecount of PPII is already present in PPII/Interactions_Ecoli/noOfNodes.txt-------------------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command15 - Extract unweighted edges of PPII
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_15 == 1 ] # Command15 will be executed
	then
		echo '15) Extracting unweighted edges of PPII-------------------------------------------------------------'
		command15='cd '$Path3
		$command15
		command15='python Extract_Unweighted_Edges.py'
		echo '   '$command15
		$command15
		cd ~-
		echo '   Results are present in PPII/Nodes_Edges_PPII/Unweighted_Edges.txt--------------------------------'
		echo '   Finished extracting unweighted edges of PPII-----------------------------------------------------'
elif [ $STEP_15 == 0 ] # Command15 will be skipped	
	then
		echo '15) Unweighted edges of PPII is already present in PPII/Nodes_Edges_PPII/Unweighted_Edges.txt-------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command16 - Extract nodes of PPII
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_16 == 1 ] # Command16 will be executed
	then
		echo '16) Extracting nodes of PPII------------------------------------------------------------------------'
		command16='cd '$Path3
		$command16
		command16='python Extract_Nodes.py'
		echo '   '$command16
		$command16
		cd ~-
		echo '   Results are present in PPII/Nodes_Edges_PPII/Nodes.txt-------------------------------------------'
		echo '   Finished extracting nodes of PPII----------------------------------------------------------------'
elif [ $STEP_16 == 0 ] # Command16 will be skipped	
	then
		echo '16) Nodes of PPII is already present in PPII/Nodes_Edges_PPII/Nodes.txt-----------------------------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command17 - Extract edges of PPII
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_17 == 1 ] # Command17 will be executed
	then
		echo '17) Extracting edges of PPII------------------------------------------------------------------------'
		command17='cd '$Path3
		$command17
		command17='javac Extract_Edges.java'
		echo '   '$command17
		$command17
		command17='java Extract_Edges'
		echo '   '$command17
		$command17
		cd ~-
		echo '   Results are present in PPII/Nodes_Edges_PPII/Edges.txt-------------------------------------------'
		echo '   Finished extracting edges of PPII----------------------------------------------------------------'
elif [ $STEP_17 == 0 ] # Command17 will be skipped	
	then
		echo '17) Edges of PPII is already present in PPII/Nodes_Edges_PPII/Edges.txt-----------------------------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Phase5 - GPG+PPID+PPII Construction 
# ----------------------------------------------------------------------------------------------------------------
echo 
echo 'E)  GPG+PPID+PPII Construction----------------------------------------------------------------------'
echo

STEP_18=0 # Set STEP_18 to 1 if you want to execute command18

# ----------------------------------------------------------------------------------------------------------------
# Command18 - Construct GPG+PPID+PPII
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_18 == 1 ] # Command18 will be executed
	then
		echo '18) Constructing GPG+PPID+PPII----------------------------------------------------------------------'
		command18='cd '$Path4
		$command18
		command18='javac Construct_GPG_PPID_PPII.java'
		echo '   '$command18
		$command18
		command18='java Construct_GPG_PPID_PPII'
		echo '   '$command18
		$command18
		cd ~-
		echo '   Results are present in GPG_PPID_PPII/GPG_PPID_PPII.txt-------------------------------------------'
		echo '   Finished constructing GPG+PPID+PPII--------------------------------------------------------------'
elif [ $STEP_18 == 0 ] # Command18 will be skipped	
	then
		echo '18) GPG+PPID+PPII is already present in GPG_PPID_PPII/GPG_PPID_PPII.txt-----------------------------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Phase6 - PPIM Construction 
# ----------------------------------------------------------------------------------------------------------------
echo 
echo 'F)  PPIM Construction-------------------------------------------------------------------------------'
echo

STEP_19=0 # Set STEP_19 to 1 if you want to execute command19

STEP_20=0 # Set STEP_20 to 1 if you want to execute command20

STEP_21=0 # Set STEP_21 to 1 if you want to execute command21

STEP_22=0 # Set STEP_22 to 1 if you want to execute command22

STEP_23=0 # Set STEP_23 to 1 if you want to execute command23

STEP_24=0 # Set STEP_24 to 1 if you want to execute command24

# ----------------------------------------------------------------------------------------------------------------
# Command19 - Remove missing interactions from MINT database and extract interactions along with their taxids
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_19 == 1 ] # Command19 will be executed
	then
		echo '19) Removing missing interactions from MINT---------------------------------------------------------'
		command19='cd '$Path5
		$command19
		command19='python Remove_Missing_Interactions.py'
		echo '   '$command19
		$command19
		cd ~-
		echo '   Results are present in PPIM/Reduced_MINT/Reduced_MINT.txt----------------------------------------'
		echo '   Finished removing missing interactions from MINT-------------------------------------------------'
elif [ $STEP_19 == 0 ] # Command19 will be skipped	
	then
		echo '19) Reduced MINT is already present in PPIM/Reduced_MINT/Reduced_MINT.txt---------------------------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command20 - Extract PPIs of E. coli from MINT Database
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_20 == 1 ] # Command20 will be executed
	then
		echo '20) Extracting PPIs of E. coli from MINT------------------------------------------------------------'
		command20='cd '$Path5
		$command20
		command20='python Extract_Interactions_Ecoli.py'
		echo '   '$command20
		$command20
		cd ~-
		echo '   Results are present in PPIM/Interactions_Ecoli/Ecoli_PPIs.txt------------------------------------'
		echo '   Finished extracting PPIs of E. coli from MINT----------------------------------------------------'
elif [ $STEP_20 == 0 ] # Command20 will be skipped	
	then
		echo '20) E. coli PPIs from MINT are already present in PPIM/Interactions_Ecoli/Ecoli_PPIs.txt------------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command21 - Count nodes of PPIM
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_21 == 1 ] # Command21 will be executed
	then
		echo '21) Counting nodes of PPIM--------------------------------------------------------------------------'
		command21='cd '$Path5
		$command21
		command21='python Count_Nodes_PPIM.py'
		echo '   '$command21
		$command21
		cd ~-
		echo '   Results are present in PPIM/Interactions_Ecoli/noOfNodes.txt-------------------------------------'
		echo '   Finished counting nodes of PPIM------------------------------------------------------------------'
elif [ $STEP_21 == 0 ] # Command21 will be skipped	
	then
		echo '21) Nodecount of PPIM is already present in PPIM/Interactions_Ecoli/noOfNodes.txt-------------------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command22 - Extract unweighted edges of PPIM
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_22 == 1 ] # Command22 will be executed
	then
		echo '22) Extracting unweighted edges of PPIM-------------------------------------------------------------'
		command22='cd '$Path5
		$command22
		command22='python Extract_Unweighted_Edges.py'
		echo '   '$command22
		$command22
		cd ~-
		echo '   Results are present in PPIM/Nodes_Edges_PPIM/Unweighted_Edges.txt--------------------------------'
		echo '   Finished extracting unweighted edges of PPIM-----------------------------------------------------'
elif [ $STEP_22 == 0 ] # Command22 will be skipped	
	then
		echo '22) Unweighted edges of PPIM is already present in PPIM/Nodes_Edges_PPIM/Unweighted_Edges.txt-------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command23 - Extract nodes of PPIM
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_23 == 1 ] # Command23 will be executed
	then
		echo '23) Extracting nodes of PPIM------------------------------------------------------------------------'
		command23='cd '$Path5
		$command23
		command23='python Extract_Nodes.py'
		echo '   '$command23
		$command23
		cd ~-
		echo '   Results are present in PPIM/Nodes_Edges_PPIM/Nodes.txt-------------------------------------------'
		echo '   Finished extracting nodes of PPIM----------------------------------------------------------------'
elif [ $STEP_23 == 0 ] # Command23 will be skipped	
	then
		echo '23) Nodes of PPIM is already present in PPIM/Nodes_Edges_PPIM/Nodes.txt-----------------------------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command24 - Extract edges of PPIM
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_24 == 1 ] # Command24 will be executed
	then
		echo '24) Extracting edges of PPIM------------------------------------------------------------------------'
		command24='cd '$Path5
		$command24
		command24='javac Extract_Edges.java'
		echo '   '$command24
		$command24
		command24='java Extract_Edges'
		echo '   '$command24
		$command24
		cd ~-
		echo '   Results are present in PPIM/Nodes_Edges_PPIM/Edges.txt-------------------------------------------'
		echo '   Finished extracting edges of PPIM----------------------------------------------------------------'
elif [ $STEP_24 == 0 ] # Command24 will be skipped	
	then
		echo '24) Edges of PPIM is already present in PPIM/Nodes_Edges_PPIM/Edges.txt-----------------------------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Phase7 - GPG+PPID+PPII+PPIM Construction 
# ----------------------------------------------------------------------------------------------------------------
echo 
echo 'G)  GPG+PPID+PPII+PPIM Construction-----------------------------------------------------------------'
echo

STEP_25=0 # Set STEP_25 to 1 if you want to execute command25

# ----------------------------------------------------------------------------------------------------------------
# Command25 - Construct GPG+PPID+PPII+PPIM
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_25 == 1 ] # Command25 will be executed
	then
		echo '25) Constructing GPG+PPID+PPII+PPIM-----------------------------------------------------------------'
		command25='cd '$Path6
		$command25
		command25='javac Construct_GPG_PPID_PPII_PPIM.java'
		echo '   '$command25
		$command25
		command25='java Construct_GPG_PPID_PPII_PPIM'
		echo '   '$command25
		$command25
		cd ~-
		echo '   Results are present in GPG_PPID_PPII_PPIM/GPG_PPID_PPII_PPIM.txt---------------------------------'
		echo '   Finished constructing GPG+PPID+PPII+PPIM---------------------------------------------------------'
elif [ $STEP_25 == 0 ] # Command25 will be skipped	
	then
		echo '25) GPG+PPID+PPII+PPIM is already present in GPG_PPID_PPII_PPIM/GPG_PPID_PPII_PPIM.txt--------------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Phase8 - PPIB Construction 
# ----------------------------------------------------------------------------------------------------------------
echo 
echo 'H)  PPIB Construction-------------------------------------------------------------------------------'
echo

STEP_26=0 # Set STEP_26 to 1 if you want to execute command26

STEP_27=0 # Set STEP_27 to 1 if you want to execute command27

STEP_28=0 # Set STEP_28 to 1 if you want to execute command28

STEP_29=0 # Set STEP_29 to 1 if you want to execute command29

STEP_30=0 # Set STEP_30 to 1 if you want to execute command30

STEP_31=0 # Set STEP_31 to 1 if you want to execute command31

STEP_32=0 # Set STEP_32 to 1 if you want to execute command32

STEP_33=0 # Set STEP_33 to 1 if you want to execute command33

# ----------------------------------------------------------------------------------------------------------------
# Command26 - Extract PPIs of E. coli from BioGRID Database
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_26 == 1 ] # Command26 will be executed
	then
		echo '26) Extracting PPIs of E. coli from BioGRID---------------------------------------------------------'
		command26='cd '$Path7
		$command26
		command26='python Extract_Interactions_Ecoli.py'
		echo '   '$command26
		$command26
		cd ~-
		echo '   Results are present in PPIB/Intermediate_Files/Ecoli_PPIs.txt------------------------------------'
		echo '   Finished extracting PPIs of E. coli from BioGRID-------------------------------------------------'
elif [ $STEP_26 == 0 ] # Command26 will be skipped	
	then
		echo '26) E. coli PPIs from BioGRID are already present in PPIB/Intermediate_Files/Ecoli_PPIs.txt---------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command27 - Download UniProt information of the genes of PPIB
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_27 == 1 ] # Command27 will be executed
	then
		echo '27) Downloading UniProt information of nodes of PPIB------------------------------------------------'
		command27='cd '$Path7
		$command27
		command27='python Extract_UniProtIDs.py'
		echo '   '$command27
		$command27
		cd ~-
		echo '   Nodes are present in PPIB/Nodes_BioGRID----------------------------------------------------------'
		echo '   Nodecount of PPIB is stored in PPIB/Intermediate_Files/noOfNodes.txt-----------------------------'
		echo '   Finished downloading UniProt information of nodes of PPIB----------------------------------------'
elif [ $STEP_27 == 0 ] # Command27 will be skipped	
	then
		echo '27) UniProt information of PPIB nodes is already present in PPIB/Nodes_BioGRID----------------------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command28 - Replace genes by proteins in the PPIs from BioGRID
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_28 == 1 ] # Command28 will be executed
	then
		echo '28) Replacing genes by proteins in the PPIs from BioGRID--------------------------------------------'
		command28='cd '$Path7
		$command28
		command28='python Exchange_Gene_Protein.py'
		echo '   '$command28
		$command28
		cd ~-
		echo '   Genes replaced by proteins and stored in PPIB/Intermediate_Files/Genes_Exchanged_Proteins.txt----'
		echo '   Finished replacing genes by proteins in the PPIs from BioGRID------------------------------------'
elif [ $STEP_28 == 0 ] # Command28 will be skipped	
	then
		echo '28) Genes replaced by proteins and present in PPIB/Intermediate_Files/Genes_Exchanged_Proteins.txt--'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command29 - Extract valid PPIs of E. coli from BioGRID Database
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_29 == 1 ] # Command29 will be executed
	then
		echo '29) Extracting valid PPIs of E. coli from BioGRID---------------------------------------------------'
		command29='cd '$Path7
		$command29
		command29='python Remove_Missing_Interactions.py'
		echo '   '$command29
		$command29
		cd ~-
		echo '   Results are present in PPIB/Interactions_Ecoli/Ecoli_PPIs.txt------------------------------------'
		echo '   Finished extracting valid PPIs of E. coli from BioGRID-------------------------------------------'
elif [ $STEP_29 == 0 ] # Command29 will be skipped	
	then
		echo '29) Valid E. coli PPIs from BioGRID are already present in PPIB/Interactions_Ecoli/Ecoli_PPIs.txt---'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command30 - Count nodes of PPIB
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_30 == 1 ] # Command30 will be executed
	then
		echo '30) Counting nodes of PPIB--------------------------------------------------------------------------'
		command30='cd '$Path7
		$command30
		command30='python Count_Nodes_PPIB.py'
		echo '   '$command30
		$command30
		cd ~-
		echo '   Results are present in PPIB/Interactions_Ecoli/Nodecount.txt-------------------------------------'
		echo '   Finished counting nodes of PPIB------------------------------------------------------------------'
elif [ $STEP_30 == 0 ] # Command30 will be skipped	
	then
		echo '30) Nodecount of PPIB is already present in PPIB/Interactions_Ecoli/Nodecount.txt-------------------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command31 - Extract unweighted edges of PPIB
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_31 == 1 ] # Command31 will be executed
	then
		echo '31) Extracting unweighted edges of PPIB-------------------------------------------------------------'
		command31='cd '$Path7
		$command31
		command31='python Extract_Unweighted_Edges.py'
		echo '   '$command31
		$command31
		cd ~-
		echo '   Results are present in PPIB/Nodes_Edges_PPIB/Unweighted_Edges.txt--------------------------------'
		echo '   Finished extracting unweighted edges of PPIB-----------------------------------------------------'
elif [ $STEP_31 == 0 ] # Command31 will be skipped	
	then
		echo '31) Unweighted edges of PPIB is already present in PPIB/Nodes_Edges_PPIB/Unweighted_Edges.txt-------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command32 - Extract nodes of PPIB
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_32 == 1 ] # Command32 will be executed
	then
		echo '32) Extracting nodes of PPIB------------------------------------------------------------------------'
		command32='cd '$Path7
		$command32
		command32='python Extract_Nodes.py'
		echo '   '$command32
		$command32
		cd ~-
		echo '   Results are present in PPIB/Nodes_Edges_PPIB/Nodes.txt-------------------------------------------'
		echo '   Finished extracting nodes of PPIB----------------------------------------------------------------'
elif [ $STEP_32 == 0 ] # Command32 will be skipped	
	then
		echo '32) Nodes of PPIB is already present in PPIB/Nodes_Edges_PPIB/Nodes.txt-----------------------------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command33 - Extract edges of PPIB
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_33 == 1 ] # Command33 will be executed
	then
		echo '33) Extracting edges of PPIB------------------------------------------------------------------------'
		command33='cd '$Path7
		$command33
		command33='javac Extract_Edges.java'
		echo '   '$command33
		$command33
		command33='java Extract_Edges'
		echo '   '$command33
		$command33
		cd ~-
		echo '   Results are present in PPIB/Nodes_Edges_PPIB/Edges.txt-------------------------------------------'
		echo '   Finished extracting edges of PPIB----------------------------------------------------------------'
elif [ $STEP_33 == 0 ] # Command33 will be skipped	
	then
		echo '33) Edges of PPIB is already present in PPIB/Nodes_Edges_PPIB/Edges.txt-----------------------------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Phase9 - PLG Construction 
# ----------------------------------------------------------------------------------------------------------------
echo 
echo 'I)  PLG Construction--------------------------------------------------------------------------------'
echo

STEP_34=0 # Set STEP_34 to 1 if you want to execute command34

# ----------------------------------------------------------------------------------------------------------------
# Command34 - Construct PLG
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_34 == 1 ] # Command34 will be executed
	then
		echo '34) Constructing PLG--------------------------------------------------------------------------------'
		command34='cd '$Path8
		$command34
		command34='javac Construct_PLG.java'
		echo '   '$command34
		$command34
		command34='java Construct_PLG'
		echo '   '$command34
		$command34
		cd ~-
		echo '   Results are present in PLG/PLG.txt---------------------------------------------------------------'
		echo '   Finished constructing PLG------------------------------------------------------------------------'
elif [ $STEP_34 == 0 ] # Command34 will be skipped	
	then
		echo '34) PLG is already present in PLG/PLG.txt-----------------------------------------------------------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Phase10 - Filtering PLG wrt UniProt
# ----------------------------------------------------------------------------------------------------------------
echo 
echo 'J)  Filtering PLG wrt UniProt-----------------------------------------------------------------------'
echo

STEP_35=0 # Set STEP_35 to 1 if you want to execute command35

STEP_36=0 # Set STEP_36 to 1 if you want to execute command36

STEP_37=0 # Set STEP_37 to 1 if you want to execute command37

# ----------------------------------------------------------------------------------------------------------------
# Command35 - Downloading UniProt files for proteins (nodes) of PLG
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_35 == 1 ] # Command35 will be executed
	then
		echo '35) Downloading UniProt files for proteins (nodes) of PLG-------------------------------------------'
		command35='cd '$Path9
		$command35
		command35='python Extract_MolecularWeight.py'
		echo '   '$command35
		$command35
		cd ~-
		echo '   Results are present in PLG_Filtering/MolecularWeight_From_UniProt--------------------------------'
		echo '   Finished downloading UniProt files for proteins (nodes) of PLG-----------------------------------'
elif [ $STEP_35 == 0 ] # Command35 will be skipped	
	then
		echo '35) UniProt files for proteins of PLG is present in PLG_Filtering/MolecularWeight_From_UniProt------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command36 - Extracting molecular weights and calculating volume, surface area of filtered PLG nodes
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_36 == 1 ] # Command36 will be executed
	then
		echo '36) Extracting filtered PLG nodes after removing obsolete ones as per UniProt-----------------------'
		command36='cd '$Path9
		$command36
		command36='python Calculate_Volume_SurfaceArea.py'
		echo '   '$command36
		$command36
		cd ~-
		echo '   Mol wt, volume present in PLG_Filtering/Volume_SA_Filtered_PLG_Nodes/MolecularWeight_Vol.txt-----'
		echo '   Surface area present in PLG_Filtering/Volume_SA_Filtered_PLG_Nodes/Surface_Area.txt--------------'
		echo '   Filtered PLG nodes present in PLG_Filtering/Filtered_PLG/Nodes.txt-------------------------------'
		echo '   Finished extracting PLG nodes after removing obsolete ones as per UniProt------------------------'
elif [ $STEP_36 == 0 ] # Command36 will be skipped	
	then
		echo '36) Filtered PLG nodes is present in PLG_Filtering/Filtered_PLG/Nodes.txt---------------------------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command37 - Extracting the filtered PLG edges after removing the obsolete ones
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_37 == 1 ] # Command37 will be executed
	then
		echo '37) Extracting filtered PLG edges after removing obsolete ones as per UniProt-----------------------'
		command37='cd '$Path9
		$command37
		command37='python Extract_Filtered_PLG.py'
		echo '   '$command37
		$command37
		cd ~-
		echo '   Filtered PLG edges present in PLG_Filtering/Filtered_PLG/Edges.txt-------------------------------'
		echo '   Finished extracting PLG edges after removing obsolete ones as per UniProt------------------------'
elif [ $STEP_37 == 0 ] # Command37 will be skipped	
	then
		echo '37) Filtered PLG edges is present in PLG_Filtering/Filtered_PLG/Edges.txt---------------------------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Phase11 - Clustering PLG
# ----------------------------------------------------------------------------------------------------------------
echo 
echo 'K)  Clustering PLG----------------------------------------------------------------------------------'
echo

STEP_38=0 # Set STEP_38 to 1 if you want to execute command38

STEP_39=0 # Set STEP_39 to 1 if you want to execute command39

# ----------------------------------------------------------------------------------------------------------------
# Command38 - Saving nodes and edges of PLG in pickle files for future processing purposes
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_38 == 1 ] # Command38 will be executed
	then
		echo '38) Generating pickle files for nodes and edges of PLG----------------------------------------------'
		command38='cd '$Path10
		$command38
		command38='python Extract_Nodes_Edges_Pickle_PLG.py'
		echo '   '$command38
		$command38
		cd ~-
		echo '   Pickle file for nodes is present in PLG_Clustering/Intermediate_Files/Nodes_PLG.pickle-----------'
		echo '   Pickle file for edges is present in PLG_Clustering/Intermediate_Files/Edges_PLG.pickle-----------'
		echo '   Finished generating pickle files for nodes and edges of PLG--------------------------------------'
elif [ $STEP_38 == 0 ] # Command38 will be skipped	
	then
		echo '38) Pickle files for nodes, edges of PLG is already present in PLG_Clustering/Intermediate_Files----'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command39 - Clustering PLG by Markov Cluster Algorithm
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_39 == 1 ] # Command39 will be executed
	then
		echo '39) Clustering PLG by MCL---------------------------------------------------------------------------'
		command39='cd '$Path10
		$command39
		command39='python Cluster_By_MCL.py'
		echo '   '$command39
		$command39
		cd ~-
		echo '   Single-node clusters present in PLG_Clustering/MCL_Clusters/Single_Node_Clusters.txt-------------'
		echo '   Multi-node clusters present in PLG_Clustering/MCL_Clusters/out.Shared_Edges.txt.I20--------------'
		echo '   Finished clustering PLG by MCL-------------------------------------------------------------------'
elif [ $STEP_39 == 0 ] # Command39 will be skipped	
	then
		echo '39) Clusters are already present in PLG_Clustering/MCL_Clusters-------------------------------------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Phase12 - GO verification
# ----------------------------------------------------------------------------------------------------------------
echo 
echo 'L)  GO Verification---------------------------------------------------------------------------------'
echo

STEP_40=0 # Set STEP_40 to 1 if you want to execute command40

STEP_43=0 # Set STEP_43 to 1 if you want to execute command43

STEP_44=0 # Set STEP_44 to 1 if you want to execute command44

STEP_45=0 # Set STEP_45 to 1 if you want to execute command45

STEP_46=0 # Set STEP_46 to 1 if you want to execute command46

STEP_47=0 # Set STEP_47 to 1 if you want to execute command47

STEP_48=0 # Set STEP_48 to 1 if you want to execute command48

STEP_49=0 # Set STEP_49 to 1 if you want to execute command49

STEP_50=0 # Set STEP_50 to 1 if you want to execute command50

STEP_51=0 # Set STEP_51 to 1 if you want to execute command51

STEP_52=0 # Set STEP_52 to 1 if you want to execute command52

STEP_53=0 # Set STEP_53 to 1 if you want to execute command53

STEP_54=0 # Set STEP_54 to 1 if you want to execute command54

# ----------------------------------------------------------------------------------------------------------------
# Command40 - Extracting individual clusters from the MCL output
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_40 == 1 ] # Command40 will be executed
	then
		echo '40) Extracting individual clusters from the MCL output----------------------------------------------'
		command40='cd '$Path11
		$command40
		command40='python Separate_Clusters.py'
		echo '   '$command40
		$command40
		cd ~-
		echo '   Individual clusters are present in GO/Individual_Clusters----------------------------------------'
		echo '   Finished extracting individual clusters from the MCL output--------------------------------------'
elif [ $STEP_40 == 0 ] # Command40 will be skipped	
	then
		echo '40) Individual clusters are already present in GO/Individual_Clusters-------------------------------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command41 - Splitting bigger cluster files into smaller files as supported by Frela
# ----------------------------------------------------------------------------------------------------------------

echo '41) Use GO/Code/Split_Cluster_Files.py and manually break big cluster files and use Frela-----------'

# ----------------------------------------------------------------------------------------------------------------
# Command42 - Merging the Frela output of the split cluster files into a single output file
# ----------------------------------------------------------------------------------------------------------------

echo '42) Use GO/Code/Merge_Cluster_Files.py and manually merge split cluster files-----------------------'

# ----------------------------------------------------------------------------------------------------------------
# Command43 - Constructing FSM containing the combined FS value
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_43 == 1 ] # Command43 will be executed
	then
		echo '43) Constructing FSM containing the combined FS value-----------------------------------------------'
		command43='cd '$Path11
		$command43
		command43='python Get_FSM_Combined.py'
		echo '   '$command43
		$command43
		cd ~-
		echo '   FSM_Combined is present in GO/Functional_Similarity_Matrix/FSM_Combined.tsv----------------------'
		echo '   Finished constructing FSM containing the combined FS value---------------------------------------'
elif [ $STEP_43 == 0 ] # Command43 will be skipped	
	then
		echo '43) FSM_Combined is already present in GO/Functional_Similarity_Matrix/FSM_Combined.tsv-------------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command44 - Constructing FSM containing the FS value for a particular ontology
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_44 == 1 ] # Command44 will be executed
	then
		echo '44) Constructing FSM containing separate FS value---------------------------------------------------'
		command44='cd '$Path11
		$command44
		command44='python Get_FSM_Separate.py'
		echo '   '$command44
		$command44
		cd ~-
		echo '   FSM_BP is present in GO/Functional_Similarity_Matrix/FSM_BP.tsv----------------------------------'
		echo '   FSM_CC is present in GO/Functional_Similarity_Matrix/FSM_CC.tsv----------------------------------'
		echo '   FSM_MF is present in GO/Functional_Similarity_Matrix/FSM_MF.tsv----------------------------------'
		echo '   Finished constructing FSM containing the separate FS value---------------------------------------'
elif [ $STEP_44 == 0 ] # Command44 will be skipped	
	then
		echo '44) Separate FSMs are already present in GO/Functional_Similarity_Matrix/---------------------------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command45 - Extracting the list of obsolute proteins as per Frela
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_45 == 1 ] # Command45 will be executed
	then
		echo '45) Extracting the list of obsolute proteins as per Frela-------------------------------------------'
		command45='cd '$Path11
		$command45
		command45='python Extract_Obsolute_Frela.py'
		echo '   '$command45
		$command45
		cd ~-
		echo '   FSM_All is present in GO/Functional_Similarity_Matrix/FSM_All.tsv--------------------------------'
		echo '   List of Frela obsolute proteins present in GO/Obsolute_Proteins/Frela_Obsolute.txt---------------'
		echo '   Finished extracting the list of obsolute proteins as per Frela-----------------------------------'
elif [ $STEP_45 == 0 ] # Command45 will be skipped	
	then
		echo '45) Frela obsolute proteins are present in GO/Obsolute_Proteins/Frela_Obsolute.txt------------------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command46 - Extracting GO information of PLG proteins from UniProt dump
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_46 == 1 ] # Command46 will be executed
	then
		echo '46) Extracting GO information of PLG proteins from UniProt dump-------------------------------------'
		command46='cd '$Path11
		$command46
		command46='python Extract_Ecoli_GO_Uniprot.py'
		echo '   '$command46
		$command46
		cd ~-
		echo '   Extracted GO information of PLG proteins present in GO/Input/Ecoli_GO.txt------------------------'
		echo '   Finished extracting GO information of PLG proteins from UniProt dump-----------------------------'
elif [ $STEP_46 == 0 ] # Command46 will be skipped	
	then
		echo '46) GO information of PLG proteins is already present in GO/Input/Ecoli_GO.txt----------------------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command47 - Extracting GO hierarchies of PLG proteins from GO database
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_47 == 1 ] # Command47 will be executed
	then
		echo '47) Extracting GO hierarchies of PLG proteins from GO database--------------------------------------'
		command47='cd '$Path11
		$command47
		command47='python Extract_GO_Hierarchy.py'
		echo '   '$command47
		$command47
		cd ~-
		echo '   GO hierarchies of PLG proteins present in GO/Individual_Clusters_GO_Hierarchies------------------'
		echo '   Finished extracting GO hierarchies of PLG proteins from GO database------------------------------'
elif [ $STEP_47 == 0 ] # Command47 will be skipped	
	then
		echo '47) GO hierarchies of PLG proteins present in GO/Individual_Clusters_GO_Hierarchies-----------------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command48 - Extracting obsolute PLG proteins as per GO database
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_48 == 1 ] # Command48 will be executed
	then
		echo '48) Extracting obsolute PLG proteins as per GO database---------------------------------------------'
		command48='cd '$Path11
		$command48
		command48='python Extract_Obsolute_GO.py'
		echo '   '$command48
		$command48
		cd ~-
		echo '   Obsolute PLG proteins as per GO database are present in GO/Obsolute_Proteins/GO_Obsolute.txt-----'
		echo '   Finished extracting obsolute PLG proteins as per GO database-------------------------------------'
elif [ $STEP_48 == 0 ] # Command48 will be skipped	
	then
		echo '48) Obsolute PLG proteins as per GO database are present in GO/Obsolute_Proteins/GO_Obsolute.txt----'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command49 - Generating the final list of obsolute proteins by merging information from GO and Frela
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_49 == 1 ] # Command49 will be executed
	then
		echo '49) Generating the final list of obsolute proteins--------------------------------------------------'
		command49='cd '$Path11
		$command49
		command49='python Merge_GO_Frela_Obsolute.py'
		echo '   '$command49
		$command49
		cd ~-
		echo '   Obsolute proteins as per GO and Frela are present in GO/Obsolute_Proteins/GO_Frela_Obsolute.txt--'
		echo '   Finished generating the final list of obsolute proteins------------------------------------------'
elif [ $STEP_49 == 0 ] # Command49 will be skipped	
	then
		echo '49) Obsolute proteins as per GO and Frela are present in GO/Obsolute_Proteins/GO_Frela_Obsolute.txt-'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command50 - Removing the obsolute proteins from the clusters
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_50 == 1 ] # Command50 will be executed
	then
		echo '50) Removing the obsolute proteins from the clusters------------------------------------------------'
		command50='cd '$Path11
		$command50
		command50='python Remove_Obsolute_Modify_Clusters.py'
		echo '   '$command50
		$command50
		cd ~-
		echo '   Modified clusters are present in GO/Clusters_After_Removing_Obsolute_Proteins--------------------'
		echo '   Finished removing the obsolute proteins from the clusters----------------------------------------'
elif [ $STEP_50 == 0 ] # Command50 will be skipped	
	then
		echo '50) Modified clusters are present in GO/Clusters_After_Removing_Obsolute_Proteins-------------------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command51 - Removing empty clusters
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_51 == 1 ] # Command51 will be executed
	then
		echo '51) Removing empty clusters-------------------------------------------------------------------------'
		command51='cd '$Path11
		$command51
		command51='python Refresh_Clusters.py'
		echo '   '$command51
		$command51
		cd ~-
		echo '   Modified clusters are present in GO/Clusters_After_Removing_Obsolute_Proteins--------------------'
		echo '   Finished removing the empty clusters-------------------------------------------------------------'
elif [ $STEP_51 == 0 ] # Command51 will be skipped	
	then
		echo '51) Clusters for analysis are present in GO/Clusters_After_Removing_Obsolute_Proteins---------------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command52 - Performing statistical analysis on the clusters
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_52 == 1 ] # Command52 will be executed
	then
		echo '52) Performing statistical analysis on the clusters-------------------------------------------------'
		command52='cd '$Path11
		$command52
		command52='python Statistical_Analysis.py'
		echo '   '$command52
		$command52
		cd ~-
		echo '   Statistical analysis is present in GO/Analysis_Output--------------------------------------------'
		echo '   Finished performing statistical analysis on the clusters-----------------------------------------'
elif [ $STEP_52 == 0 ] # Command52 will be skipped	
	then
		echo '52) Statistical analysis is present in GO/Analysis_Output-------------------------------------------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command53 - Generating boxplot of statistical analysis on the clusters
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_53 == 1 ] # Command53 will be executed
	then
		echo '53) Generating boxplot of statistical analysis on the clusters--------------------------------------'
		command53='cd '$Path11
		$command53
		command53='python -W ignore BoxPlot.py'
		echo '   '$command53
		$command53
		cd ~-
		echo '   Boxplots are present in GO/BoxPlots--------------------------------------------------------------'
		echo '   Finished generating boxplot of statistical analysis on the clusters------------------------------'
elif [ $STEP_53 == 0 ] # Command53 will be skipped	
	then
		echo '53) Boxplots are present in GO/BoxPlots-------------------------------------------------------------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command54 - Counting the number of validated clusters
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_54 == 1 ] # Command54 will be executed
	then
		echo '54) Counting the number of validated clusters-------------------------------------------------------'
		command54='cd '$Path11
		$command54
		command54='python Count_Validated_Clusters.py'
		echo '   '$command54
		$command54
		cd ~-
		echo '   Validated clusters are present in GO/Analysis_Output/Analysis.tsv--------------------------------'
		echo '   Finished counting the number of validated clusters-----------------------------------------------'
elif [ $STEP_54 == 0 ] # Command54 will be skipped	
	then
		echo '54) Validated clusters are present in GO/Analysis_Output/Analysis.tsv-------------------------------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Phase13 - Computational Cell Division
# ----------------------------------------------------------------------------------------------------------------
echo 
echo 'M)  Computational Cell Division---------------------------------------------------------------------'
echo

STEP_55=0 # Set STEP_55 to 1 if you want to execute command55

STEP_56=0 # Set STEP_56 to 1 if you want to execute command56

STEP_58=0 # Set STEP_58 to 1 if you want to execute command58

STEP_60=0 # Set STEP_60 to 1 if you want to execute command60

STEP_62=0 # Set STEP_62 to 1 if you want to execute command62

STEP_63=0 # Set STEP_63 to 1 if you want to execute command63

# ----------------------------------------------------------------------------------------------------------------
# Command55 - Counting interconnections among clusters
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_55 == 1 ] # Command55 will be executed
	then
		echo '55) Counting interconnections among clusters--------------------------------------------------------'
		command55='cd '$Path12
		$command55
		command55='python Extract_Shared_Info.py'
		echo '   '$command55
		$command55
		cd ~-
		echo '   Shared info is present in Cell_Division/Shared_Info/Shared_Clusters.txt--------------------------'
		echo '   Finished counting interconnections among clusters------------------------------------------------'
elif [ $STEP_55 == 0 ] # Command55 will be skipped	
	then
		echo '55) Shared info is present in Cell_Division/Shared_Info/Shared_Clusters.txt-------------------------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command56 - Generating distance matrix
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_56 == 1 ] # Command56 will be executed
	then
		echo '56) Generating distance matrix----------------------------------------------------------------------'
		command56='cd '$Path12
		$command56
		command56='python Generate_Distance_Matrix.py'
		echo '   '$command56
		$command56
		cd ~-
		echo '   Distance matrix is present in Cell_Division/Distance_Matrix/Dist_Mat.csv-------------------------'
		echo '   Finished generating distance matrix--------------------------------------------------------------'
elif [ $STEP_56 == 0 ] # Command56 will be skipped	
	then
		echo '56) Distance matrix is present in Cell_Division/Distance_Matrix/Dist_Mat.csv------------------------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command57 - Determine spatial distribution of clusters using PCoA in R
# ----------------------------------------------------------------------------------------------------------------

echo '57) Use Cell_Division/Code/PCoA.R and determine spatial distribution of the clusters----------------'
echo '    Spatial coordinates of the clusters are present in Cell_Division/PCoA/PCoA.csv------------------'

# ----------------------------------------------------------------------------------------------------------------
# Command58 - Processing the file storing the cluster coordinates
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_58 == 1 ] # Command58 will be executed
	then
		echo '58) Processing the file storing the cluster coordinates---------------------------------------------'
		command58='cd '$Path12
		$command58
		command58='python PCoA_Processing.py'
		echo '   '$command58
		$command58
		cd ~-
		echo '   The processed PCoA file is stored in Cell_Division/PCoA/PCoA_Processed---------------------------'
		echo '   Finished processing the file storing the cluster coordinates-------------------------------------'
elif [ $STEP_58 == 0 ] # Command58 will be skipped	
	then
		echo '58) The processed PCoA file is stored in Cell_Division/PCoA/PCoA_Processed--------------------------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command59 - Getting the imput files ready for Voronoi Diagram construction
# ----------------------------------------------------------------------------------------------------------------

echo '59) Modify the input parameters of Cell_Division/Voro/examples/CCD/import.cc------------------------'

# ----------------------------------------------------------------------------------------------------------------
# Command60 - Voronoi Diagram construction
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_60 == 1 ] # Command60 will be executed
	then
		echo '60) Construction of the Voronoi Diagram-------------------------------------------------------------'
		command60='cd '$Path13
		$command60
		command60='make'
		echo '   '$command60
		$command60
		command60='./import'
		echo '   '$command60
		$command60
		cd ~-
		echo '   The geometry of Voronoi regions is present in Cell_Division/Voro/examples/CCD/Voronoi_Regions.pov'
		echo '   The geometry of Voronoi seeds is present in Cell_Division/Voro/examples/CCD/Voronoi_Seeds.pov----'
		echo '   Finished constructing the Voronoi Diagram--------------------------------------------------------'
elif [ $STEP_60 == 0 ] # Command60 will be skipped	
	then
		echo '60) The geometry of Voronoi Diagram is present in Cell_Division/Voro/examples/CCD/------------------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command61 - Getting the imput files ready for Voronoi Diagram visualization
# ----------------------------------------------------------------------------------------------------------------

echo '61) Modify the input parameters of Cell_Division/Voro/examples/CCD/import.pov-----------------------'

# ----------------------------------------------------------------------------------------------------------------
# Command62 - Voronoi Diagram Visualization
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_62 == 1 ] # Command62 will be executed
	then
		echo '62) Visualization of the Voronoi Diagram------------------------------------------------------------'
		command62='cd '$Path13
		$command62
		command62='povray +W900 +H600 +A0.3 +OVD import.pov Output_File_Type=J'
		echo '   '$command62
		$command62
		cd ~-
		echo '   Visualization of the Voronoi Diagram is present in Cell_Division/Voro/examples/CCD/VD.jpg--------'
		echo '   Finished visualization of the Voronoi Diagram----------------------------------------------------'
elif [ $STEP_62 == 0 ] # Command62 will be skipped	
	then
		echo '62) Visualization of the Voronoi Diagram is present in Cell_Division/Voro/examples/CCD/VD.jpg-------'
fi

# ----------------------------------------------------------------------------------------------------------------
# Command63 - Extracting cellular dictionary
# ----------------------------------------------------------------------------------------------------------------

if [ $STEP_63 == 1 ] # Command63 will be executed
	then
		echo '63) Extracting cellular dictionary------------------------------------------------------------------'
		command63='cd '$Path12
		$command63
		command63='python Extract_Cellular_Dictionary.py'
		echo '   '$command63
		$command63
		cd ~-
		echo '   Cellular Dictionary is present in Cell_Division/Cellular_Dictionary/Cellular_Dictionary.txt------'
		echo '   Finished extracting cellular dictionary----------------------------------------------------------'
elif [ $STEP_63 == 0 ] # Command63 will be skipped	
	then
		echo '63) Cellular Dictionary is present in Cell_Division/Cellular_Dictionary/Cellular_Dictionary.txt-----'
fi

echo