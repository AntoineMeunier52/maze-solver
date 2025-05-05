class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, color):
        canvas.create_line(
            self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=color, width=2
        )

class Cell():
    def __init__(self, window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True 
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None 
        self._y1 = None 
        self._y2 = None
        self._win = window
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "black")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "black")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "black")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "black")

    def draw_breaking_wall(self):
        if not self.has_left_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(line, "white")
        if not self.has_right_wall:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(line, "white")
        if not self.has_top_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line, "white")
        if not self.has_bottom_wall:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False):
        curr_half = abs(self._x2 - self._x1) // 2
        curr_x_center = curr_half + self._x1
        curr_y_center = curr_half + self._y1

        to_half = abs(to_cell._x2 - to_cell._x1) // 2
        to_x_center = to_half + to_cell._x1
        to_y_center = to_half + to_cell._y1

        line = Line(Point(curr_x_center, curr_y_center), Point(to_x_center, to_y_center))

        color = "red"
        if undo:
            color = "gray"

        self._win.draw_line(line, color)


