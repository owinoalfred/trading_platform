from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Trading Platform")

        label = QLabel("Hello, PyQt!")
        self.setCentralWidget(label)

def main():
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec_()

if __name__ == "__main__":
    main()