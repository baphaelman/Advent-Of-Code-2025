from Point import Point

class Grid:
    def __init__(self, size):
        self.map: dict[Point, str] = {}
        self.x = size[0]
        self.y = size[1]

    def get(self, square: Point):
        return self.map[square]
    
    def set(self, square: Point, s: str):
        self.map[square] = s

    def find(self, s):
        """Returns one point where grid has s"""
        for i in range(self.x):
            for j in range(self.y):
                if self.get(Point(i, j)) == s:
                    return Point(i, j)
    
    def get_row(self, y):
        row = []
        for x in range(self.x):
            p = Point(x, y)
            row.append(self.get(p))
        return row
    
    def __str__(self):
        result = ""
        for y in range(self.y):
            for x in range(self.x):
                result += self.get(Point(x, y))
            result += "\n"
        return result
    
    """FOR SPECIFIC PROBLEMS"""
    def tachyon_fill(self):
        """Fills 'empty' tachyon grid"""
        S_pos = self.find("S")
        beams_at = set()
        beams_at.add(S_pos.x)
        for y in range(S_pos.y + 1, self.y):
            new_beams_at = set()
            for x in beams_at:
                p = Point(x, y)
                s = self.get(p)
                if s == '.':
                    self.set(p, '|')
                    new_beams_at.add(x)
                elif s == '^':
                    if x > 0:
                        p2 = Point(x - 1, y)
                        new_beams_at.add(x - 1)
                        self.set(p2, '|')
                    if x < self.x - 1:
                        p3 = Point(x + 1, y)
                        new_beams_at.add(x + 1)
                        self.set(p3, '|')
            beams_at = new_beams_at