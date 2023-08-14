""" 
unit tests for function parse_fasta_from_lines(lines)

supplied with a list of lines from a FASTA format file
returns a tuple (list of the IDs, list of the sequences)
"""
from fasta_gc_content import parse_fasta_from_lines


def test_single_sequence_one_line():
    ids, seqs = parse_fasta_from_lines(['>id_1','ATAT'])
    assert ids == ['id_1']
    assert seqs == ['ATAT']


def test_single_sequence_two_line():
    ids, seqs = parse_fasta_from_lines(['>foo','A'*80, 'G'*19])
    assert ids == ['foo']
    assert seqs == ['A'*80 + 'G'*19]


def test_three_sequences():
    ids, seqs = parse_fasta_from_lines(['>seq_one','A'*80, 'G'*19, 
                                        '>two', 'A', 
                                        '>three', 'ATATGC'])
    assert ids == ['seq_one', 'two', 'three']
    assert seqs == ['A'*80 + 'G'*19, 'A', 'ATATGC']


