from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QWidget
from variables import FONT_SIZE_SM

class Info(QLabel):
    def __init__(self, text: str, parent: QWidget | None = None) -> None:
        super().__init__(text, parent)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f"font-size: {FONT_SIZE_SM}px")
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
