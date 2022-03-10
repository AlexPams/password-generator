from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLayout, QVBoxLayout, QWidget, QLineEdit
from passwordgenerator import generate


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.password = ' '
        self.password_length = 8

        self.setWindowTitle("Password Generator")
        self.button_generate_password = QPushButton("Generate")
        self.label_password = QLabel(str(self.password))
        self.label_password_length = QLabel("Введите длинну пароля")
        self.lineedit_password_length = QLineEdit()

        self.button_generate_password.clicked.connect(self.button_generate_password_is_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.label_password_length)
        layout.addWidget(self.lineedit_password_length)
        layout.addWidget(self.label_password)
        layout.addWidget(self.button_generate_password)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def button_generate_password_is_clicked(self):
        self.password = generate(int(self.lineedit_password_length.text()))
        self.label_password.setText(str(self.password))


app = QApplication([])

window = MainWindow()
window.show()
app.exec()
