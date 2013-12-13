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
