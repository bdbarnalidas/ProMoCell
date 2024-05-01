
// --------------------------------------------------------------------------------------------------------------
// This code downloads all the pathway maps from KEGG website and stores the pathway maps as individual files.

// Input - The list of all pathway maps (/GPG/Input/KEGG_Pathway_Maps_eco.txt).
// Output - Pathway maps for 'eco' in '/GPG/KEGG_Pathway_Maps'.
// --------------------------------------------------------------------------------------------------------------


import java.io.*;
import java.net.URL;


public class Download_Pathway_Maps{
  public static void main(String arg[]) throws Exception,IOException {
	System.setProperty("http.proxyHost", "172.16.2.30");
	System.setProperty("http.proxyPort", "8080");
	String line = null;
	BufferedReader br = new BufferedReader(new FileReader("../Input/KEGG_Pathway_Maps_eco.txt")); // Input filename
	while( ( line = br.readLine() ) != null )  {
	  String[] lineb = line.split("\t");
	  int size = lineb.length;
	  for(int i=0;i<size;i++)
	  {
		  if(lineb[i].contains("path:"))
		  {
			  lineb[i] = lineb[i].replace("path:","");
			  String myurl = "http://rest.kegg.jp/get/"+lineb[i]+"/kgml";
			  URL url = new URL(myurl);
			  try{
			  InputStream IS = url.openConnection().getInputStream();
			  BufferedReader reader = new BufferedReader( new InputStreamReader( IS )  );
			  String line1 = null;
			  String result = "";
			  while( ( line1 = reader.readLine())  != null ) {
			       result = result + line1 +"\n";
			    }
			  String filename = lineb[i]+".txt";
			  PrintWriter pwriter = new PrintWriter("../KEGG_Pathway_Maps/"+filename); // Set output directory to save pathway maps
			  pwriter.print(result);
			  pwriter.close();
			  System.out.println(lineb[i]);
			  reader.close();
			  }
			  catch(FileNotFoundException e){
			  	System.out.println(e);
			  }
		  }
	  }
	}
	br.close();
  }
}
