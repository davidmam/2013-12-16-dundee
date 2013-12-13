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
