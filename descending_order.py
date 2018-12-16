def descending_order(n):
    return int(''.join(sorted(str(n), reverse=True)))

print(descending_order(123456789))