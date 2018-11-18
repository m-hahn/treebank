import mafan

with open("hlm.txt", "r") as inFile:
   data = inFile.read().strip().replace("\n", "")
   data = mafan.split_text(data)
   print(" ".join(data).encode("utf8"))

