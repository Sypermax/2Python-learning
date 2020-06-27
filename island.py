def missing_elements(L):
    start, end = L[0], L[-1]
    return sorted(set(range(start, end + 1)).difference(L))
def find_missing_letter(chars):
    numbers = list(map(ord, chars))
    n = missing_elements(numbers)
    return chr(n[0])
print(find_missing_letter(['a','b','c','d','f']))