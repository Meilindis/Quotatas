from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QColor

custom_colors = [
        QColor(255, 255, 255),    # White
        QColor(0, 0, 0),          # Black
        QColor(199, 17, 234),     # Magenta
        QColor(29, 37, 82),       # Dark blue
        QColor(142, 255, 221),    # Cyan
        QColor(255, 245, 185),    # Peach
        QColor(65, 75, 139),      # Periwinkle
        QColor(167, 255, 174),    # Mint
        QColor(145, 0, 140),      # Fuchsia
        QColor(207, 220, 255),    # Ice blue
        QColor(255, 245, 215),    # Beige
        QColor(24, 0, 59),        # Eggplant
    ]

class ColorButton(QtWidgets.QPushButton):
    '''
    Custom Qt Widget to show a chosen color.

    Left-clicking the button shows the color-chooser, while
    right-clicking resets the color to None (no-color).
    '''

    colorChanged = Signal(object)

    def __init__(self, *args, color=None, **kwargs):
        super().__init__(*args, **kwargs)

        self._color = None
        self._default = color
        self.pressed.connect(self.onColorPicker)

        # Set the initial/default state.
        self.setColor(self._default)

    def setColor(self, color):
        if color != self._color:
            self._color = color
            self.colorChanged.emit(color)

        if self._color:
            self.setStyleSheet("background-color: %s;" % self._color)
        else:
            self.setStyleSheet("")

    def color(self):
        return self._color

    def onColorPicker(self):
        '''
        Show color-picker dialog to select color.

        Qt will use the native dialog by default.

        '''
        dlg = QtWidgets.QColorDialog(self)

        # Include all the default colours
        for i, color in enumerate(custom_colors):
            dlg.setCustomColor(i, color.rgb())

        if self._color:
            dlg.setCurrentColor(QtGui.QColor(self._color))

        if dlg.exec_():
            self.setColor(dlg.currentColor().name())

    def mousePressEvent(self, e):
        if e.button() == Qt.RightButton:
            self.setColor(self._default)

        return super().mousePressEvent(e)
        