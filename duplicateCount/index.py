def duplicate_count(text):
    return len(set([ei for i, ei in enumerate(text) if ei in [ej for j, ej in enumerate(text) if j != i]]))

print(duplicate_count('asdf'))