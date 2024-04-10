from PyQt5.QtWidgets import QMenuBar, QMenu, QAction
from PyQt5.QtGui import QIcon

def create_menu_bar(window):
    menu_bar = QMenuBar()

    # Create the File menu and add actions
    file_menu = QMenu("&File", window)
    menu_bar.addMenu(file_menu)

    open_action = QAction(QIcon(), "&Open", window)
    file_menu.addAction(open_action)

    save_action = QAction(QIcon(), "&Save", window)
    file_menu.addAction(save_action)

    return menu_bar
