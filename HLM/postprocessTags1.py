#!/usr/bin/env python
# -*- coding: utf-8 -*-

# run some automatic correction informed by manual correction of about 80% 


alwaysTag = {}
alwaysTag["寶釵"] = "PROPN"
alwaysTag["周瑞家"] = "PROPN"
alwaysTag["張材家"] = "PROPN"
alwaysTag["賴大家"] = "PROPN"
alwaysTag["寶玉"] = "PROPN"
alwaysTag["李紈"] = "PROPN"
alwaysTag["鳳姐兒"] = "PROPN"
alwaysTag["平兒"] = "PROPN"
alwaysTag["探春"] = "PROPN"
alwaysTag["鳳姐"] = "PROPN"
alwaysTag["賴嬤嬤"] = "PROPN"
alwaysTag["賈母"] = "PROPN"
alwaysTag["王夫人"] = "PROPN"
alwaysTag["寶釵"] = "PROPN"
alwaysTag["黛玉"] = "PROPN"


alwaysTag["呢"] = "PART"
alwaysTag["的"] = "PART"

alwaysTag["咱們"] = "PRON"

alwaysTag["似的"] = "ADP"

alwaysTag["丫鬟"] = "NOUN"

with open("hlm_45_tokenized_trad-tagged-corrected.conll", "r") as inFile:
   with open("hlm_45_tokenized_trad-tagged-corrected-1.conll", "w") as outFile:
      for line in inFile:
          if len(line) < 3:
              print >> outFile, line.strip()
          else:
             line = line.strip().split("\t")
             if line[1] in alwaysTag:
                 line[3] = alwaysTag[line[1]]
             elif line[1] == "了" and line[3] == "X":
                 line[3] = "PART"
             elif line[1] == "道" and line[3] == "PART":
                 line[3] = "VERB"
             elif line[1] == "多早晚":
                 line[-1] = "何時"
             elif line[1] == "忙":
                 line[3] = "ADV"
             elif line[1] in ["去", "來"] and line[3] == "ADV":
                 line[3] = "VERB"
             elif line[1] == "，":
                 line[3] = "PUNCT"
                 line[4] = ","
             elif line[1] == "”":
                 line[3] = "PUNCT"
                 line[4] = '”'
             elif line[1] == "“":
                 line[3] = "PUNCT"
                 line[4] = "``"
             elif line[1] in ["：", "；"]:
                 line[3] = "PUNCT"
                 line[4] = ":"
             elif line[1] == "‘":
                 line[3] = "PUNCT"
                 line[4] = "``"
             elif line[1] == "’":
                 line[3] = "PUNCT"
                 line[4] = "”"


             print >> outFile, ("\t".join(line))



