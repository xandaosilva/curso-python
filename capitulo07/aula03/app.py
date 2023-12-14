import sys
from main_window import MainWindow
from buttons import Button
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

    info = Info("2.0 ^ 10.0 = 1024")
    window.addWidgetToVLayout(info)

    display = Display()
    window.addWidgetToVLayout(display)

    button = Button("Clique aqui")
    window.addWidgetToVLayout(button)

    window.adjustFixedSize()
    window.show()
    app.exec()
