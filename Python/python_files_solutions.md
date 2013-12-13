      
##Splitting genomic DNA      
      
      
      # open the file and read its contents
      dna_file = open("genomic_dna.txt")
      my_dna = dna_file.read()
      
      # extract the different bits of DNA sequence
      exon1 = my_dna[0:62]
      intron = my_dna[62:90]
      exon2 = my_dna[90:10000]
      
      # open the two output files
      coding_file = open("coding_dna.txt", "w")
      noncoding_file = open("noncoding_dna.txt", "w")
      
      # write the sequences to the output files
      coding_file.write(exon1 + exon2)
      noncoding_file.write(intron)
      
      
      
##Writing a FASTA file

      # set the values of all the header variables
      header_1 = "ABC123"
      header_2 = "DEF456"
      header_3 = "HIJ789"
      
      # set the values of all the sequence variables
      seq_1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
      seq_2 = "actgatcgacgatcgatcgatcacgact"
      seq_3 = "ACTGAC-ACTGT—ACTGTA----CATGTG"
      
      # make a new file to hold the output
      output = open("sequences.fasta", "w")
      
      # write the header and sequence for seq1
      output.write('>' + header_1 + '\n' + seq_1 + '\n') 
      
      # write the header and uppercase sequences for seq2
      output.write('>' + header_2 + '\n' + seq_2.upper() + '\n') 
      
      # write the header and sequence for seq3 with hyphens removed
      output.write('>' + header_3 + '\n' + seq_3.replace('-', '') + '\n') 
      
      
##Writing multiple FASTA files

      # set the values of all the header variables 
      header_1 = "ABC123" 
      header_2 = "DEF456" 
      header_3 = "HIJ789" 
       
      # set the values of all the sequence variables 
      seq_1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG" 
      seq_2 = "actgatcgacgatcgatcgatcacgact" 
      seq_3 = "ACTGAC-ACTGT—ACTGTA----CATGTG" 
       
      # make three files to hold the output 
      output_1 = open(header_1 + ".fasta", "w") 
      output_2 = open(header_2 + ".fasta", "w") 
      output_3 = open(header_3 + ".fasta", "w") 
       
      # write one sequence to each output file
      output_1.write('>' + header_1 + '\n' + seq_1 + '\n') 
      output_2.write('>' + header_2 + '\n' + seq_2.upper() + '\n') 
      output_3.write('>' + header_3 + '\n' + seq_3.replace('-', '') + '\n') 
