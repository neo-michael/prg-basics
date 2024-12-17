def f(array2D):
    row_sums = []
    col_sums = [0] * len(array2D) 
    for y, row in enumerate(array2D):
        row_sums.append(sum(row))
        for x, ele in enumerate(row):
            col_sums[x] += ele
    print(row_sums)
    print(col_sums)
    return row_sums == col_sums

print(f([[3,7,2],[4,2,5],[5,2,1]])) 
print(f([[3,7,2],[4,2,5],[9,2,1]]))