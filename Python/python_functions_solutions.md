##Percentage of amino acids part one
      
      def get_aa_percentage(protein, aa):
      	protein = protein.upper()
      	aa = aa.upper()
      	aa_count = protein.count(aa)
      	protein_length = len(protein)
      	percentage = aa_count * 100 / protein_length
      	return percentage
      	
##Percentage of amino acids part two
      
      def get_aa_percentage(protein, aa_list=['A','I','L','M','F','W','Y','V']):
          protein = protein.upper()
          protein_length = len(protein)
          total = 0
          for aa in aa_list:
              aa = aa.upper()
              aa_count = protein.count(aa)
              total = total + aa_count
          percentage = total * 100 / protein_length
          return percentage

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
