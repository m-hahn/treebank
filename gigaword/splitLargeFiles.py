import os
inpath = "/u/scr/mhahn/CORPORA/chinese-gigaword-2.0/"
outpath = "/u/scr/mhahn/CORPORA/chinese-gigaword-2.0-split/"

files = os.listdir(inpath)

linecount = 0
filecount = 0
outfile = open(outpath+"/"+"cna_cmn_split_"+str(filecount)+".conllu", "w")
for filename in files:
    print(filename)
    with open(inpath+filename, "r") as infile:
       for line in infile:
           linecount += 1
           if len(line) < 5 and linecount > 500000:
               outfile.close()
               filecount += 1
               linecount = 0
               outfile = open(outpath+"/"+"cna_cmn_split_"+str(filecount)+".conllu", "w")
               print(filecount)
           else:
                print(line.strip(), file=outfile)
    print("", file=outfile)
outfile.close()

