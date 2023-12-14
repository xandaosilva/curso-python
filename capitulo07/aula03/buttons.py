from PySide6.QtWidgets import QPushButton
from variables import FONT_SIZE_MD

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(FONT_SIZE_MD)
        self.setFont(font)
        self.setMinimumSize(75, 75)
        self.setProperty("cssClass", "specialButton")
