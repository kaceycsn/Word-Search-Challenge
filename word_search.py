class Point:
    def __init__(self, x, y):
        """Initialize a Point object with x and y coordinates.

        Keyword arguments:
            x (int) -- the x-coordinate.
            y (int) -- the y-coordinate.
        """
        self.x = x
        self.y = y

    def __eq__(self, other):
        """Check if two Point objects are equal by comparing their coordinates.

        Keyword arguments:
            other (Point): The other Point object to compare.

        Returns:
            bool: True if the two Points have the same coordinates, False otherwise.
        """
        return self.x == other.x and self.y == other.y


class WordSearch:
    def __init__(self, puzzle):
        """Initialize a WordSearch object with a puzzle grid.

        This constructor sets up a WordSearch object with the provided puzzle grid.

        Keyword arguments:
            puzzle (List[str]): A list of strings representing the puzzle grid.
                Each string in the list represents a row of characters.

        Raises:
            ValueError: If the puzzle is not valid (e.g., empty or rows of different lengths).

        Attributes:
            puzzle (List[str]): The puzzle grid represented as a list of strings.
            moves (List[Tuple[int, int]]): A list of valid moves for searching words.
            rows (int): The number of rows in the puzzle grid.
            cols (int): The number of columns in the puzzle grid.
        """
        if not puzzle or not all(len(row) == len(puzzle[0]) for row in puzzle):
            raise ValueError("Puzzle is not valid. All rows should have the same length.")

        self.puzzle = puzzle
        self.moves = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        self.rows = len(puzzle)
        self.cols = len(puzzle[0])

    def is_within_bounds(self, point):
        """Check if a Point is within the bounds of the puzzle grid.

        Keyword arguments:
            point (Point): The Point to check.

        Returns:
            bool: True if the Point is within bounds, False otherwise.
        """
        return 0 <= point.x < self.cols and 0 <= point.y < self.rows
    
    def is_char_at_position(self, point, character):
        """Check if a specific character is at a given Point in the puzzle grid.

        Keyword arguments:
            point (Point): The Point to check.
            character (str): The character to compare with.

        Returns:
            bool: True if the character is at the specified Point, False otherwise.
        """
        return self.puzzle[point.y][point.x] == character
    
    def get_next_point(self, current_point, direction):
        """Calculate the next Point based on the current Point and a direction.

        Keyword arguments:
            current_point (Point): The current Point.
            direction (tuple): A tuple representing the direction (e.g., (1, 0) for right).

        Returns:
            Point: The next Point based on the direction.
        """
        next_x = current_point.x + direction[0]
        next_y = current_point.y + direction[1]
        return Point(next_x, next_y)

    def find_next_char(self, point, word, direction):
        """Find the next character in a given direction from a Point.

        Keyword arguments:
            point (Point): The starting Point.
            word (str): The remaining word to find.
            direction (tuple): A tuple representing the direction.

        Returns:
            Union[Point, bool]: The next Point if a character is found, False otherwise.
        """
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
        """Search for a word in the puzzle grid.

        Keyword arguments:
            word (str): The word to search for.

        Returns:
            Union[Tuple[Point, Point], None]: A tuple of start and end Points if the word is found,
            None if the word is not found.
        """
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