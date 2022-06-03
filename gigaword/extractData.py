

import zipfile
import io
import os

encoding = "utf8"
path = "/u/scr/corpora/ldc/2009/LDC2009T14/data/"
counter = 1
# TODO take into account,xin_cmn uses simplified characters. Have to convert before feeding into parser.

for subdir in ["cna_cmn"]: #, "xin_cmn", "zbn_cmn"]:
   files = os.listdir(path+subdir)
   filecounter = 0
   for filename in files:
    filecounter += 1
    sentCount = 0
    print(subdir, filename, filecounter/float(len(files)))
    with open("/u/scr/mhahn/CORPORA/chinese-gigaword-2.0/"+subdir+"_"+filename+".conllu", "w") as outFile:
     with zipfile.ZipFile(path+subdir+"/"+filename) as zfile:
        for name in zfile.namelist():
            with zfile.open(name) as readfile:
                for line in io.TextIOWrapper(readfile, encoding):
  #                  print(repr(line))
                    if line.startswith("<"):
                       if line.startswith("</P>"):
                           sentCount += 1
                           print("", file=outFile)
                           print("# sent_id = "+subdir+"_"+filename+"_"+str(sentCount), file=outFile)
                           counter = 1
                       continue
#                    assert line.endswith(")\n"), line
                    for word in line.strip().split(" "):
#                    line = [ for x in line.strip().split(" ")]
 #                   print(" ".join(line))
 #                   for word in line:
                        x = word
                        try:
                          word = ("(" if x[0] == "(" else x[:x.index("(")])
                          print("\t".join([str(counter), word, word, "_", "_", "_", "_", "_", "_", "_"]), file=outFile)
                          counter += 1
                        except IndexError:
                            print("ERROR "+x)
 
