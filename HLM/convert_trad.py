import mafan

with open("hlm_45_tokenized.conll", "r") as inFile:
 with open("hlm_45_tokenized_trad.conll", "w") as outFile:
   for line in inFile:
     if len(line) > 1:
         line = line.strip().split("\t")

         line[1] = mafan.tradify(line[1].decode("utf8")).encode("utf8")
         print >> outFile, "\t".join(line)
     else:
         print >> outFile, ("\n")
#      print(mafan.tradify(line.strip()).encode("utf8"))
 #     print >> outFile, (mafan.tradify(line.strip()).encode("utf8"))

