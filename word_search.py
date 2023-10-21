class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class WordSearch:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.moves = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        self.rows = len(puzzle)
        self.cols = len(puzzle[0])

    def isWithinBounds(self, point):
        return 0 <= point.x < self.cols and 0 <= point.y < self.rows

    def findNextChar(self, point, word, direction):
        next_point = Point(point.x + direction[0], point.y + direction[1])

        if self.isWithinBounds(next_point) and self.puzzle[next_point.y][next_point.x] == word[0]:
            remaining_word = word[1:]

            if not remaining_word:
                return next_point
            
            else:
                return self.findNextChar(next_point, remaining_word, direction)

        else:
            return False
    
    def search(self, word):
        ans = None

        for i in range(self.rows):
            for j in range(self.cols):
                grid_pointer = Point(j, i)

                if self.puzzle[grid_pointer.y][grid_pointer.x] == word[0]:
                    remaining_word = word[1:]

                    if not remaining_word:
                        ans = (grid_pointer, grid_pointer) 

                    else:
                        for direction in self.moves:
                            next_point = Point(grid_pointer.x + direction[0], grid_pointer.y + direction[1])
             
                            if not self.isWithinBounds(next_point):
                                continue
                            
                            elif self.puzzle[next_point.y][next_point.x] == remaining_word[0]:
                                remainder_word = remaining_word[1:]
                         
                                if not remainder_word:
                                    ans = (grid_pointer, next_point)

                                else:
                                    sol = self.findNextChar(next_point, remainder_word, direction)
                                    if sol:
                                        ans = (grid_pointer, sol)
                                        return ans
                                    else:
                                        continue
        return ans
    
    
