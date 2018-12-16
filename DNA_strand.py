def DNA_strand(dna):
    d = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    return ''.join([d[e] for e in dna])

print(DNA_strand('ATCGATGC'))