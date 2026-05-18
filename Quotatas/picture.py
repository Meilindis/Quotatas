class Picture:
    def __init__(self, filename, colour, alignment, location, x_offset, y_offset):
        self._filename = filename
        self._colour = colour
        self._alignment = alignment
        self._location = location
        self._x_offset = x_offset
        self._y_offset = y_offset
        self._x = self._x_offset
        self._y = self._y_offset

        self._text_block_height = -1

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

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, value):
        self._x = value

    def set_y(self, value):
        self._y = value

    def increase_x(self):
        if self._x < 500:
            self._x_offset += 1

    def decrease_x(self):
        if self._x > 0:
            self._x_offset -= 1

    def increase_y(self):
        if self._y < (500 - self._text_block_height):
            self._y_offset += 1

    def decrease_y(self):
        if self._y > -12: # Take into account the default indentation and the extra space of the overlay
            self._y_offset -= 1

    def get_text_block_height(self):
        return self._text_block_height

    def set_text_block_height(self, height):
        self._text_block_height = height

    def print(self):
        return f"{self._filename};{self._colour};{self._alignment};{self._location};{self._x_offset};{self._y_offset}\n"
