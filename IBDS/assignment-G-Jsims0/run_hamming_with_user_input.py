""" little script to test hamming function prompting user for input """
from hamming import hamming

dna_a = input('Enter first DNA sequence:  ')
dna_b = input('Enter second DNA sequence: ')
hamming_result = hamming(dna_a, dna_b)
print('Hamming distance between the two sequences is', hamming_result)
