import sys
from main_window import MainWindow
from buttons import ButtonsGrid
from display import Display
from info import Info
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from styles import setupTheme
from variables import WINDOW_ICON_PATH

if __name__ == "__main__":
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()
    icon = QIcon(str(WINDOW_ICON_PATH))

    app.setWindowIcon(icon)

    info = Info("Operação")
    window.addWidgetToVLayout(info)

    display = Display()
    window.addWidgetToVLayout(display)

    buttonsGrid = ButtonsGrid(display, info, window)
    buttonsGrid._makeGrid()
    window.v_layout.addLayout(buttonsGrid)

    window.adjustFixedSize()
    window.show()
    app.exec()
