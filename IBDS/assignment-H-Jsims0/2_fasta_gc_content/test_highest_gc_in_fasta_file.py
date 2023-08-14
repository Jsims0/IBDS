"""
pytest test for function parse_fasta_file(filename)
that supplied with a filename of a FASTA file returns a 
tuple (list of the IDs, list of the sequences).

uses two files in this directory.
"""
import pytest
from fasta_gc_content import highest_gc_in_fasta_file
from test_lines_from_file import filename_in_this_directory


def test_from_simple_fasta_dot_txt():
    simple_fasta_dot_txt = filename_in_this_directory('simple_fasta.txt')
    max_id, max_percent = highest_gc_in_fasta_file(simple_fasta_dot_txt)
    assert max_id == 'minimal_fasta_with_single_short_sequence'
    assert max_percent == pytest.approx(50)

def test_from_rosalind_sample_dot_txt():
    rosalind_sample_dot_txt = filename_in_this_directory('rosalind_sample.txt')
    max_id, max_percent = highest_gc_in_fasta_file(rosalind_sample_dot_txt)
    # From "Sample Output" given at http://rosalind.info/problems/gc/
    assert max_id == 'Rosalind_0808'
    assert max_percent == pytest.approx(60.919540)

def test_function_has_docstring():
    # just check there is one as cannot check that it is human readable
    assert len(highest_gc_in_fasta_file.__doc__) > 0
