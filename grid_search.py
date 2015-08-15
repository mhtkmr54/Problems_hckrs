# Enter your code here. Read input from STDIN. Print output to STDOUT
def find_all(string, substring):
    index = []
    L = len(string)
    l = len(substring)
    for i in xrange(L-l+1):
        if string[i:i+l] == substring:
            index.append(i)
    return index


def find_pattern(grid, pattern):
    R, C = len(grid), len(grid[0])
    r, c = len(pattern), len(pattern[0])
    for i in xrange(R-r+1):
        indeces = find_all(grid[i], pattern[0])        
        if indeces:
            for idx in indeces:
                for j in xrange(i+1, i+r):
                    if pattern[j-i] != grid[j][idx:idx+c]:
                        break
                else:
                    print 'YES'
                    return

    print 'NO'
    return
 
def main():
    T = input()
    for i in xrange(T):
        R, C = map(int, raw_input().strip().split())
        N = R * C
        grid = []
        for k in xrange(R):
            grid.append(raw_input().strip())
        r, c = map(int, raw_input().strip().split())
        pattern = []
        for k in xrange(r):
            pattern.append(raw_input().strip())
        find_pattern(grid, pattern)

if __name__ == '__main__':
    main()
 
