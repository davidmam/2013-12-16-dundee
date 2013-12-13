##Accessions

      import re
      
      accs = "xkn59438", "yhdck2", "eihd39d9", "chdsye847", "hedle3455", "xjhd53e", "45da", "de37dp"
      print("containing the number 5")
      for acc in accs:
          if re.search(r"5", acc):
              print("\t" + acc)
      
      print("containing d or e ")
      for acc in accs:
          if re.search(r"(d|e)", acc):
              print("\t" + acc)
      
      print("containing d followed by e ")
      for acc in accs:
          if re.search(r"d.*e", acc):
              print("\t" + acc)
      
      print("containing d followed by e with a single letter between them ")
      for acc in accs:
          if re.search(r"d.e", acc):
              print("\t" + acc)
      
      print("containing d and e in any order")
      for acc in accs:
          if re.search(r"d.*e", acc) or re.search(r"e.*d", acc):
              print("\t" + acc)
      
      
      print("starting with x or y")
      for acc in accs:
          if re.search(r"^(x|y)", acc):
              print("\t" + acc)
      
      
      print("starting with x or y and ending with e")
      for acc in accs:
          if re.search(r"^(x|y).*e$", acc):
              print("\t" + acc)
      
      
      print("three or more numbers in a row")
      for acc in accs:
          if re.search(r"[0123456789]{3,100}", acc):
              print("\t" + acc)
      
      
      print("three or more numbers in a row, more concisely")
      for acc in accs:
          if re.search(r"\d{3,}", acc):
              print("\t" + acc)
      
      
      print("ends with d and either a, r or p")
      for acc in accs:
          if re.search(r"d[arp]$", acc):
              print("\t" + acc)


##Double digest

      import re
      dna = open("dna.txt").read().rstrip("\n")
      print(str(len(dna)))
      all_cuts = [0]
      
      # add cut positions for AbcI
      for match in re.finditer(r"A[ATGC]TAAT", dna):
          all_cuts.append(match.start() + 3)
      
      # add cut positions for AbcII
      for match in re.finditer(r"GC[AG][AT]TG", dna):
          all_cuts.append(match.start() + 4)
      
      # add the final position
      all_cuts.append(len(dna))
      sorted_cuts = sorted(all_cuts)
      print(sorted_cuts)
      
      
      for i in range(1,len(sorted_cuts)):
          this_cut_position = sorted_cuts[i]
          previous_cut_position = sorted_cuts[i-1]
          fragment_size = this_cut_position - previous_cut_position
          print("one fragment size is  "  + str(fragment_size))
