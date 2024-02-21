def wstawienie_sort(L):
    for marker in range(1, len(L)):
        for i in range(marker - 1, -1, -1):
            if L[i] > L[marker]:
                L[i], L[marker] = L[marker], L[i]
                marker -= 1
            else:
                break
    return L


def wstawienie_sort_while(L):
    j = 1
    while j < len(L):
        marker = j
        i = marker - 1
        while i > -1:
            if L[i] > L[marker]:
                L[i], L[marker] = L[marker], L[i]
                marker -= 1
            else:
                break
            i -= 1
        j += 1
    return L


print(wstawienie_sort([5, 6, -1, 0, 4, 7, 2, 3, 102, 88]))
print(wstawienie_sort([i for i in range(10)]))
print(wstawienie_sort([i for i in range(10, 0, -1)]))

print(wstawienie_sort_while([5, 6, -1, 0, 4, 7, 2, 3, 102, 88]))
print(wstawienie_sort_while([i for i in range(10)]))
print(wstawienie_sort_while([i for i in range(10, 0, -1)]))