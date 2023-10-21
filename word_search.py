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

    def search(self, word):
        rows = len(self.puzzle)
        cols = len(self.puzzle[0])
        ans = None

        def findNextChar(point, word, direction):
            next_point = Point(point.x + direction[0], point.y + direction[1])

            if 0 <= next_point.x < cols and 0 <= next_point.y < rows and self.puzzle[next_point.y][next_point.x] == word[0]:
                remaining_word = word[1:]

                if not remaining_word:
                    return next_point
                
                else:
                    return findNextChar(next_point, remaining_word, direction)

            else:
                return False
        
        for i in range(rows):
            for j in range(cols):
                grid_pointer = Point(j, i)

                if self.puzzle[grid_pointer.y][grid_pointer.x] == word[0]:
                    remaining_word = word[1:]

                    if not remaining_word:
                        ans = (grid_pointer, grid_pointer) 

                    else:
                        for direction in self.moves:
                            next_point = Point(grid_pointer.x + direction[0], grid_pointer.y + direction[1])
             
                            if next_point.x < 0 or next_point.x >= cols or next_point.y < 0 or next_point.y >= rows:
                                continue
                            
                            if self.puzzle[next_point.y][next_point.x] == remaining_word[0]:
                                remainder_word = remaining_word[1:]
                         
                                if not remainder_word:
                                    ans = (grid_pointer, next_point)

                                else:
                                    sol = findNextChar(next_point, remainder_word, direction)
                                    if sol:
                                        ans = (grid_pointer, sol)
                                        return ans
                                    else:
                                        continue
        return ans
    
    
