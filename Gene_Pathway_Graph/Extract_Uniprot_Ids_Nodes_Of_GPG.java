
// -------------------------------------------------------------------------------------------------------------------
// This code extracts the UniProt IDs of the GPG nodes present in 'GPG/Nodes_GPG'.

// Input - The GPG node information stored in 'GPG/Nodes_GPG'.
// Output - The UniProt IDs of nodes of GPG saved in 'GPG/Uniprot_Ids_GPG/IDs.txt'.
// -------------------------------------------------------------------------------------------------------------------

import java.io.*;
import java.math.*;
import java.util.*;
public class Extract_Uniprot_Ids_Nodes_Of_GPG{

	public static void main(String[] args) throws IOException
	{
        BufferedReader br1 = new BufferedReader(new FileReader("../Nodes_GPG/noOfFiles.txt")); // Input File
        String cntStr = br1.readLine();
        int cnt = Integer.parseInt(cntStr);
        br1.close();
        FileWriter fout = new FileWriter("../Uniprot_Ids_GPG/IDs.txt"); // Output File
        fout.close();

		for(int i=1;i<=cnt;i++)
		{
			System.out.println("++++++++++++  "+i);
			main1(i);
		}
	}
    public static void main1(int file) throws IOException 
    {	
        BufferedReader br = new BufferedReader(new FileReader("../Nodes_GPG/"+Integer.toString(file)+".html")); // Input Folder
        FileWriter fout = new FileWriter("../Uniprot_Ids_GPG/IDs.txt",true); // Output File
        String line = null;
        String text = "";
        while((line = br.readLine())!= null)
        {
        	text = text + line;
        }
        String result = "";
        while(text.contains("http://www.uniprot.org/uniprot/"))
        {
        	//text.indexOf("/uniprot/")
        	//System.out.println(text.indexOf("/uniprot/"));
        	String substr = text.substring(text.indexOf("/uniprot/")+9);
        	//System.out.println();
        	
        	result = result +" "+text.substring(text.indexOf("/uniprot/")+9 , text.indexOf("/uniprot/")+9+ substr.indexOf("\">"));
        	System.out.println(result);
        	text = text.substring(text.indexOf("/uniprot/")+1);
        	//System.out.println(text.length());
        }
        //fout.write(Integer.toString(file)+"\n");
        fout.write(result+"\n");
        fout.close();
    }

}
