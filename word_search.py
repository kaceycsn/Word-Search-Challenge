class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class WordSearch:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        print(puzzle)
        self.moves = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    def search(self, word):
        rows = len(self.puzzle)
        cols = len(self.puzzle[0])
        ans = []

        def findNextChar(point, word, direction):
            next_point = Point(point.x + direction[0], point.y + direction[1])
            if self.puzzle[next_point.x][next_point.y] == word[0]:
                remaining_word = word[1:]

                if not remaining_word:
                    return next_point
                
                else:
                    return findNextChar(next_point, remaining_word, direction)

            else:
                return False
        
        for i in range(rows):
            for j in range(cols):
                grid_pointer = Point(i, j)
                if self.puzzle[grid_pointer.x][grid_pointer.y] == word[0]:
                    remaining_word = word[1:]

                    if not remaining_word:
                        ans.append([grid_pointer, grid_pointer])

                    else:
                        for move in self.moves:
                            direction = move
                            next_point = Point(grid_pointer.x + move[0], grid_pointer.y + move[1])
                            if self.puzzle[next_point.x][next_point.y] == remaining_word[0]:
                                remainder_word = remaining_word[1:]

                                if not remainder_word:
                                    ans.append([grid_pointer, next_point])

                                else:
                                    sol = findNextChar(next_point, remainder_word, direction)
                                    if sol:
                                        ans.append([grid_pointer, sol])
                                    else:
                                        break
        print(ans)
        return ans
    
    
