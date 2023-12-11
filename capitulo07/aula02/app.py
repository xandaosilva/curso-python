import sys
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QMainWindow, QPushButton
# from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
# layout = QVBoxLayout()
# layout = QHBoxLayout()

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)

button_a, button_b, button_c = QPushButton("Clique aqui 1"), QPushButton("Clique aqui 2"), QPushButton("Clique aqui 3")

button_a.setStyleSheet("font-size: 30px;")
button_b.setStyleSheet("font-size: 30px;")
button_c.setStyleSheet("font-size: 30px;")

layout = QGridLayout()

central_widget.setLayout(layout)

layout.addWidget(button_a, 1, 1, 1, 1)
layout.addWidget(button_b, 1, 2, 1, 1)
layout.addWidget(button_c, 3, 1, 1, 2)

status_bar = window.statusBar()
status_bar.showMessage("Mensagem que será exibida")

menu = window.menuBar()

first_menu = menu.addMenu("Primeiro menu")

first_action = first_menu.addAction("Primeira ação")
second_action = first_menu.addAction("Segunda ação")
third_action = first_menu.addAction("Terceira ação")

# central_widget.show()
window.show()
app.exec()
