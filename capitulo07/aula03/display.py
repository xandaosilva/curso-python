from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit
from variables import FONT_SIZE_LG, TEXT_MARGIN, MINIMUM_WIDTH

class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f"font-size: {FONT_SIZE_LG}px")
        self.setMinimumHeight(FONT_SIZE_LG * 2)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*[TEXT_MARGIN for _ in range(4)])
