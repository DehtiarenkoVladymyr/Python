# As for the programming challenge,
# could you please program a pascal triangle
# so that it follows SOLID principles?

n = 7

#Matrix creation
triangle_pascal = []
for x in range(n+1):
    triangle_pascal.append([1]+[0]*n)

#Logic module
for x in range(1, n+1):
    for y in range(1, x+1):
        triangle_pascal [x][y] = triangle_pascal[x-1][y]+triangle_pascal[x-1][y-1]

#Print module
for x in  range(0, n+1):
    for y in range(0, x+1):
        print(triangle_pascal[x][y], end='\t')
    print()

if __name__ == '__main__':
    print(f' Formula: (a+b)**7')