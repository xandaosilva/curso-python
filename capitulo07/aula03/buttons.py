import math
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QPushButton, QGridLayout
from variables import FONT_SIZE_SM
from utils import isEmpty, isNumOrDot, isValidNumber

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from display import Display
    from info import Info
    from main_window import MainWindow

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(FONT_SIZE_SM)
        self.setFont(font)
        self.setMinimumSize(50, 50)


class ButtonsGrid(QGridLayout):
    def __init__(self, display: "Display", info: "Info", window: "MainWindow", *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._gridMask = [
                ['C', '◀', '^', '/'],
                ['7', '8', '9', '*'],
                ['4', '5', '6', '-'],
                ['1', '2', '3', '+'],
                ['',  '0', '.', '='],
        ]
        self.display = display
        self.info = info
        self.window = window
        self._equation = ""
        self._equationInitialValue = "Operação"
        self._left = None
        self._right = None
        self._op = None
        self.equation = self._equationInitialValue
        self._makeGrid()

    @property
    def equation(self):
        return self._equation
    
    @equation.setter
    def equation(self, equation):
        self._equation = equation
        self.info.setText(equation)

    def vouApagarVoce(self):
        print("Signal recebido:", type(self).__name__)

    def _makeGrid(self):
        self.display.eqPressed.connect(self.vouApagarVoce)
        self.display.delPressed.connect(self.display.backspace)
        self.display.clearPressed.connect(self.vouApagarVoce)
        self.display.inputPressed.connect(self.vouApagarVoce)

        for i, row in enumerate(self._gridMask):
            for j, button_text in enumerate(row):
                button = Button(button_text)
                if not isNumOrDot(button_text) and not isEmpty(button_text):
                    button.setProperty("cssClass", "specialButton")
                    self._configSpecialButton(button)
                self.addWidget(button, i, j)
                slot = self._makeSlot(self._insertButtonTextToDisplay, button)
                self._connectButtonClicked(button, slot)

    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button):
        text = button.text()
        
        if text == "C":
            self._connectButtonClicked(button, self._clear)

        if text in "+-*/^":
            self._connectButtonClicked(button, self._makeSlot(self._operatorClicked, button))
        
        if text == "=":
            self._connectButtonClicked(button, self._eq)
        
        if text == "◀":
            self._connectButtonClicked(button, self.display.backspace)

    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot():
            func(*args, **kwargs)
        return realSlot

    def _insertButtonTextToDisplay(self, button):
        button_text = button.text()
        new_display_value = self.display.text() + button_text

        if not isValidNumber(new_display_value):
            return

        self.display.insert(button_text)

    def _clear(self):
        self._left = None
        self._right = None
        self._op = None
        self.equation = self._equationInitialValue
        self.display.clear()

    def _operatorClicked(self, button):
        buttonText = button.text()
        displayText = self.display.text()
        self.display.clear()

        if not isValidNumber(displayText) and self._left is None:
            self._showError("Informe um valor")
            return
        
        if self._left is None:
            self._left = float(displayText)

        self._op = buttonText
        self.equation = f"{self._left} {self._op} ??"

    def _eq(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            return
        
        self._right = float(displayText)
        self.equation = f"{self._left} {self._op} {self._right}"
        result = "error"

        try:
            if "^" in self.equation and isinstance(self._left, float):
                result = math.pow(self._left, self._right)
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
            self._showError("Impossível dividir por Zero")
        except OverflowError:
            self._showInfo("Número extenso")

        self.display.clear()
        self.info.setText(f"{self.equation} = {result}")
        self._left = result
        self._right = None

        if result == "error":
            self._left = None

    def _makeDialog(self, text):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
        return msgBox

    def _showError(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setIcon(msgBox.Icon.Critical)
        msgBox.exec()
    
    def _showInfo(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setIcon(msgBox.Icon.Information)
        msgBox.exec()
