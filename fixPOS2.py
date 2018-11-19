#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Automatically corrects fine-grained POS whenever universal POS tags were changed during manual correction


POSs = {}

with open("hlm_45_tokenized_trad-tagged.conll", "r") as inFile:
   for line in inFile:
       if len(line) > 3:
           line = line.strip().split("\t")
           if line[3] not in POSs:
               POSs[line[3]] = {}
           if line[4] not in POSs[line[3]]:
              POSs[line[3]][line[4]] = 0
           POSs[line[3]][line[4]] = POSs[line[3]][line[4]] + 1

relevant = {}

for pos in POSs:
#    print(pos, [(x,y) for x, y in POSs[pos].iteritems() if y > 50])
    relevant[pos] = [(x,y) for x, y in POSs[pos].iteritems() if y > 50]


with open("hlm_45_tokenized_trad-tagged.conll", "r") as inFile:
   with open("hlm_45_tokenized_trad-tagged-corrected-1.conll", "r") as inFile2:
     with open("hlm_45_tokenized_trad-tagged-corrected-2.conll", "w") as outFile:
       for line1, line2 in zip(inFile, inFile2):
           if len(line1) < 3:
                 print >> outFile, line1.strip()
           else:
               line1 = line1.strip().split("\t")
               line2 = line2.strip().split("\t")
               if line1[3] != line2[3] and line1[4] == line2[4]:
                   pos = line2[3]
                   if len(relevant[pos]) == 1:
                       line2[4] = relevant[pos][0][0]
                   else:
                       if line2[1] == "了" and line2[3] == "PART":
                           line2[4] = "AS"
                       elif line2[1] in ["罷", "呀", "呢", "咧", "哪", "哦"] and line2[3] == "PART":
                           line2[4] = "SFN"
                       elif line2[1] == "的" and line2[-1] == "_":
                           line2[4] = "DEC"
                       elif line2[1] == "是" and line2[3] == "AUX":
                           line2[4] = "VC"
                       elif line2[1] in ["該", "必要","寧可","只得","不必","未免","何必"] and line2[3] == "AUX":
                           line2[4] = "MD"
                       elif line2[3] == "NOUN":
                           line2[4] = "NN"
                       elif line2[3] == "PUNCT":
                           _ = 5
                       else:
                          line2[4] = "???"
               print >> outFile, ("\t".join(line2))



