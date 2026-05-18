class Font:
    def __init__(self, filename, default_size, ui_name):
        self._filename = filename
        self._default_size = default_size
        self._ui_name = ui_name
        

    def get_filename(self):
        return self._filename

    def get_default_size(self):
        return self._default_size

    def set_default_size(self, size):
        self._default_size = size

    def get_ui_name(self):
        return self._ui_name

    def print(self):
        return f"{self._filename};{self._default_size};{self._ui_name}\n"
