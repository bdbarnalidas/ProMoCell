
// --------------------------------------------------------------------------------------------------------------
// This code removes all those interactions from DIP where the UniProt ID of either of the 2 interacting proteins 
// is absent. 

// Input - The DIP database stored in 'PPID/Input/DIP_Database_Ecoli(K12).txt'.
// Output - The reduced DIP database after removing the obsolete proteins as per UniProt stored in
// 'PPID/Reduced_DIP/DIP_After_Removing_Uniprot_Obsolete_Proteins.txt'.
// --------------------------------------------------------------------------------------------------------------

import java.io.*;
import java.math.*;
import java.util.*;
public class Remove_Uniprot_Obsolete_Proteins {

    public static void main(String[] args) throws IOException, FileNotFoundException
    {	
        BufferedReader br = new BufferedReader(new FileReader("../Input/DIP_Database_Ecoli(K12).txt")); // Input File
        //BufferedReader br2 = new BufferedReader(new FileReader("IDs.txt"));
        /*
        String id = "";
        TreeSet<String> ts = new TreeSet<String>();
        while( (id = br2.readLine()) != null)
        {
        	//System.out.println(id);
        	if(id.length() <= 2)
        	{
        		//System.out.println("HI");
        		continue;
        	}
        	else
        	{
        		String[] str = id.split(" ");
        		for(int i=1;i<str.length;i++)
        		{
        			ts.add(str[i]);
        			//System.out.println(str[i]);
        		}
        	}
        }
        System.out.println("Size : " + ts.size());
        */
        PrintWriter pout = new PrintWriter("../Reduced_DIP/DIP_After_Removing_Uniprot_Obsolete_Proteins.txt");
        
        String text = "";
        int count = 0;
        
        
        //int idmatch = 0;
        TreeSet<String> ct1 = new TreeSet<String>();
        TreeSet<String> ct2 = new TreeSet<String>();
        int edgesct=-1;
        while((text = br.readLine())!= null)
        {
        	String str[] = text.split("\t");
        	//String ans = str[str.length-4];
        	ct1.add(str[0]);
        	ct1.add(str[1]);
        	edgesct++;
        	if(str[0].contains("uniprotkb") && str[1].contains("uniprotkb"))
        	{
        		count++;
        		pout.println(str[0]+"\t"+str[1]);
        		ct2.add(str[0]);
        		ct2.add(str[1]);
        		//String myid1 = str[0].substring(str[0].indexOf("u")+10);
        		//String myid2 = str[1].substring(str[1].indexOf("u")+10);
        		//System.out.println(myid1 +"  "+myid2);
        		//if(ts.contains(myid1) && ts.contains(myid2))
        		//{
        			//System.out.println("YO");
        		//}
        		//System.out.println(stt[0]+"  "+stt[1]+"  "+stt[2]);
        		//System.out.println("###########"+str[0]+"###########"+str[1]);
        	}
            else 
            {
                System.out.println(str[0]+"\t"+str[1]);
            }
        }
        System.out.println("Total Size : "+ct1.size());
        System.out.println("Edges total : "+edgesct);
        System.out.println(ct2.size());
        PrintWriter pout1 = new PrintWriter("../Reduced_DIP/noOfNodes.txt");
        pout1.println(ct2.size());
        pout1.close();
        System.out.println("Reduced : "+count);
        br.close();
        pout.close();
    }

}

