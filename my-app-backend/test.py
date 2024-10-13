def starTriangle(length):
    for rows in range(length,0,-1):
        print(' '*(length-rows)+'*'*(2*rows-1))

print(f'{starTriangle(9)}')
