__author__ = 'genes'

def get_next_pos(param):
	xp = []
	x, y = param
	if x-1 >= 0 and matrix[x-1][y] != 'X':
		xp.append((x-1, y))
	if x+1 < N and matrix[x+1][y] != 'X':
		xp.append((x+1, y))
	if y-1 >= 0 and matrix[x][y-1] != 'X':
		xp.append((x, y-1))
	if y+1 < M and matrix[x][y+1] != 'X':
		xp.append((x, y+1))
	return xp


def bfs(start_pos, exit_pos):
	queue, visited = [(0, start_pos, 0)], {}
	while queue:
		location = queue.pop(0)
		if location[1] in visited:
			continue
		visited[location[1]] = True
		next_pos = [i for i in get_next_pos(location[1]) if i not in visited]
		ll = location[2]
		if len(next_pos) > 1:
			ll += 1
		for np in next_pos:
			if np not in visited:
				queue.append((location[0] + 1, np, ll))
		if location[1] == exit_pos:
			if location[2] == K:
				return 'Impressed'
	return 'Oops!'

for _ in xrange(int(raw_input())):
	N, M = map(int, raw_input().split(' '))
	matrix = []
	for i in xrange(N):
		matrix.append(raw_input())
	K = int(raw_input())

	fe, he = (0, 0), (0, 0)
	for i in xrange(N):
		for j in xrange(M):
			if matrix[i][j] == 'M':
				he = (i, j)
			elif matrix[i][j] == '*':
				fe = (i, j)

	print bfs(he, fe)
