import itertools


permutation = list(itertools.combinations('1234', 2))
print(permutation)

permutation = list(itertools.combinations_with_replacement('1234', 4))
print(permutation)

permutation = list(itertools.permutations('212', 3))
print([''.join(i) for i in permutation])



