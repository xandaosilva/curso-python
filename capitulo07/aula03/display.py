from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit
from utils import isEmpty, isNumOrDot
from variables import FONT_SIZE_LG, TEXT_MARGIN, MINIMUM_WIDTH

class Display(QLineEdit):
    eqPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()
    inputPressed = Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f"font-size: {FONT_SIZE_LG}px")
        self.setMinimumHeight(FONT_SIZE_LG * 2)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*[TEXT_MARGIN for _ in range(4)])

    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text().strip()
        key = event.key()
        KEYS = Qt.Key
        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return, KEYS.Key_Equal]
        isDelete = key in [KEYS.Key_Backspace, KEYS.Key_Delete, KEYS.Key_D]
        isEsc = key in [KEYS.Key_Escape, KEYS.Key_C]

        if isEnter:
            print("Eq pressionado, sinal emitido", type(self).__name__)
            self.eqPressed.emit()
            return event.ignore()
        
        if isDelete:
            print("Del pressionado, sinal emitido", type(self).__name__)
            self.delPressed.emit()
            return event.ignore()
        
        if isEsc:
            print("Esc pressionado, sinal emitido", type(self).__name__)
            self.clearPressed.emit()
            return event.ignore()

        if isEmpty(text):
            return event.ignore()

        if isNumOrDot(text):
            print(f"{text} pressionado, sinal emitido", type(self).__name__)
            self.inputPressed.emit()
            return event.ignore()
