def find_even_index(arr):
    try: 
        return [
            sum([ej for (j, ej) in enumerate(arr) if j < i]) == 
            sum([ej for (j, ej) in enumerate(arr) if j > i]) 
            for (i, ei) in enumerate(arr)
        ].index(True)
    except ValueError:
        return -1

print(find_even_index([1,2,3,4,5,6]))
print(find_even_index([1,2,3,4,3,2,1]))