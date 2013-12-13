## From amino acids part one

    assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", "M") == 5
    assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", "r") == 10
    assert get_aa_percentage("msrslllrfllfllllpplp", "L") == 50
    assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", "Y") == 0
    
    
## From amino acids part two
    
    assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", ["M"]) == 5
    assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) == 55
    assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']) == 70
    assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP") == 65


## Example from the slides

    from __future__ import division
    
    import unittest
    
    def get_at_content(dna, sig_figs=2):
        length = len(dna)
        a_count = dna.upper().count('A')
        t_count = dna.upper().count('T')
        at_content = (a_count + t_count) / length
        return round(at_content, sig_figs)
    
    
    
    class TestATContent(unittest.TestCase):
    
        def test_single_base(self):
            self.assertEqual(get_at_content("A"), 1)
    
        def test_lowercase(self):
    		self.assertEqual(get_at_content("agtc"), 0.5)
    
    if __name__ == '__main__':
        unittest.main()
