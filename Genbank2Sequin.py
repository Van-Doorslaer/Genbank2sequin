from Bio import SeqIO
import re, glob, os

for f in glob.glob("*.gb"):
    ID = f.split(".")[0]
    for r in SeqIO.parse(f,"genbank"):
       #print r.features
       with open(ID+'.fsa', 'w') as fasta, open(ID+".tbl", 'w') as table:
        print >> fasta, ">%s [organism=Human papillomavirus %s]\n%s" %(ID, ID, r.seq)
        print >>table, ">Feature "+ID 
        for (index, feature) in enumerate(r.features):
         if feature.type ==  'CDS':
             m=re.search('\[(\d*)\:(\d*)\]',str(feature.location))
             if m:
                #print feature.qualifiers
                print >>table, "%s\t%s\tgene\n\t\t\tgene\t%s" %(int(m.groups()[0])+1, m.groups()[1],feature.qualifiers['note'][0])
                print >>table, "%s\t%s\tCDS\n\t\t\tproduct\t%s\n\t\t\tgene\t%s\n\t\t\tcodon_start\t1" %(int(m.groups()[0])+1, m.groups()[1], feature.qualifiers['note'][0], feature.qualifiers['note'][0])
                

                
