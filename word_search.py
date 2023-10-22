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

    def is_within_bounds(self, point):
        return 0 <= point.x < self.cols and 0 <= point.y < self.rows
    
    def is_char_at_position(self, point, character):
        return self.puzzle[point.y][point.x] == character
    
    def get_next_point(self, current_point, direction):
        next_x = current_point.x + direction[0]
        next_y = current_point.y + direction[1]
        return Point(next_x, next_y)

    def find_next_char(self, point, word, direction):
        next_point = self.get_next_point(point, direction)

        if self.is_within_bounds(next_point) and self.is_char_at_position(next_point,word[0]):
            remaining_word = word[1:]

            if not remaining_word:
                return next_point
            
            else:
                return self.find_next_char(next_point, remaining_word, direction)

        else:
            return False
    
    def search(self, word):
        for i in range(self.rows):
            for j in range(self.cols):
                start_point = Point(j, i)

                if self.is_char_at_position(start_point, word[0]):
                    remaining_word = word[1:]

                    if not remaining_word:
                        return (start_point, start_point) 

                    for direction in self.moves:
                        next_point =self.get_next_point(start_point, direction)

                        if not self.is_within_bounds(next_point):
                            continue
                        
                        elif self.is_char_at_position(next_point, remaining_word[0]):
                            remainder_word = remaining_word[1:]
                        
                            if not remainder_word:
                                return (start_point, next_point)

                            else:
                                sol = self.find_next_char(next_point, remainder_word, direction)
                                if sol:
                                    return (start_point, sol)
                                    
                                else:
                                    continue
        return None
    
    
