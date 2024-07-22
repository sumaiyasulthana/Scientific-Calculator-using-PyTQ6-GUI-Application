#pip install PyQt6
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit,QHBoxLayout
import math
import sys 

class CalculatorUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Scientific Calculator")
        self.setGeometry(100, 100, 300, 400)

         # Set background color for the main window
        self.setStyleSheet("background-color: #BD9A82;")  # Light gray background #f0f0f0

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.entry = QLineEdit()
        self.entry.setReadOnly(True)
        self.entry.setStyleSheet("background-color: #ffffff;")  # Set white background color
        self.layout.addWidget(self.entry)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('(', ')', 'C', 'AC'),
            ('sin', 'cos', 'tan', 'log'),
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+'),
            ('sqrt', 'pow', 'pi', 'e')
        ]

        for row in buttons:
            button_row = QHBoxLayout()
            for button_text in row:
                button = QPushButton(button_text)
                button.clicked.connect(self.on_button_click)
                button_row.addWidget(button)
            self.layout.addLayout(button_row)

    def on_button_click(self):
        button = self.sender()
        button_text = button.text()

        if button_text == '=':
            try:
                result = str(eval(self.entry.text()))
                self.entry.setText(result)
            except Exception as e:
                self.entry.setText("Error")

        elif button_text == 'C':
            current_text = self.entry.text()
            self.entry.setText(current_text[:-1])

        elif button_text == 'AC':
            self.entry.clear()

        elif button_text == 'sqrt':
            try:
                result = math.sqrt(float(self.entry.text()))
                self.entry.setText(str(result))
            except ValueError:
                self.entry.setText("Error")

        elif button_text == 'pow':
            try:
                result = str(eval(self.entry.text()))
                self.entry.setText(result)
            except Exception as e:
                self.entry.setText("Error")

        elif button_text == 'pi':
            self.entry.setText(str(math.pi))

        elif button_text == 'e':
            self.entry.setText(str(math.e))

        else:
            current_text = self.entry.text()
            new_text = current_text + button_text
            self.entry.setText(new_text)


if __name__ == "__main__":
    app = QApplication([])
    calculator = CalculatorUI()
    calculator.show()
    app.exec()
