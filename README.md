# Genbank2sequin
This python script takes a GenBank format file with associated annotations and produces a the files needed to submit the sequence to GenBank using sequin. 

The python script turns the GenBank  files into the fasta and *.tbl files needed for submission.
1)  Place the python script in the same folder as the GenBank files you want to convert.  
2) In the terminal type: "python genbank2sequin.py”  
3) Produce "template file" using https://submit.ncbi.nlm.nih.gov/genbank/template/submission/. And save the template.sbt file in the same folder as the other files.    
4) In terminal type: "tbl2asn -t template.sbt.txt -p . -M n -Z discrep -r ./sequin"  
5) submit the files to GenBank  

Please note that this script was written for a very specific purpose, and it may not work for you. Feel free to contact me if you need help.
