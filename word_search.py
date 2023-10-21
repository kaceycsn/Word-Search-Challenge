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
            print("=====FINDNEXTCHAR=====")
            next_point = Point(point.x + direction[0], point.y + direction[1])

            if 0 <= next_point.x < cols and 0 <= next_point.y < rows and self.puzzle[next_point.y][next_point.x] == word[0]:
                remaining_word = word[1:]
                print("MATCHED: ", self.puzzle[next_point.y][next_point.x])
                print("REMAINING WORD: ", remaining_word)

                if not remaining_word:
                    print("NOT REMAINING WORD")
                    return next_point
                
                else:
                    print("NEW ITERATION")
                    return findNextChar(next_point, remaining_word, direction)

            else:
                return False
        
        for i in range(rows):
            for j in range(cols):
                grid_pointer = Point(j, i)

                print("grid_word: ", self.puzzle[grid_pointer.y][grid_pointer.x])

                if self.puzzle[grid_pointer.y][grid_pointer.x] == word[0]:
                    print("MATCH!! word[0]: ", word[0])

                    remaining_word = word[1:]

                    if not remaining_word:
                        ans.append([grid_pointer, grid_pointer])

                    else:
                        for direction in self.moves:
                            print("direction: ", direction)

                            next_point = Point(grid_pointer.x + direction[0], grid_pointer.y + direction[1])
                            print("next_point,y", next_point.y)
                            print("next_point,x", next_point.x)
                            

                            if next_point.x < 0 or next_point.x >= cols or next_point.y < 0 or next_point.y >= rows:
                                print("SKIP")
                                continue
                            
                            print("next_point_char: ", self.puzzle[next_point.y][next_point.x])

                            if self.puzzle[next_point.y][next_point.x] == remaining_word[0]:
                                print("SELECTED: ", self.puzzle[next_point.y][next_point.x])
                                

                                remainder_word = remaining_word[1:]
                                print("remainder_word: ", remainder_word)

                                if not remainder_word:
                                    ans.append([grid_pointer, next_point])

                                else:
                                    print("HERE")
                                    sol = findNextChar(next_point, remainder_word, direction)
                                    if sol:
                                        ans.append([(grid_pointer.x, grid_pointer.y), (sol.x, sol.y)])
                                        return ans
                                    else:
                                        continue
        print(ans)
        return ans
    
    
