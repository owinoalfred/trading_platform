from PyQt5.QtWidgets import QMainWindow, QTextEdit, QStatusBar
from components.menu_bar import create_menu_bar
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Trading Platform")

        # Create the text edit widget and set it as the central widget
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        # Create the menu bar
        self.setMenuBar(create_menu_bar(self))

        # Create the status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        # Style the widgets
        self.setStyleSheet("""
            QMainWindow {
                background-color: #333;
            }

            QTextEdit {
                background-color: #222;
                color: #fff;
                font-size: 16px;
            }

            QMenuBar {
                background-color: #444;
            }

            QMenuBar::item {
                color: #fff;
            }

            QStatusBar {
                background-color: #444;
                color: #fff;
            }
        """)