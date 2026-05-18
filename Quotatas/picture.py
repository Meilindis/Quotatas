class Picture:
    def __init__(self, filename, colour, alignment, location, x_offset, y_offset):
        self._filename = filename
        self._colour = colour
        self._alignment = alignment
        self._location = location
        self._x_offset = x_offset
        self._y_offset = y_offset

    def get_filename(self):
        return self._filename

    def get_colour(self):
        return self._colour

    def set_colour(self, colour):
        self._colour = colour

    def get_alignment(self):
        return self._alignment

    def get_location(self):
        return self._location

    def set_location(self, location):
        self._location = location

    def get_x_offset(self):
        return self._x_offset

    def get_y_offset(self):
        return self._y_offset

    def print(self):
        return f"{self._filename};{self._colour};{self._alignment};{self._location};{self._x_offset};{self._y_offset}\n"
