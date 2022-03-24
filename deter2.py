def sort(A):
    i = 0
    while i < len(A):
        j = i
        while j < len(A):
            while i < len(A) and A[i] == i:
                i += 1
            while j < len(A) and A[j] == j:
                j += 1

            A[i], A[j] = A[j], A[i]

A = [0, 1, 2, 3, 4]
sort(A)
print(A)

A = [1, 0, 3, 2, 4]
sort(A)
print(A)


