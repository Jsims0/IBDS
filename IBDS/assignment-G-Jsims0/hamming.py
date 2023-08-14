def hamming(sequence_a, sequence_b):
    """calculates the number of different bases between two DNA strings """

    point_mutations = 0
    assert(len(sequence_a) == len(sequence_b)), 'DNA strings must be of equal length'
    for base in range(len(sequence_a)):
            if sequence_a[base] != sequence_b[base]:
                point_mutations +=1

    return point_mutations
