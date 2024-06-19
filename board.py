class Board:
    def __init__(self):
        self.board = []

    def createBoard(self, string, sidelength):
        self.board = []  # Reset the board
        i = 0
        for x in range(sidelength):
            row = []
            for y in range(sidelength):
                row.append(string[i])
                i += 1
            self.board.append(row)
        print("Board created:", self.board)  # Debug statement

    def compareprefix(self, prefix, trie):
        return trie.prefixsearch(prefix)

    def getneighbors(self, row, column, visited):
        neighbors = []
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                nx, ny = row + dx, column + dy
                if 0 <= nx < len(self.board) and 0 <= ny < len(self.board[0]) and (nx, ny) not in visited:
                    neighbors.append((nx, ny))
        return neighbors

    def dfs(self, row, column, visited, path, results, trie):
        path.append(self.board[row][column])
        visited.add((row, column))
        word = "".join(path)
        print("Visiting:", (row, column), "Path:", word)  # Debug statement

        if trie.search(word):
            print("Word found:", word)  # Debug statement
            results.add(word)

        for nx, ny in self.getneighbors(row, column, visited):
            if trie.prefixsearch(word + self.board[nx][ny]):
                self.dfs(nx, ny, visited, path, results, trie)

        path.pop()
        visited.remove((row, column))

    def findallpath(self, trie):
        results = set()
        for x in range(len(self.board)):
            for y in range(len(self.board[0])):
                self.dfs(x, y, set(), [], results, trie)
        return results